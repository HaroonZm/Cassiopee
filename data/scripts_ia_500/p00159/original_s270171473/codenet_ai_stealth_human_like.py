while True:
    n = int(input())  # number of entries
    if n == 0:  # zero means stop
        break
    ans = 0
    min_diff = 1 << 10  # just a large number, kinda arbitrary
    for _ in range(n):
        p, h, w = map(int, input().split())  # price, height in cm, weight in kg
        bmi = w / ((h/100)**2)  # BMI calculation
        diff = abs(bmi - 22)  # difference from ideal BMI of 22
        if diff < min_diff:
            min_diff = diff
            ans = p
    print(ans)