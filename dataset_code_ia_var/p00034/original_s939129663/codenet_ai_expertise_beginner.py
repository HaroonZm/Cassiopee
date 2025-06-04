while True:
    try:
        s = input()
        values = s.split(',')
        numbers = []
        for item in values:
            numbers.append(int(item))
    except:
        break
    total_distance = 0
    for i in range(10):
        total_distance += numbers[i]
    speed1 = numbers[10]
    speed2 = numbers[11]
    sum_time = 0
    meters = 0
    for i in range(10):
        time = numbers[i] / speed1
        meters += time * speed2
        temp_sum = 0
        for j in range(i+1):
            temp_sum += numbers[j]
        if meters + temp_sum >= total_distance:
            print(i+1)
            break