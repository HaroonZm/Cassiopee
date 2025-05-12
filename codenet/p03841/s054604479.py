n = int(input())
x = [int(x) for i, x in enumerate(input().split())]
x = sorted(zip(x, range(1, n+1)))

stack = []
for v, i in x[::-1]:
    for _ in range(i-1):
        stack.append(i)

cur = 1
ans = []
res = []
cnt = [0]*(n+1)
for i in range(n):
    for _ in range(x[i][0]-cur):
        if stack:
            nxt = stack.pop()
        elif res:
            nxt = res.pop()
        else:
            print('No')
            exit()
        ans.append(nxt)
        cnt[nxt] += 1
    if cnt[x[i][1]] != x[i][1]-1:
        print('No')
        exit()
    ans.append(x[i][1])
    for _ in range(n-x[i][1]):
        res.append(x[i][1])
    cur = x[i][0]+1

ans += res

print('Yes')
print(*ans)