N, F = map(int, input().split())
data = [input().split() for _ in range(N)]

tmp = dict()
for row in data:
    j = 1
    while j < len(row) - 1:
        k = j + 1
        while k < len(row):
            a, b = row[j], row[k]
            if a > b:
                a, b = b, a
            if (a, b) in tmp:
                tmp[(a, b)] += 1
            else:
                tmp[(a, b)] = 1
            k += 1
        j += 1

ans = []
for pair, count in tmp.items():
    if count >= F:
        ans.append(pair)

ans.sort(key=lambda x: x[1])
ans.sort()

print(len(ans))
if ans:
    for item in ans:
        print(*item)