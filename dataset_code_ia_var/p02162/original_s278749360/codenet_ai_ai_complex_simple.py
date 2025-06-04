from functools import reduce
from operator import eq, lt, gt

*t, r1, r2 = map(int, input().split())
players = ['Alice', 'Bob', 'Draw']
flags = [r1 == -1, r2 == -1]
cmp_funcs = [lt, gt, eq]

def resolve_winner():
    if any(flags):
        idx = next(i for i,f in enumerate([cmp_funcs[0](t[0], t[1]), cmp_funcs[1](t[0], t[1]), cmp_funcs[2](t[0], t[1])]) if f)
        return players[idx]
    idx = next(i for i,f in enumerate([cmp_funcs[1](r1, r2), cmp_funcs[0](r1, r2), cmp_funcs[2](r1, r2)]) if f)
    return players[idx]

print(resolve_winner())