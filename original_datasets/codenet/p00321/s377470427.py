n, f = map(int, input().split())
pair = {}
for i in range(n):
    m, *items = input().split()
    m = int(m)
    for p in range(m):
        for q in range(p):
            key = tuple(sorted([items[p], items[q]]))
            pair[key] = pair.get(key, 0) + 1
ans = sorted(key for key in pair if pair[key] >= f)
print(len(ans))
if ans:
    for a, b in ans:
        print(a, b)