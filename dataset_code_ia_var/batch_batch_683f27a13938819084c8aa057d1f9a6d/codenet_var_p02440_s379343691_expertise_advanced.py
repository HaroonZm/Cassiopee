from sys import stdin
from itertools import islice
from operator import itemgetter

def solve():
    input_lines = map(str.strip, stdin)
    n = int(next(input_lines))
    A = tuple(map(int, next(input_lines).split()))
    q = int(next(input_lines))
    queries = (tuple(map(int, line.split())) for line in islice(input_lines, q))
    funcs = (min, max)
    results = (
        str(funcs[com](A[b:e]))
        for com, b, e in queries
    )
    print(*results, sep='\n')

solve()