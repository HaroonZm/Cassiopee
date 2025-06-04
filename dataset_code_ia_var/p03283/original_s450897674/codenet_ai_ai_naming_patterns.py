class PrefixSum2D:
    """Constructs a two-dimensional prefix sum array"""
    def __init__(self, source_matrix):
        self.row_count = len(source_matrix)
        self.col_count = len(source_matrix[0])
        self.prefix_sum = [[0] * (self.col_count + 1) for _ in range(self.row_count + 1)]

        for row_idx in range(self.row_count):
            for col_idx in range(self.col_count):
                self.prefix_sum[row_idx + 1][col_idx + 1] = self.prefix_sum[row_idx + 1][col_idx] + source_matrix[row_idx][col_idx]
        for row_idx in range(self.row_count):
            for col_idx in range(self.col_count):
                self.prefix_sum[row_idx + 1][col_idx + 1] += self.prefix_sum[row_idx][col_idx + 1]

    def range_sum(self, top_row, bottom_row, left_col, right_col):
        """Returns the sum in the submatrix defined by [top_row, bottom_row) x [left_col, right_col)"""
        return (self.prefix_sum[bottom_row][right_col] + self.prefix_sum[top_row][left_col]
                - self.prefix_sum[bottom_row][left_col] - self.prefix_sum[top_row][right_col])

num_columns, num_entries, num_queries = map(int, input().split())
entry_list = [list(map(int, input().split())) for _ in range(num_entries)]
query_list = [list(map(int, input().split())) for _ in range(num_queries)]

base_matrix = [[0] * (num_columns + 1) for _ in range(num_columns + 1)]
for entry_left, entry_right in entry_list:
    base_matrix[entry_left][entry_right] += 1
prefix_sum_2d = PrefixSum2D(base_matrix)

for query_left, query_right in query_list:
    query_result = prefix_sum_2d.range_sum(query_left, query_right + 1, query_left, query_right + 1)
    print(query_result)