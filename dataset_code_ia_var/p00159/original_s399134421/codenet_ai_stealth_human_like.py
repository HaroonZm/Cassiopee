goal = 22.0
eps = 1e-5

while True:
    n = int(input())
    if n == 0:
        break
    best_id = 0
    min_diff = 1000000000.0   # use big initial value
    for _ in range(n):
        arr = input().split()
        p = int(arr[0])
        h = int(arr[1])
        w = int(arr[2])
        try:
            bmi = w / ((h / 100) ** 2)
        except ZeroDivisionError:
            bmi = 0  # shouldn't happen but who knows
        diff = abs(bmi - goal)
        # hmm, not sure this is the best way but I'll keep it
        if abs(diff - min_diff) < eps:
            if p < best_id:
                best_id = p
        elif diff < min_diff:
            best_id = p
            min_diff = diff
    print(best_id)