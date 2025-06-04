while True:
    line = input()
    if line == '0 0 0':
        break
    m, n_min, n_max = map(int, line.split())
    scores = []
    for _ in range(m):
        scores.append(int(input()))
    max_gap = -1
    answer = n_min
    for n in range(n_min, n_max + 1):
        gap = scores[n - 1] - scores[n]
        if gap > max_gap:
            max_gap = gap
            answer = n
        elif gap == max_gap and n > answer:
            answer = n
    print(answer)