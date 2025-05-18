n = int(input())
s = 0
for i in range(n):
    a, b = map(int, input().split())
    s += 1 << (a+b)
i = 0
ans = []
while s:
    if s & 1:
        ans.append(i)
    s >>= 1
    i += 1
for e in ans:
    print(e, 0)