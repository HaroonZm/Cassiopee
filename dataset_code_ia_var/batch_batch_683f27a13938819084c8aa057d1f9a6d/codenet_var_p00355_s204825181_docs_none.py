a, b = [int(i) for i in input().split()]
N = int(input())
ans = 0
for _ in range(N):
    s, f = [int(i) for i in input().split()]
    if a < f and s < b:
        ans = 1
        break
print(ans)