while True:
    line = input()
    if line == '0 0':
        break
    n, m = map(int, line.split())
    taro = []
    hanako = []
    for _ in range(n):
        taro.append(int(input()))
    for _ in range(m):
        hanako.append(int(input()))
    sum_taro = sum(taro)
    sum_hanako = sum(hanako)
    found = False
    min_sum = None
    result = (-1,)
    for t in taro:
        for h in hanako:
            new_taro = sum_taro - t + h
            new_hanako = sum_hanako - h + t
            if new_taro == new_hanako:
                s = t + h
                if (not found) or (s < min_sum):
                    found = True
                    min_sum = s
                    result = (t, h)
    if found:
        print(result[0], result[1])
    else:
        print(-1)