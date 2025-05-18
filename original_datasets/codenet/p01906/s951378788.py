N, M = map(int, input().split())
A = [int(i) for i in input().split()]

l = 0
ans = 0

while l % N != 0 or l == 0:
    min_ = 101
    max_ = -1

    for i in range(l, l + M):
        min_ = min(min_, A[i % N])
        max_ = max(max_, A[i % N])

    ans += max_ - min_
    l += M

print(ans)