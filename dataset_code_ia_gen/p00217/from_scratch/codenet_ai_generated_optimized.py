while True:
    n = int(input())
    if n == 0:
        break
    max_patient = 0
    max_distance = -1
    for _ in range(n):
        p, d1, d2 = map(int, input().split())
        total = d1 + d2
        if total > max_distance:
            max_distance = total
            max_patient = p
    print(max_patient, max_distance)