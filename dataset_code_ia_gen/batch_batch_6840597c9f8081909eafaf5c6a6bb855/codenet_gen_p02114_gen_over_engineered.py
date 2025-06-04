class CellColor:
    WHITE = 'o'
    BLACK = 'x'

class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"Pos({self.row},{self.col})"

class Grid:
    def __init__(self, size: int, data: list):
        self.size = size
        self.data = data  # 2D list, each element CellColor.WHITE or CellColor.BLACK

    def color_at(self, pos: Position) -> str:
        return self.data[pos.row][pos.col]

    def is_white(self, pos: Position) -> bool:
        return self.color_at(pos) == CellColor.WHITE

    def is_black(self, pos: Position) -> bool:
        return self.color_at(pos) == CellColor.BLACK

    def set_black(self, pos: Position):
        self.data[pos.row][pos.col] = CellColor.BLACK

    def in_bounds(self, pos: Position) -> bool:
        return 0 <= pos.row < self.size and 0 <= pos.col < self.size

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.data)

class Direction:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    @staticmethod
    def all_dirs():
        return [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

class FissureOperation:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.size = grid.size

    def _chain_black_in_direction(self, start_pos: Position, direction: tuple):
        drow, dcol = direction
        cur = Position(start_pos.row + drow, start_pos.col + dcol)
        while self.grid.in_bounds(cur) and self.grid.is_white(cur):
            self.grid.set_black(cur)
            cur = Position(cur.row + drow, cur.col + dcol)

    def select_cell_and_blacken(self, pos: Position):
        if not (pos.row % 2 == 1 and pos.col % 2 == 1):
            raise ValueError("Can only select cells at odd-indexed rows and columns (1-based even position => 0-based odd)")
        if self.grid.is_black(pos):
            return
        self.grid.set_black(pos)
        for direction in Direction.all_dirs():
            self._chain_black_in_direction(pos, direction)

class Pattern:
    """
    Represents the black/white pattern we want to achieve.
    """
    def __init__(self, size: int, pattern_grid: list):
        self.size = size
        self.pattern_grid = pattern_grid

    def color_at(self, pos: Position) -> str:
        return self.pattern_grid[pos.row][pos.col]

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.pattern_grid)

