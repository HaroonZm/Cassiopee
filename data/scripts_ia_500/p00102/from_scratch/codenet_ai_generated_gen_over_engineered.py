class MatrixData:
    def __init__(self, size, rows):
        self.size = size
        self.rows = rows

class MatrixProcessor:
    def __init__(self, matrix_data):
        self.matrix = matrix_data
        self.column_sums = [0] * self.matrix.size
        self.row_sums = [0] * self.matrix.size
        self.grand_total = 0

    def calculate_sums(self):
        for i in range(self.matrix.size):
            row_sum = 0
            for j in range(self.matrix.size):
                val = self.matrix.rows[i][j]
                row_sum += val
                self.column_sums[j] += val
            self.row_sums[i] = row_sum
            self.grand_total += row_sum

    def formatted_output(self):
        output_lines = []
        for i in range(self.matrix.size):
            row_strs = [f"{self.matrix.rows[i][j]:>5}" for j in range(self.matrix.size)]
            row_strs.append(f"{self.row_sums[i]:>5}")
            output_lines.append("".join(row_strs))
        col_strs = [f"{self.column_sums[j]:>5}" for j in range(self.matrix.size)]
        col_strs.append(f"{self.grand_total:>5}")
        output_lines.append("".join(col_strs))
        return output_lines

class InputHandler:
    def __init__(self):
        self.datasets = []

    def read_input(self):
        while True:
            try:
                line = input().strip()
                if line == '0':
                    break
                n = int(line)
                rows = []
                for _ in range(n):
                    row = list(map(int, input().strip().split()))
                    rows.append(row)
                self.datasets.append(MatrixData(n, rows))
            except EOFError:
                break

class SpreadsheetApp:
    def __init__(self):
        self.input_handler = InputHandler()

    def run(self):
        self.input_handler.read_input()
        for dataset in self.input_handler.datasets:
            processor = MatrixProcessor(dataset)
            processor.calculate_sums()
            for line in processor.formatted_output():
                print(line)

if __name__ == "__main__":
    app = SpreadsheetApp()
    app.run()