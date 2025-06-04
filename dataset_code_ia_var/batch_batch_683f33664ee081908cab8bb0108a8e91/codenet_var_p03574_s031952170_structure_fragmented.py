def get_input_dimensions():
    return map(int, input().split())

def get_grid_rows(high):
    return [list(input()) for _ in range(high)]

def create_empty_grid(high, width):
    return [[0 for _ in range(width)] for _ in range(high)]

def get_directions():
    return [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]

def is_mine(cell):
    return cell == '#'

def mark_mine(tmp_list, h, w):
    tmp_list[h][w] = '#'

def is_in_bounds(h, w, high, width):
    return 0 <= h < high and 0 <= w < width

def is_empty_cell(cell):
    return cell == '.'

def increment_cell(tmp_list, h, w):
    if isinstance(tmp_list[h][w], int):
        tmp_list[h][w] += 1

def handle_neighbors(s_list, tmp_list, h, w, high, width, directions):
    for dx, dy in directions:
        nh = h + dx
        nw = w + dy
        if is_in_bounds(nh, nw, high, width):
            if is_empty_cell(s_list[nh][nw]):
                increment_cell(tmp_list, nh, nw)

def process_grid(s_list, tmp_list, high, width, directions):
    for h in range(high):
        for w in range(width):
            if is_mine(s_list[h][w]):
                mark_mine(tmp_list, h, w)
                handle_neighbors(s_list, tmp_list, h, w, high, width, directions)

def row_to_str(row):
    return ''.join(map(str, row))

def print_grid(tmp_list):
    for row in tmp_list:
        print(row_to_str(row))

def main():
    high, width = get_input_dimensions()
    s_list = get_grid_rows(high)
    tmp_list = create_empty_grid(high, width)
    directions = get_directions()
    process_grid(s_list, tmp_list, high, width, directions)
    print_grid(tmp_list)

main()