from sys import stdin
from collections import deque

def optimized_process():
    n, *rest = map(int, stdin.read().split())
    a_len = n
    a = rest[:a_len]
    r = rest[a_len:]

    s = deque(range(n))
    b = 0

    for i in a:
        if i % 2:
            b = (b - i) % len(s)
        else:
            b = (b + i) % len(s)
        s.rotate(-b)
        s.popleft()
        b = 0

    s_set = set(s)
    print(*(int(i in s_set) for i in r), sep='\n')

optimized_process()