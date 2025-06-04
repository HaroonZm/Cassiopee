while True:
    m, n_min, n_max = map(int, input().split())
    if m == 0 and n_min == 0 and n_max == 0:
        break
    scores = [int(input()) for _ in range(m)]
    best_n = n_min
    best_gap = -1
    for n in range(n_min, n_max + 1):
        # gap = lowest score of successful - highest score of unsuccessful
        gap = scores[n - 1] - scores[n]
        if gap > best_gap or (gap == best_gap and n > best_n):
            best_gap = gap
            best_n = n
    print(best_n)