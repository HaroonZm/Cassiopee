N, M = map(int, input().split())
A = [int(i) for i in input().split()]
l = 0
ans = 0
premiere = True
while l % N != 0 or premiere:
    premiere = False
    min_ = 101
    max_ = -1
    i = l
    while i < l + M:
        idx = i % N
        if A[idx] < min_:
            min_ = A[idx]
        if A[idx] > max_:
            max_ = A[idx]
        i += 1
    ans += max_ - min_
    l += M
print(ans)