n, m = map(int, input().split())
hs = list(map(int, input().split()))

ans = []
for i in range(n):
    ans.append(1)

for i in range(m):
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    if hs[a] < hs[b]:
        ans[a] = 0
    elif hs[a] == hs[b]:
        ans[a] = 0
        ans[b] = 0
    else:
        ans[b] = 0

result = 0
for num in ans:
    result = result + num
print(result)