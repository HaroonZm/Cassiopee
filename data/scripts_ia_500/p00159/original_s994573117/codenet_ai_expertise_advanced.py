while True:
    n = int(input())
    if n == 0:
        break
    a, b = float('inf'), None
    for _ in range(n):
        i, h, w = map(int, input().split())
        bmi_diff = abs(w / (h / 100) ** 2 - 22)
        if bmi_diff <= a:
            a, b = bmi_diff, i
    print(b)