while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    scores = [0] * (N + 1)
    poss = [set() for _ in range(M + 1)]

    for i in range(M):
        data = list(map(int, input().split()))
        S_i = data[0]
        k_i = data[1]
        c_i = data[2:]
        # For each possible contestant for problem i
        for c in c_i:
            scores[c] += S_i
        poss[i] = set(c_i)

    poss[M] = set(range(1, N+1))  # Last question everyone can answer

    maxS = max(scores)

    ans = 0
    for x in range(1, N + 1):
        # max score among others except contestant x
        max_other = max(scores[:x] + scores[x+1:])
        diff = max_other - scores[x] + 1
        if diff < 0:
            diff = 0
        ans = max(ans, diff)

    print(ans)