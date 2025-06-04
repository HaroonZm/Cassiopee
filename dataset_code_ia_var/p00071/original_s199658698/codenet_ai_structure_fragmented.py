def read_int():
    return int(input())

def skip_line():
    input()

def read_row():
    return [int(i) for i in list(input())]

def read_table(n_rows):
    table = []
    for _ in range(n_rows):
        table.append(read_row())
    return table

def print_row(row):
    for val in row:
        print("{0:d}".format(val), end="")
    print("")

def print_table(t):
    for row in t:
        print_row(row)

def get_neighbors(x, y, size, i):
    positions = []
    if x + i < size:
        positions.append((x + i, y))
    if x - i >= 0:
        positions.append((x - i, y))
    if y + i < size:
        positions.append((x, y + i))
    if y - i >= 0:
        positions.append((x, y - i))
    return positions

def should_add_to_queue(t, pos):
    x, y = pos
    return t[y][x] == 1

def mark_zero(t, pos):
    x, y = pos
    t[y][x] = 0

def process_neighbors(t, x, y, q, size):
    for i in range(1, 4):
        positions = get_neighbors(x, y, size, i)
        for pos in positions:
            if should_add_to_queue(t, pos):
                q.append([pos[0], pos[1]])
                mark_zero(t, pos)

def play_step(t, q, size):
    p = q.pop(0)
    x, y = p[0], p[1]
    mark_zero(t, (x, y))
    process_neighbors(t, x, y, q, size)

def play(t, x, y):
    size = len(t)
    q = [[x, y]]
    while q:
        play_step(t, q, size)
    return t

def main():
    n = read_int()
    for i in range(1, n + 1):
        skip_line()  # skip
        t = []
        t.append(read_row())
        for _ in range(7):
            t.append(read_row())
        x = read_int()
        y = read_int()
        tt = play(t, x - 1, y - 1)
        print('Data {0:d}:'.format(i))
        print_table(tt)

main()