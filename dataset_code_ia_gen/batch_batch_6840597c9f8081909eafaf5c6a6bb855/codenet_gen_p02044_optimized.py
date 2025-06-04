while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    A = list(map(int, input().split()))
    per_person = M // N
    total = 0
    for money in A:
        total += money if money < per_person else per_person
    print(total)