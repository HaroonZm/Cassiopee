n = int(input())
p = list(map(int, input().split()))

for i in range(n):
    p[i] -= 1

i = 0
ans = 0
while i < n:
    if p[i] == i:
        ans += 1
        i += 2
    else:
        i += 1

print(ans)