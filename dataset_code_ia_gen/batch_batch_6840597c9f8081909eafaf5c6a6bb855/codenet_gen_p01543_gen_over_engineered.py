class Cell:
    def __init__(self, row: int, col: int, write_cost: int, erase_cost: int, has_mark: bool):
        self.row = row
        self.col = col
        self.write_cost = write_cost
        self.erase_cost = erase_cost
        self.has_mark = has_mark

    def cost_to_write(self) -> int:
        return self.write_cost

    def cost_to_erase(self) -> int:
        return self.erase_cost


class Operation:
    def __init__(self, r: int, c: int, op_type: str):
        self.r = r
        self.c = c
        self.op_type = op_type  # "write" or "erase"


class Board:
    def __init__(self, n: int):
        self.n = n
        self.cells = [[None] * n for _ in range(n)]

    def set_cell(self, r: int, c: int, cell: Cell):
        self.cells[r][c] = cell

    def get_cell(self, r: int, c: int) -> Cell:
        return self.cells[r][c]

    def initial_state(self):
        return [[self.cells[i][j].has_mark for j in range(self.n)] for i in range(self.n)]


class HungarianSolver:
    # Hungarian algorithm for minimum cost perfect matching
    def __init__(self, cost_matrix):
        self.N = len(cost_matrix)
        self.cost = cost_matrix
        self.u = [0] * (self.N+1)
        self.v = [0] * (self.N+1)
        self.p = [0] * (self.N+1)
        self.way = [0] * (self.N+1)

    def solve(self):
        N = self.N
        for i in range(1,N+1):
            self.p[0] = i
            j0 = 0
            minv = [float('inf')] * (N+1)
            used = [False] * (N+1)
            while True:
                used[j0] = True
                i0 = self.p[j0]
                j1 = 0
                delta = float('inf')
                for j in range(1,N+1):
                    if not used[j]:
                        cur = self.cost[i0-1][j-1] - self.u[i0] - self.v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            self.way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                for j in range(0,N+1):
                    if used[j]:
                        self.u[self.p[j]] += delta
                        self.v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if self.p[j0] == 0:
                    break
            while True:
                j1 = self.way[j0]
                self.p[j0] = self.p[j1]
                j0 = j1
                if j0 == 0:
                    break
        # p[j] = i means i-th row assigned to j-th column
        result = [-1]*N
        for j in range(1,N+1):
            i = self.p[j]
            result[i-1] = j-1
        return result, -(self.u[0]+self.v[0])


class Solution:
    def __init__(self):
        self.n = 0
        self.board = None
        self.operations = []
        self.mincost = 0

    def input_data(self):
        import sys
        input = sys.stdin.readline
        self.n = int(input())
        n = self.n
        write_costs = [list(map(int, input().split())) for _ in range(n)]
        erase_costs = [list(map(int, input().split())) for _ in range(n)]
        initial_marks = [input().strip() for _ in range(n)]

        self.board = Board(n)
        for i in range(n):
            for j in range(n):
                has_mark = (initial_marks[i][j] == 'o')
                c = Cell(i, j, write_costs[i][j], erase_costs[i][j], has_mark)
                self.board.set_cell(i, j, c)

    def create_cost_matrix(self):
        # We want to select exactly one cell per row and column with minimal transformation cost
        # For each candidate (row,col), compute cost to fix that cell marks only:
        # If cell initially has mark: cost to erase others marks in row and col + cost to write others marks if necessary
        # Actually: better to consider for each cell (r,c) cost is the sum of erase costs of marks outside (r,c) plus write cost if (r,c) doesn't have mark.
        # Since output must be minimal total cost to achieve exactly one mark per row and col

        n = self.n
        cost_matrix = [[0]*n for _ in range(n)]

        # precompute rows and columns marks info
        initial = self.board.initial_state()

        # For efficient cost, precompute for each cell:
        # sum of erase costs of marks in row, except this cell if marked
        # sum of erase costs of marks in column, except this cell if marked
        # write cost if no mark on this cell initially

        row_erase_sum = [0]*n
        col_erase_sum = [0]*n
        for i in range(n):
            s = 0
            for j in range(n):
                if initial[i][j]:
                    s += self.board.get_cell(i,j).erase_cost
            row_erase_sum[i] = s
        for j in range(n):
            s = 0
            for i in range(n):
                if initial[i][j]:
                    s += self.board.get_cell(i,j).erase_cost
            col_erase_sum[j] = s

        for r in range(n):
            for c in range(n):
                cell = self.board.get_cell(r,c)
                cost = 0
                # erase marks in row except (r,c) if they have mark
                cost += row_erase_sum[r]
                if initial[r][c]:
                    cost -= cell.erase_cost  # exclude erase cost on chosen cell if initially marked (we keep it)
                # erase marks in column except (r,c) if they have mark
                cost += col_erase_sum[c]
                if initial[r][c]:
                    cost -= cell.erase_cost
                # if cell (r,c) no mark initially, must write mark
                if not initial[r][c]:
                    cost += cell.write_cost
                cost_matrix[r][c] = cost
        return cost_matrix

    def reconstruct_operations(self, assignment):
        # assignment[i] = column assigned to row i
        # For chosen positions, keep mark: erase marks in the row and column except chosen cell, write mark if it is not initially marked
        n = self.n
        initial = self.board.initial_state()
        ops = []
        total_cost = 0

        # We will erase every initial mark except those at (i, assignment[i])
        keep_positions = set((i, assignment[i]) for i in range(n))

        # Erase all extra marks
        for i in range(n):
            for j in range(n):
                cell = self.board.get_cell(i,j)
                if initial[i][j]:
                    if (i,j) not in keep_positions:
                        ops.append(Operation(i+1, j+1, "erase"))
                        total_cost += cell.erase_cost

        # Write marks at chosen cells if missing
        for i in range(n):
            c = assignment[i]
            cell = self.board.get_cell(i,c)
            if not initial[i][c]:
                ops.append(Operation(i+1, c+1, "write"))
                total_cost += cell.write_cost

        return total_cost, ops

    def is_goal_already(self):
        # Check if each row and column has exactly one mark initially
        n = self.n
        initial = self.board.initial_state()
        for i in range(n):
            if sum(initial[i][j] for j in range(n)) != 1:
                return False
        for j in range(n):
            if sum(initial[i][j] for i in range(n)) != 1:
                return False
        return True

    def run(self):
        if self.is_goal_already():
            print(0)
            print(0)
            return

        cost_matrix = self.create_cost_matrix()
        solver = HungarianSolver(cost_matrix)
        assignment, min_cost = solver.solve()

        total_cost, ops = self.reconstruct_operations(assignment)

        # Sanity check
        assert total_cost == min_cost, "Cost mismatch between Hungarian and reconstructed operations"

        print(min_cost)
        print(len(ops))
        for op in ops:
            print(op.r, op.c, op.op_type)


def main():
    solution = Solution()
    solution.input_data()
    solution.run()


if __name__ == "__main__":
    main()