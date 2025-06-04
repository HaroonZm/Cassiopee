class Matrix:
    def __init__(self, n, data):
        if len(data) != n or any(len(row) != n for row in data):
            raise ValueError("Data dimensions do not match n x n.")
        self.n = n
        self.data = data

    def submatrix_sum(self, r1, r2, c1, c2):
        # Sum of elements in the submatrix from rows r1 to r2 and columns c1 to c2 inclusive
        total = 0
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                total += self.data[r][c]
        return total


class KadaneResult:
    def __init__(self, max_sum, start_index, end_index):
        self.max_sum = max_sum
        self.start_index = start_index
        self.end_index = end_index


class Kadane:
    @staticmethod
    def run(arr):
        max_current = max_global = arr[0]
        start = end = s = 0

        for i in range(1, len(arr)):
            if arr[i] > max_current + arr[i]:
                max_current = arr[i]
                s = i
            else:
                max_current += arr[i]

            if max_current > max_global:
                max_global = max_current
                start = s
                end = i

        return KadaneResult(max_global, start, end)


class MaxSubmatrixSumFinder:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_max_sum(self):
        n = self.matrix.n
        max_sum = -float('inf')

        # Iterate over left column
        for left in range(n):
            # Temporary array for row sums
            temp_row_sum = [0] * n

            # Iterate over right column >= left
            for right in range(left, n):
                for row in range(n):
                    temp_row_sum[row] += self.matrix.data[row][right]

                # Use Kadane's algorithm on temp_row_sum to find max subarray sum
                kadane_res = Kadane.run(temp_row_sum)
                if kadane_res.max_sum > max_sum:
                    max_sum = kadane_res.max_sum
        return max_sum


class InputReader:
    @staticmethod
    def read():
        import sys
        lines = sys.stdin.read().strip().split('\n')
        n = int(lines[0])
        data = []
        for i in range(1, n+1):
            row = list(map(int, lines[i].strip().split()))
            data.append(row)
        return n, data


class MaxSumSequenceII:
    def __init__(self):
        self.n = None
        self.matrix = None
        self.finder = None

    def execute(self):
        self.n, data = InputReader.read()
        self.matrix = Matrix(self.n, data)
        self.finder = MaxSubmatrixSumFinder(self.matrix)
        answer = self.finder.find_max_sum()
        print(answer)


if __name__ == "__main__":
    program = MaxSumSequenceII()
    program.execute()