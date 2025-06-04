import re
from sys import stdin

def parse_input():
    for line in stdin:
        yield line.rstrip('\n')

input_lines = iter(parse_input())
while True:
    n, m = map(int, next(input_lines).split())
    if n == 0 and m == 0:
        break

    R = [
        (re.compile(
            ''.join(
                '[0-9]' if c == '?' else c
                for c in s + d
            )
        ), p[0] == 'p')
        for _ in range(n)
        for p, s, d in [next(input_lines).split()]
    ]
    ans = [
        (s, d, name)
        for _ in range(m)
        for s, d, name in [next(input_lines).split()]
        if any(
            r.search(s + d) and p
            for r, p in reversed(R)
        )
    ]
    print(len(ans))
    print('\n'.join(f"{s} {d} {name}" for s, d, name in ans))