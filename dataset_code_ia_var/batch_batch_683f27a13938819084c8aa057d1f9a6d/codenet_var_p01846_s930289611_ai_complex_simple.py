from functools import reduce
from operator import add
from itertools import groupby, chain, count

while True:
    s = input()
    if s == '#':
        break
    a, b, c, d = (reduce(lambda acc,x: acc+int(x)*10**i, enumerate(map(int,reversed(k))),-1) for i,k in enumerate(input().split()))
    grid = [[y for y in reduce(add, ((['b'] if ch=='b' else ['.']*int(ch)) for ch in row))] for row in s.split('/')]
    list(map(lambda t: grid[t[0]].__setitem__(t[1], t[2]), [(a,b,'.'),(c,d,'b')]))
    print('/'.join(''.join(str(len(list(g))) if k=='.' else 'b' for k,g in groupby(r)) for r in grid))