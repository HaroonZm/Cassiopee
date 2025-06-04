def read_dimensions():
    return map(int, input().split())

def read_row():
    return input()

def append_row(ms, row):
    ms.append(list(row))

def read_grid(h):
    ms = []
    for i in range(h):
        m = read_row()
        append_row(ms, m)
    return ms

def is_dot(cell):
    return cell == "."

def is_sharp(cell):
    return cell == "#"

def in_bounds(i, j, h, w):
    return 0 <= i < h and 0 <= j < w

def get_directions():
    return [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)]

def count_neighbors(ms, i, j, h, w):
    dirs = get_directions()
    count = 0
    for dx, dy in dirs:
        ni, nj = i + dx, j + dy
        if in_bounds(ni, nj, h, w):
            if is_sharp(ms[ni][nj]):
                count += 1
    return count

def process_cell(ms, i, j, h, w):
    if is_dot(ms[i][j]):
        count = count_neighbors(ms, i, j, h, w)
        ms[i][j] = str(count)

def process_grid(ms, h, w):
    for i in range(h):
        for j in range(w):
            process_cell(ms, i, j, h, w)

def join_row(row, w):
    return "".join([row[j] for j in range(w)])

def print_grid(ms, h, w):
    for i in range(h):
        temp = join_row(ms[i], w)
        print(temp)

def main():
    h, w = read_dimensions()
    ms = read_grid(h)
    process_grid(ms, h, w)
    print_grid(ms, h, w)

main()