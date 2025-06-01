def read_dimensions():
    return map(int, input().split())

def read_grid(height):
    return [list(input()) for _ in range(height)]

def initialize_answer(height, width):
    return [[0] * width for _ in range(height)]

def count_c_before(column_list, index):
    return column_list[:index].count('c')

def find_distance_to_nearest_c(row, current_index):
    for offset in range(1, current_index + 1):
        if row[current_index - offset] == 'c':
            return offset
    return -1

def compute_answer(height, width, grid, answer):
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '.':
                if count_c_before(grid[i], j) == 0:
                    answer[i][j] = -1
                else:
                    answer[i][j] = find_distance_to_nearest_c(grid[i], j)

def print_answer(answer):
    for row in answer:
        print(*row)

def main():
    h, w = read_dimensions()
    c = read_grid(h)
    ans = initialize_answer(h, w)
    compute_answer(h, w, c, ans)
    print_answer(ans)

main()