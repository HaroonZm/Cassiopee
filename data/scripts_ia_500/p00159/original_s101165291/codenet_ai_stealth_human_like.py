while True:
    n = int(input())
    if n == 0:
        break
    closest_diff = None  # keep track of smallest diff from 22
    answer = 0
    for _ in range(n):
        idx, height, weight = map(int, input().split())
        bmi = weight / ((height / 100.0) ** 2)
        diff = abs(22 - bmi)
        # first iteration or found closer bmi
        if closest_diff is None or diff < closest_diff:
            closest_diff = diff
            answer = idx
    print(answer)