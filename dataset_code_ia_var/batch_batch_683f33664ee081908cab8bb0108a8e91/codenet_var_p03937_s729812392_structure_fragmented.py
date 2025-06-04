def read_dimensions():
    return tuple(int(i) for i in input().split())

def read_grid(h):
    return [input() for _ in range(h)]

def count_hashes(grid):
    return sum(row.count('#') for row in grid)

def init_queue():
    return [(0, 0)]

def is_valid_start(a):
    return a[0][0] == '#'

def print_impossible_and_exit():
    print('Impossible')
    exit()

def print_possible_and_exit():
    print('Possible')
    exit()

def get_neighbors(i, j, h, w, a):
    neighbors = []
    if i + 1 < h and a[i + 1][j] == '#':
        neighbors.append((i + 1, j))
    if j + 1 < w and a[i][j + 1] == '#':
        neighbors.append((i, j + 1))
    return neighbors

def update_queue(queue, neighbors):
    for nb in neighbors:
        if nb not in queue:
            queue.append(nb)

def update_check(check, pos):
    check.append(pos)

def check_corner_case(i, j, h, w, a):
    if i + 1 < h and j + 1 < w:
        if a[i + 1][j] == '#' and a[i][j + 1] == '#':
            return True
    return False

def is_goal(queue, h, w, a):
    return queue and queue[0] == (h - 1, w - 1) and a[h - 1][w - 1] == '#'

def correct_path_length(h, w, ct):
    return (h + w - 1) == ct

def bfs(a, h, w, ct):
    queue = init_queue()
    check = []
    while queue:
        i, j = queue[0]
        queue.pop(0)
        if (i, j) not in check:
            neighbors = get_neighbors(i, j, h, w, a)
            update_queue(queue, neighbors)
            update_check(check, (i, j))
            if check_corner_case(i, j, h, w, a):
                break
            if is_goal(queue, h, w, a):
                if correct_path_length(h, w, ct):
                    print_possible_and_exit()
    print_impossible_and_exit()

def main():
    h, w = read_dimensions()
    a = read_grid(h)
    ct = count_hashes(a)
    if not is_valid_start(a):
        print_impossible_and_exit()
    bfs(a, h, w, ct)

main()