class Solver:
    """
    Encapsulates solving logic for the fissure puzzle easy problem.
    """
    def __init__(self, N: int, pattern_grid: list):
        self.N = N
        self.pattern = Pattern(N, pattern_grid)
        self.current_grid = Grid(N, [[CellColor.WHITE]*N for _ in range(N)])
        self.fissure_operation = FissureOperation(self.current_grid)
        # Cache of corner candidates (cells at even rows and cols 1-based -> odd 0-based)
        self.selection_candidates = []
        for r in range(1, N, 2):
            for c in range(1, N, 2):
                self.selection_candidates.append(Position(r,c))

    def _pos_repr(self, pos):
        return f"(r={pos.row+1},c={pos.col+1})"

    def solve(self) -> int:
        # The key insight from editorial: 
        # The puzzle maps to the XOR of restriction on 2x2 subgrids (mod 2),
        # and selecting cells at positions with both odd indexes (0-based) toggles a
        # cross-shaped pattern covering entire rows or columns.
        # The problem reduces to solving a linear system over GF(2). But here we implement
        # a sophisticated abstraction anticipating extension.

        # Represent black=1, white=0 for convenience in the system
        # Construct "target" as binary matrix of black=1, white=0
        target_bin = [[1 if c == CellColor.BLACK else 0 for c in row] for row in self.pattern.pattern_grid]

        # The toggle effect of selecting a cell at (i,j) with i,j odd (0-based) is:
        # It toggles (flips) the cell itself and all cells in the same row and same column?
        # No — the toggling is: the selected cell becomes black and then the four directions
        # turn white cells black continuously until a black cell or border is reached
        #
        # However, since all changes are monotonous from white to black, we only model XOR
        # because it's "select or not select" - we must find minimal such toggles.
        #
        # The solution is from the editorial to the original Fissure Puzzle Easy:
        # Presence of black cell only depends on parity of toggles on the corresponding crosses.
        #
        # Because of the problem size (N odd and ≤127), we can represent the system as a vector of bits,
        # with variables corresponding to possible selection points at (odd,odd)

        import copy

        # Index map for variables: key = (row,col), value = index in variables
        var_index = {}
        idx = 0
        for r in range(1,self.N,2):
            for c in range(1,self.N,2):
                var_index[(r,c)] = idx
                idx += 1
        var_num = idx

        # Each cell (i,j) is affected by variable x if and only if:
        # x == selected cell at (r,c) odd odd 0-based, and the effect covers cell (i,j).
        #
        # The effect of selecting cell (r,c):
        # toggles cell (r,c) black
        # toggles black all white cells upwards until black or boundary:
        # => all cells (k,c) with k<r that are white are turned black, up to boundary or black cell.
        # similarly down, left, right.
        #
        # Note: The effect is monotonic, and since the puzzle guarantees always possible, modeling as XOR is valid.
        #
        # We simulate effect of each variable on each cell to build linear system.

        # Build the matrix encoding effects
        # We represent system as: M x = b mod 2
        # M is (N*N) x var_num matrix, b is flattened target vector length (N*N)

        M = [[0]*var_num for _ in range(self.N*self.N)]
        b = [0]*(self.N*self.N)

        # Helper for position to linear index
        def pos_to_idx(p):
            return p.row*self.N + p.col

        # Precompute grid black/white for each variable impact by simulating one toggle
        for (r,c), var_id in var_index.items():
            # Create empty grid (all 0=white)
            sim_grid = [[0]*self.N for _ in range(self.N)]
            # Select cell (r,c)
            sim_grid[r][c] = 1
            # chain upwards
            rr = r-1
            while rr >=0 and sim_grid[rr][c] == 0:
                sim_grid[rr][c] = 1
                rr -=1
            # chain downwards
            rr = r+1
            while rr < self.N and sim_grid[rr][c] == 0:
                sim_grid[rr][c] = 1
                rr +=1
            # chain leftwards
            cc = c-1
            while cc >=0 and sim_grid[r][cc] == 0:
                sim_grid[r][cc] = 1
                cc -=1
            # chain rightwards
            cc = c+1
            while cc < self.N and sim_grid[r][cc] == 0:
                sim_grid[r][cc] = 1
                cc +=1
            for i in range(self.N):
                for j in range(self.N):
                    M[pos_to_idx(Position(i,j))][var_id] = sim_grid[i][j]

        # Build vector b from target black cells (1) or white cells (0)
        for i in range(self.N):
            for j in range(self.N):
                b[pos_to_idx(Position(i,j))] = target_bin[i][j]

        # Solve linear system M x = b mod 2 by Gauss-Jordan elimination

        def gauss_jordan(M, b):
            rows = len(M)
            cols = len(M[0])
            M = [row[:] for row in M]  # copy
            b = b[:]
            rank = 0
            for col in range(cols):
                pivot = -1
                for r in range(rank, rows):
                    if M[r][col] == 1:
                        pivot = r
                        break
                if pivot == -1:
                    continue
                # swap pivot row with current rank row
                if pivot != rank:
                    M[rank], M[pivot] = M[pivot], M[rank]
                    b[rank], b[pivot] = b[pivot], b[rank]
                # eliminate below and above
                for r in range(rows):
                    if r != rank and M[r][col] == 1:
                        for c in range(col, cols):
                            M[r][c] ^= M[rank][c]
                        b[r] ^= b[rank]
                rank += 1
            # Back substitution to produce solution, variables correspond to cols
            x = [0]*cols
            for r in range(rank-1, -1, -1):
                # find leading col
                lead_col = -1
                for c in range(cols):
                    if M[r][c] == 1:
                        lead_col = c
                        break
                if lead_col == -1:
                    continue
                x[lead_col] = b[r]
                # subtract x[lead_col] * that col from other cols (but already done)
            return x

        solution = gauss_jordan(M,b)
        # minimal number of selections = number of 1 in solution vector
        return sum(solution)

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    pattern_grid = [list(input().strip()) for _ in range(N)]
    solver = Solver(N, pattern_grid)
    ans = solver.solve()
    print(ans)

if __name__ == '__main__':
    main()