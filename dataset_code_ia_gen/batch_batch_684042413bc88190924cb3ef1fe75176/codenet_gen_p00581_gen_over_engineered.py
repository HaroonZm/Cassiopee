class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __lt__(self, other):
        return (self.row, self.col) < (other.row, other.col)

class Grid:
    def __init__(self, height: int, width: int, layout: list[str]):
        self.height = height
        self.width = width
        self.layout = layout
        self.jewel_positions = []
        self.orb_positions = []
        self.ingot_positions = []
        self._extract_positions()

    def _extract_positions(self):
        for i in range(self.height):
            for j in range(self.width):
                cell = self.layout[i][j]
                pos = Position(i + 1, j + 1)
                if cell == 'J':
                    self.jewel_positions.append(pos)
                elif cell == 'O':
                    self.orb_positions.append(pos)
                elif cell == 'I':
                    self.ingot_positions.append(pos)

class MagicPowerCalculator:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.power = 0
        self._build_data_structures()

    def _build_data_structures(self):
        # Prepare binary indicator grids for J, O, I
        self.jewel_grid = [[0]*(self.grid.width + 1) for _ in range(self.grid.height + 1)]
        self.orb_grid = [[0]*(self.grid.width + 1) for _ in range(self.grid.height + 1)]
        self.ingot_grid = [[0]*(self.grid.width + 1) for _ in range(self.grid.height + 1)]

        for pos in self.grid.jewel_positions:
            self.jewel_grid[pos.row][pos.col] = 1
        for pos in self.grid.orb_positions:
            self.orb_grid[pos.row][pos.col] = 1
        for pos in self.grid.ingot_positions:
            self.ingot_grid[pos.row][pos.col] = 1

        # Precompute prefix sums for each grid by rows
        self.jewel_row_prefix = [[0]*(self.grid.width + 2) for _ in range(self.grid.height + 2)]
        self.orb_row_prefix = [[0]*(self.grid.width + 2) for _ in range(self.grid.height + 2)]
        self.ingot_row_prefix = [[0]*(self.grid.width + 2) for _ in range(self.grid.height + 2)]

        for i in range(1, self.grid.height + 1):
            for j in range(1, self.grid.width + 1):
                self.jewel_row_prefix[i][j] = self.jewel_row_prefix[i][j-1] + self.jewel_grid[i][j]
                self.orb_row_prefix[i][j] = self.orb_row_prefix[i][j-1] + self.orb_grid[i][j]
                self.ingot_row_prefix[i][j] = self.ingot_row_prefix[i][j-1] + self.ingot_grid[i][j]

        # Also for columns, as needed, but will optimize differently

    def _count_orbs_between(self, row: int, left: int, right: int) -> int:
        # Number of O in row at columns in (left+1 ... right-1)
        # but since j < l, l is strictly greater than j, so counting from j+1 to W
        # For our use case, will consider intervals correctly
        if left + 1 > right - 1:
            return 0
        return self.orb_row_prefix[row][right - 1] - self.orb_row_prefix[row][left]

    def compute_power(self) -> int:
        # To count quadruples (i, j, k, l) with i<k and j<l
        # where (i,j) = J, (i,l) = O, (k,j) = I
        # For each ordered pair of rows (i,k), i<k, count column pairs (j,l), j<l,
        # such that S[i][j] = J, S[i][l] = O, S[k][j] = I.

        # Observe that for fixed i,k:
        # For each column j: if S[i][j]==J and S[k][j]==I, mark column j as candidate
        # For each column l: if S[i][l]==O, mark l
        # For each candidate pair (j,l) with j<l, count.

        # We fix i < k and prepare two arrays:
        # C - indicator array for columns where S[i][j]==J and S[k][j]==I
        # O_arr - indicator array for columns where S[i][l]==O

        # Then for each i,k we count pairs j<l with j in C, l in O_arr.

        # To count pairs efficiently, we can:
        # For l from 1 to W:
        # Maintain prefix count of C columns up to l-1
        # When l is an O column, add prefix count to result.

        power = 0
        H, W = self.grid.height, self.grid.width
        layout = self.grid.layout

        for i in range(H - 1):
            for k in range(i + 1, H):
                mask_c = [0] * W
                mask_o = [0] * W
                for col in range(W):
                    if layout[i][col] == 'J' and layout[k][col] == 'I':
                        mask_c[col] = 1
                    if layout[i][col] == 'O':
                        mask_o[col] = 1
                prefix_c = 0
                for l in range(W):
                    if mask_c[l]:
                        prefix_c += 1
                    if mask_o[l]:
                        power += prefix_c
        self.power = power
        return self.power

class InputOutputHandler:
    @staticmethod
    def read_input() -> Grid:
        H, W = map(int, input().split())
        layout = [input().strip() for _ in range(H)]
        return Grid(H, W, layout)

    @staticmethod
    def output_result(power: int):
        print(power)

def main():
    grid = InputOutputHandler.read_input()
    calculator = MagicPowerCalculator(grid)
    power = calculator.compute_power()
    InputOutputHandler.output_result(power)

if __name__ == "__main__":
    main()