while True:
    N = int(input())
    if N == 0:
        break
    ranges = []
    for _ in range(N):
        low, high = map(int, input().split())
        cnt = high - low + 1
        ranges.append(cnt)
    ans = 1
    for c in ranges:
        ans *= c
    print(ans)