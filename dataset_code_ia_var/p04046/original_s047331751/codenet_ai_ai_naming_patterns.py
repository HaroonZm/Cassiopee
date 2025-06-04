class FactorialData:
    def __init__(self):
        self.factorial = 1
        self.inv_factorial = 1

class FactorialCombinatorics:
    def __init__(self, max_n, modulo):
        self.factorials = [FactorialData() for _ in range(max_n + 1)]
        self.modulo = modulo
        for idx in range(2, max_n + 1):
            self.factorials[idx].factorial = (self.factorials[idx - 1].factorial * idx) % self.modulo
        self.factorials[max_n].inv_factorial = pow(self.factorials[max_n].factorial, self.modulo - 2, self.modulo)
        for idx in range(max_n, 0, -1):
            self.factorials[idx - 1].inv_factorial = (self.factorials[idx].inv_factorial * idx) % self.modulo

    def compute_combination(self, n, k):
        if n < k:
            return 0
        return (self.factorials[n].factorial * self.factorials[n - k].inv_factorial * self.factorials[k].inv_factorial) % self.modulo

grid_height, grid_width, blocked_row, blocked_col = map(int, input().split())
result_total = 0
modulo_const = 10**9 + 7
combinatorics = FactorialCombinatorics(grid_width + grid_height + 2, modulo_const)
for path_row in range(grid_height - blocked_row):
    left_paths = combinatorics.compute_combination(blocked_col + path_row - 1, path_row)
    right_paths = combinatorics.compute_combination(grid_width + grid_height - 2 - blocked_col - path_row, grid_height - 1 - path_row)
    result_total = (result_total + left_paths * right_paths) % modulo_const
print(result_total)