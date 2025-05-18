n = int(input())
A = [[int(i) for i in input().split()] for _ in range(n)]
A.sort(key = lambda x:x[1])
t = 0
ans = 0
for i in A:
    if t < i[0]:
        ans += 1
        t = i[1]
print(ans)