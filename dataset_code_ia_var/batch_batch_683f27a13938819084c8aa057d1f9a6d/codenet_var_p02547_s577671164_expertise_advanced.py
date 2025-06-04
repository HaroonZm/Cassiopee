from itertools import islice, groupby, starmap

n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
consec_equal = (k for k, g in groupby(starmap(lambda x, y: x == y, pairs)) if k)
found = any(len(list(islice(g, 3))) == 3 for g in groupby(starmap(lambda x, y: x == y, pairs)) if k for k, g in [(k, g)])

print("Yes" if found else "No")