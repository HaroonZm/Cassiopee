N = int(input())
a = list(map(int, input().split()))

tmp = [0] * (N+1)
ans = 0

for i in a:
    if i > N:
        ans += 1
    else:
        tmp[i] += 1

for i in range(N+1):
    if i > tmp[i]:
        ans += tmp[i]
    elif i < tmp[i]:
        ans += tmp[i] - i

print(ans)