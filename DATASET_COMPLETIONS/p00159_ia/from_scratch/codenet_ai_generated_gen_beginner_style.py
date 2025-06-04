while True:
    n = int(input())
    if n == 0:
        break
    closest_p = None
    closest_diff = None
    for _ in range(n):
        p, h, w = map(int, input().split())
        bmi = w / ((h / 100) ** 2)
        diff = abs(bmi - 22)
        if closest_diff is None or diff < closest_diff or (diff == closest_diff and p < closest_p):
            closest_diff = diff
            closest_p = p
    print(closest_p)