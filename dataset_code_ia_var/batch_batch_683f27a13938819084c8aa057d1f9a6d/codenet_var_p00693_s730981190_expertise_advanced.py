import re
from sys import stdin

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n, m = map(int, next(lines).split())
        except StopIteration:
            break
        if (n | m) == 0:
            break

        # Using list comprehensions and assignments expressions
        rule = [
            ((g := x[0]) == 'p', re.compile((x[1] + x[2]).replace('?', r'\d')))
            for x in (next(lines).split() for _ in range(n))
        ]

        ans = [
            (s, d, msg)
            for s, d, msg in (next(lines).split() for _ in range(m))
            for G, SD in reversed(rule)
            if re.match(SD, s + d)
            and (G and not break_)
            for break_ in (True,)
        ]
        print(len(ans))
        print('\n'.join(f'{a} {b} {c}' for a, b, c in ans))

if __name__ == "__main__":
    main()