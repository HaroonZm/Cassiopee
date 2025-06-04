import sys
from itertools import accumulate, repeat, islice, starmap, count
from functools import reduce, partial, lru_cache
from operator import eq

input = sys.stdin.readline

def solve():
    S, T = map(lambda s: s.rstrip(), (input(), input()))
    q = int(input())    

    to_bool = lambda c: 1 if c == 'A' else 0

    acs = [0] + list(accumulate(map(to_bool, S)))
    act = [0] + list(accumulate(map(to_bool, T)))

    identity = lambda *args: args
    get_query = lambda: tuple(map(int, input().split()))

    get_modulo = lambda acc, a, b: (acc[b] - acc[a-1] + b - a + 1) % 3

    printer = lambda x: print('YES' if x else 'NO')
    
    for _ in map(identity, range(q)):
        a, b, c, d = get_query()
        s_mod, t_mod = map(lambda t: get_modulo(t[0], t[1], t[2]), ((acs, a, b), (act, c, d)))
        printer(s_mod == t_mod)
    
solve()