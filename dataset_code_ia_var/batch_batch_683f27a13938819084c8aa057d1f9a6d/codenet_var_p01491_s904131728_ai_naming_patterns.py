import sys
input_stream = sys.stdin.readline
output_stream = sys.stdout.write

def process_problem():
    rows_cnt, cols_cnt, rows_seed, rows_delta, cols_seed, cols_delta = map(int, input_stream().split())

    rows_sum = [0] * (rows_cnt + 1)
    current_row = rows_seed
    rows_sum[0] = current_row
    for row_idx in range(1, rows_cnt):
        current_row = (current_row * 58 + rows_delta) % (cols_cnt + 1)
        rows_sum[row_idx] = current_row
    rows_sum.sort()
    for row_idx in range(rows_cnt):
        rows_sum[row_idx + 1] += rows_sum[row_idx]

    cols_sum = [0] * (cols_cnt + 1)
    current_col = cols_seed
    cols_sum[0] = current_col
    for col_idx in range(1, cols_cnt):
        current_col = (current_col * 58 + cols_delta) % (rows_cnt + 1)
        cols_sum[col_idx] = current_col
    cols_sum.sort()
    for col_idx in range(cols_cnt):
        cols_sum[col_idx + 1] += cols_sum[col_idx]

    def generate_candidates():
        def evaluate(row_partition, col_partition):
            return (rows_cnt - row_partition) * (cols_cnt - col_partition) + rows_sum[row_partition] + cols_sum[col_partition]
        yield 10 ** 18
        col_itr = cols_cnt
        for row_itr in range(rows_cnt + 1):
            while col_itr > 0 and evaluate(row_itr, col_itr) > evaluate(row_itr, col_itr - 1):
                col_itr -= 1
            yield evaluate(row_itr, col_itr)
    output_stream("%d\n" % min(generate_candidates()))

process_problem()