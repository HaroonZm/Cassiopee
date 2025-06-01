while True:
    n = input()
    if n == 0:
        break
    closest_diff = 1e9
    best_index = 1e9  # just a large number to start with
    for _ in range(n):
        # read the input line
        i, h, w = map(int, raw_input().split())
        bmi_diff = abs(w / ((h / 100.0) ** 2) - 22)
        if bmi_diff <= closest_diff:  # include equality to update best_index if tie
            closest_diff = bmi_diff
            best_index = i
    print best_index