from itertools import combinations

n, k = map(int, input().split())
comb_list = []
for c in combinations(range(n), k):
    bitmask = sum(1 << b for b in c)
    elements = ' '.join(map(str, c))
    comb_list.append((bitmask, elements))
for bitmask, elements in sorted(comb_list):
    print(f'{bitmask}: {elements}')