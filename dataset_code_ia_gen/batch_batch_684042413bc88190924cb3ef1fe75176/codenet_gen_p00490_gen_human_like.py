N = int(input())
A, B = map(int, input().split())
C = int(input())
toppings = [int(input()) for _ in range(N)]

max_cal_per_dollar = C // A  # cas sans garniture

toppings.sort(reverse=True)

total_cal = C
for i in range(N):
    total_cal += toppings[i]
    price = A + B * (i + 1)
    cal_per_dollar = total_cal // price
    if cal_per_dollar > max_cal_per_dollar:
        max_cal_per_dollar = cal_per_dollar

print(max_cal_per_dollar)