N, F = map(int, input().split())
data = []
tmp = {}
for i in range(N) :
    data.append(list(input().split()))
    for x in range(1, len(data[i]) - 1) :
        for y in range(x+1, len(data[i])) :
            a = data[i][x]
            b = data[i][y]
            a, b = min(a, b), max(a, b)
            if (a, b) not in tmp :
                tmp[(a, b)] = 1
            else :
                tmp[(a, b)] += 1

ans = []
for k in tmp :
    if tmp[k] >= F :
        ans.append(list(k))

ans = sorted(ans, key = lambda x: x[1])
ans = sorted(ans)
print(len(ans))
if len(ans) != 0 :
    for i in range(len(ans)) :
        print(*ans[i])