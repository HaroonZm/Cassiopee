while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    A = list(map(int, input().split()))
    pay = M // N
    total = 0
    for a in A:
        total += pay if a >= pay else a
    print(total)