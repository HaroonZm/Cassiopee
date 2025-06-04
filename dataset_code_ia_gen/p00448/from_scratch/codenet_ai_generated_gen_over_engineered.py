class SenbeiState:
    def __init__(self, R: int, C: int, grid: list[list[int]]):
        self.R = R
        self.C = C
        self.grid = grid  # grid[row][col], 0-based indexing

    def flipped_rows(self, flip_mask: int) -> 'SenbeiState':
        """Return a new state with rows flipped according to flip_mask bits."""
        new_grid = []
        for r in range(self.R):
            flip = (flip_mask >> r) & 1
            if flip:
                # Flip the entire row: 0 -> 1, 1 -> 0
                new_row = [1 - cell for cell in self.grid[r]]
            else:
                new_row = self.grid[r][:]
            new_grid.append(new_row)
        return SenbeiState(self.R, self.C, new_grid)

    def flipped_cols(self, flip_mask: int) -> 'SenbeiState':
        """Return a new state with columns flipped according to flip_mask bits."""
        new_grid = [row[:] for row in self.grid]
        for c in range(self.C):
            flip = (flip_mask >> c) & 1
            if flip:
                for r in range(self.R):
                    new_grid[r][c] = 1 - new_grid[r][c]
        return SenbeiState(self.R, self.C, new_grid)

    def count_face_up(self) -> int:
        """Count number of senbei showing front (1)."""
        return sum(sum(row) for row in self.grid)


class FlipOperation:
    """Abstract flip operation for rows or columns."""
    def __init__(self, dimension: int, flip_mask: int):
        self.dimension = dimension
        self.flip_mask = flip_mask

    def apply_to_state(self, state: SenbeiState, axis: str) -> SenbeiState:
        if axis == 'row':
            return state.flipped_rows(self.flip_mask)
        elif axis == 'col':
            return state.flipped_cols(self.flip_mask)
        else:
            raise ValueError("Axis must be 'row' or 'col'.")


class SenbeiFlipper:
    def __init__(self, state: SenbeiState):
        self.initial_state = state
        self.R = state.R
        self.C = state.C

    def _column_pattern_for_row_flips(self, row_flip_mask: int) -> tuple[int, ...]:
        """
        For given row flips, compute the pattern of each column after row flips.
        Represents each column as an integer bitmask of length R.
        """
        patterns = []
        for c in range(self.C):
            col_pattern = 0
            for r in range(self.R):
                cell = self.initial_state.grid[r][c]
                # if row flipped, cell is flipped
                if (row_flip_mask >> r) & 1:
                    cell = 1 - cell
                col_pattern |= (cell << r)
            patterns.append(col_pattern)
        return tuple(patterns)

    def maximize_shipment(self) -> int:
        """
        Implements the solution:
        - enumerate all possible row flip states (2^R)
        - for each, compute column bit patterns after row flips
        - count frequencies of each pattern (= number of columns with that pattern)
        - We can flip columns with pattern p to pattern p ^ (2^R -1) (invert all bits)
        - For each unique pattern count, decide to flip columns or not for max count
        - Sum max counts => max number of shipment senbei in this row flip configuration
        - Track global maximum over all row flip configurations
        """
        max_shipment = 0
        full_mask = (1 << self.R) - 1
        # To avoid double counting pairs, we use a dictionary and process pairs carefully
        from collections import Counter

        for row_flip_mask in range(1 << self.R):
            column_patterns = self._column_pattern_for_row_flips(row_flip_mask)
            freq = Counter(column_patterns)
            visited = set()
            shipment_count = 0

            for p, cnt_p in freq.items():
                p_inv = p ^ full_mask
                if p in visited:
                    continue
                visited.add(p)
                visited.add(p_inv)
                cnt_inv = freq.get(p_inv, 0)
                shipment_count += max(cnt_p, cnt_inv)

            if shipment_count > max_shipment:
                max_shipment = shipment_count

        return max_shipment


class SenbeiProblemSolver:
    def __init__(self):
        self.datasets = []

    def add_dataset(self, R: int, C: int, grid: list[list[int]]):
        self.datasets.append(SenbeiState(R, C, grid))

    def solve_all(self) -> list[int]:
        results = []
        for state in self.datasets:
            flipper = SenbeiFlipper(state)
            result = flipper.maximize_shipment()
            results.append(result)
        return results


def main():
    import sys

    solver = SenbeiProblemSolver()
    lines = iter(sys.stdin.read().strip().split('\n'))
    while True:
        try:
            line = next(lines)
            if not line.strip():
                continue
            R, C = map(int, line.split())
            if R == 0 and C == 0:
                break
            grid = []
            for _ in range(R):
                row = list(map(int, next(lines).split()))
                grid.append(row)
            solver.add_dataset(R, C, grid)
        except StopIteration:
            break

    results = solver.solve_all()
    print('\n'.join(str(r) for r in results))


if __name__ == "__main__":
    main()