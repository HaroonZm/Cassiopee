class CheckeredPatternSolver:
    class Matrix:
        def __init__(self, rows, cols, data):
            self.rows = rows
            self.cols = cols
            self.data = data

        def get_row(self, r):
            return self.data[r]

        def get_column(self, c):
            return [self.data[r][c] for r in range(self.rows)]

        def check_pattern_feasibility(self):
            # We want to check whether rows and columns can be rearranged 
            # so that the pattern is checkered. After any swapping of rows 
            # and columns, the relative pattern between rows and columns must be consistent.
            # So, we need to check if rows can be grouped into two types alternating 
            # and same for columns.

            # Consider first row pattern:
            pattern0 = self.get_row(0)
            inv_pattern0 = [1 - x for x in pattern0]
            
            # Check each row must be either pattern0 or inverse of pattern0
            for r in range(1, self.rows):
                row = self.get_row(r)
                if row != pattern0 and row != inv_pattern0:
                    return False

            # Similarly for columns:
            first_col = self.get_column(0)
            inv_first_col = [1 - x for x in first_col]

            for c in range(1, self.cols):
                col = self.get_column(c)
                if col != first_col and col != inv_first_col:
                    return False

            # Finally check that patterns are crossing consistently:
            # pattern0[0] should equal first_col[0], else impossible
            if pattern0[0] != first_col[0]:
                return False

            return True

    class InputParser:
        @staticmethod
        def parse():
            import sys
            W, H = map(int, sys.stdin.readline().strip().split())
            data = []
            for _ in range(H):
                row = list(map(int, sys.stdin.readline().strip().split()))
                data.append(row)
            return W, H, data

    class OutputWriter:
        @staticmethod
        def write(result):
            print("yes" if result else "no")

    def __init__(self):
        self.W = 0
        self.H = 0
        self.matrix = None

    def load_input(self):
        self.W, self.H, data = self.InputParser.parse()
        self.matrix = self.Matrix(self.H, self.W, data)

    def solve(self):
        return self.matrix.check_pattern_feasibility()

    def run(self):
        self.load_input()
        result = self.solve()
        self.OutputWriter.write(result)

if __name__ == "__main__":
    solver = CheckeredPatternSolver()
    solver.run()