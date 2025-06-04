value_main, value_bonus, value_target = map(int, input().split())
accumulator_total = 0
counter_day = 0
while True:
    accumulator_total += value_main
    counter_day += 1
    if accumulator_total >= value_target:
        print(counter_day)
        break
    if counter_day % 7 == 0:
        accumulator_total += value_bonus
        if accumulator_total >= value_target:
            print(counter_day)
            break