n = int(input())
p = input().split()
for i in range(n):
    p[i] = int(p[i])
x = p[0]
ans = 1
i = 0
while i < n:
    if p[i] < x:
        x = p[i]
        ans = ans + 1
    i = i + 1
print(ans)