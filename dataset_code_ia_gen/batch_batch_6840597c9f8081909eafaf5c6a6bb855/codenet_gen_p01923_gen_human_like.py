while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    max_votes = [0] * (M + 1)
    for _ in range(N):
        d, v = map(int, input().split())
        if v > max_votes[d]:
            max_votes[d] = v
    print(sum(max_votes[1:]))