while True:
    n = int(input())
    if n == 0:
        break
    max_dist = -1
    max_patient = -1
    for _ in range(n):
        p, d1, d2 = map(int, input().split())
        total = d1 + d2
        if total > max_dist:
            max_dist = total
            max_patient = p
    print(max_patient, max_dist)