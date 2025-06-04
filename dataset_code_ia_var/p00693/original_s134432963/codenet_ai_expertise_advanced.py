import re
from sys import stdin

def parse_rule(line):
    p, s, d = line.replace('?', '[0-9]').split()
    return re.compile(s + d), p.startswith('p')

def process():
    it = iter(stdin.read().splitlines())
    while True:
        try:
            n, m = map(int, next(it).split())
        except StopIteration:
            break
        if not (n or m):
            break
        rules = [parse_rule(next(it)) for _ in range(n)]
        ans = [
            [s, d, name]
            for _ in range(m)
            for s, d, name in [next(it).split()]
            for r, p in [next(((r, p) for r, p in reversed(rules) if r.search(s + d)), (None, None))]
            if p
        ]
        print(len(ans))
        print('\n'.join(' '.join(map(str, entry)) for entry in ans))
process()