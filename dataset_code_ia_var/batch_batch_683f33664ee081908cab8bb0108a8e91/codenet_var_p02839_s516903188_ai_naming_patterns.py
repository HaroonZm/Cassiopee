import sys

def proc_main():
    stdin_input = sys.stdin.readline
    grid_height, grid_width = map(int, stdin_input().split())
    mat_a = [list(map(int, stdin_input().split())) for _ in range(grid_height)]
    mat_b = [list(map(int, stdin_input().split())) for _ in range(grid_height)]
    diff_offset = 80 * 164
    dp_table = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
    initial_diff = mat_a[0][0] - mat_b[0][0]
    dp_table[0][0] |= 1 << (initial_diff + diff_offset)
    dp_table[0][0] |= 1 << (-initial_diff + diff_offset)
    for row_idx in range(grid_height):
        for col_idx in range(grid_width):
            if row_idx + 1 < grid_height:
                abs_diff_down = abs(mat_a[row_idx + 1][col_idx] - mat_b[row_idx + 1][col_idx])
                dp_table[row_idx + 1][col_idx] |= (dp_table[row_idx][col_idx] << abs_diff_down)
                dp_table[row_idx + 1][col_idx] |= (dp_table[row_idx][col_idx] >> abs_diff_down)
            if col_idx + 1 < grid_width:
                abs_diff_right = abs(mat_a[row_idx][col_idx + 1] - mat_b[row_idx][col_idx + 1])
                dp_table[row_idx][col_idx + 1] |= (dp_table[row_idx][col_idx] << abs_diff_right)
                dp_table[row_idx][col_idx + 1] |= (dp_table[row_idx][col_idx] >> abs_diff_right)
    min_result = 10 ** 10
    for diff_idx in range(diff_offset, 80 * 330):
        if (dp_table[grid_height - 1][grid_width - 1] >> diff_idx) & 1:
            min_result = diff_idx - diff_offset
            break
    for diff_idx in reversed(range(diff_offset)):
        if (dp_table[grid_height - 1][grid_width - 1] >> diff_idx) & 1:
            min_result = min(min_result, diff_offset - diff_idx)
            break
    print(min_result)

if __name__ == '__main__':
    proc_main()