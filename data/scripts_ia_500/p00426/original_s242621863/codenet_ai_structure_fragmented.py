from collections import deque

def read_ints():
    return [int(i) for i in input().split()]

def read_and_prepare_list():
    _, *lst = read_ints()
    lst.insert(0, 0)
    return lst

def is_finished_state(lst, target):
    return lst == target

def can_move(from_stack, to_stack, last_move, forbidden1, forbidden2):
    return from_stack[-1] > to_stack[-1] and last_move != forbidden1 and last_move != forbidden2

def move_a_to_b(a, b, c, d, t):
    return [a[:-1], b + [a[-1]], c[:], d + 1, 0]

def move_b_to_a(a, b, c, d, t):
    return [a + [b[-1]], b[:-1], c[:], d + 1, 1]

def move_b_to_c(a, b, c, d, t):
    return [a[:], b[:-1], c + [b[-1]], d + 1, 2]

def move_c_to_b(a, b, c, d, t):
    return [a[:], b + [c[-1]], c[:-1], d + 1, 3]

def process_state(q, tmp, m):
    while q:
        a, b, c, d, t = q.pop()
        if d > m:
            print(-1)
            return True
        if is_finished_state(a, tmp) or is_finished_state(c, tmp):
            print(d)
            return True
        if can_move(a, b, t, 1, 0):
            q.appendleft(move_a_to_b(a, b, c, d, t))
        if can_move(b, a, t, 0, 1):
            q.appendleft(move_b_to_a(a, b, c, d, t))
        if can_move(b, c, t, 3, 2):
            q.appendleft(move_b_to_c(a, b, c, d, t))
        if can_move(c, b, t, 2, 3):
            q.appendleft(move_c_to_b(a, b, c, d, t))
    return False

def main():
    while True:
        n, m = read_ints()
        if n == 0 and m == 0:
            return
        a = read_and_prepare_list()
        b = read_and_prepare_list()
        c = read_and_prepare_list()
        q = deque()
        q.appendleft([a, b, c, 0, -1])
        tmp = [i for i in range(0, n + 1)]
        finished = process_state(q, tmp, m)
        if not finished:
            print(-1)

if __name__ == '__main__':
    main()