from collections import deque

def read_ints():
    return [int(i) for i in input().split()]

def read_tower():
    tower = read_ints()
    _, *disks = tower
    disks.insert(0, 0)
    return disks

def create_target(n):
    return [i for i in range(0, n+1)]

def should_move_disk(source, target, last_move_type, forbidden_move_type):
    return source[-1] > target[-1] and last_move_type != forbidden_move_type

def move_disk(source, target):
    return source[:-1], target + [source[-1]]

def append_state(queue, a, b, c, d, t):
    queue.appendleft([a, b, c, d, t])

def is_solved(a, c, target):
    return a == target or c == target

def process_state(queue, max_moves, target):
    while queue:
        a, b, c, d, t = queue.pop()
        if d > max_moves:
            print(-1)
            return True
        if is_solved(a, c, target):
            print(d)
            return True
        if should_move_disk(a, b, t, 1):
            na, nb = move_disk(a, b)
            append_state(queue, na, nb, c[:], d+1, 0)
        if should_move_disk(b, a, t, 0):
            na, nb = move_disk(b, a)
            append_state(queue, nb, na, c[:], d+1, 1)
        if should_move_disk(b, c, t, 3):
            nb, nc = move_disk(b, c)
            append_state(queue, a[:], nb, nc, d+1, 2)
        if should_move_disk(c, b, t, 2):
            nc, nb = move_disk(c, b)
            append_state(queue, a[:], nb, nc, d+1, 3)
    return False

def prepare_queue(a, b, c):
    q = deque()
    append_state(q, a, b, c, 0, -1)
    return q

def main():
    while True:
        n, m = read_ints()
        if n == 0 and m == 0:
            return
        a = read_tower()
        b = read_tower()
        c = read_tower()
        target = create_target(n)
        q = prepare_queue(a, b, c)
        if process_state(q, m, target):
            continue

if __name__ == '__main__':
    main()