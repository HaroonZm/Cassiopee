deposit_amount, bonus_amount, goal_amount = map(int, input().split())
current_total = 0
current_day = 1
while True:
    current_total += deposit_amount
    if current_day % 7 == 0:
        current_total += bonus_amount
    if current_total >= goal_amount:
        break
    current_day += 1
print(current_day)