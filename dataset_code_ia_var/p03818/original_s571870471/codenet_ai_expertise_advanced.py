from itertools import groupby
from math import ceil

n = int(input())
a = sorted(map(int, input().split()))

# Trouver les doublons en utilisant groupby
duplicates = [k for k, g in groupby(a) if sum(1 for _ in g) > 1]

ans = n - 2 * ceil(len(duplicates) / 2)
print(ans)