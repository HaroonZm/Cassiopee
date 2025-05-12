"""
Bitset II - Enumeration of Combinations
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_11_D&lang=jp

"""
from itertools import combinations

n, k = map(int, input().split())
for n, combi in sorted([(sum([1<<b for b in c]), ' '.join(map(str, c)))  for c in combinations(range(n), k)]):
    print(f'{n}: {combi}')