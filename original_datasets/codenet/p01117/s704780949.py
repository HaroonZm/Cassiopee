while True:
    n, m = map(int,raw_input().split(' '))
    if n == 0:
        break
    scores = [0] * n
    for i in range(m):
        j = 0
        for s in map(int,raw_input().split(' ')):
            scores[j] += s
            j += 1
    print max(scores)