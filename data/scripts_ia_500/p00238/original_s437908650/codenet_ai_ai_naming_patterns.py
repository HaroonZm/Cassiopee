while True:
    total_value = int(input())
    if total_value == 0:
        break
    interval_count = int(input())
    total_subtract = 0
    for _ in range(interval_count):
        interval_values = list(map(int, input().split()))
        interval_difference = interval_values[1] - interval_values[0]
        total_subtract += interval_difference
    if total_value > total_subtract:
        print(total_value - total_subtract)
    else:
        print('OK')