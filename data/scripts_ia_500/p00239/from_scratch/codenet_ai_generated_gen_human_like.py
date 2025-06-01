while True:
    n = int(input())
    if n == 0:
        break
    snacks = []
    for _ in range(n):
        s, p, q, r = map(int, input().split())
        snacks.append((s, p, q, r))
    P, Q, R, C = map(int, input().split())
    result = []
    for s, p, q, r in snacks:
        cal = 4 * p + 9 * q + 4 * r
        if p <= P and q <= Q and r <= R and cal <= C:
            result.append(s)
    if result:
        for s in result:
            print(s)
    else:
        print("NA")