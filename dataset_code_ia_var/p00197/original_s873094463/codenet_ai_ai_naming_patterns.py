while True:
    num_first, num_second = map(int, input().split())
    if num_first == 0 and num_second == 0:
        break
    if num_first < num_second:
        num_first, num_second = num_second, num_first
    step_count = 0
    while True:
        num_first = num_first % num_second
        num_first, num_second = num_second, num_first
        step_count += 1
        if num_second == 0:
            break
    print(num_first, step_count)