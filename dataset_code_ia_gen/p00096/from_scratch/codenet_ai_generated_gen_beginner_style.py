while True:
    try:
        n = int(input())
    except:
        break
    count = 0
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                d = n - a - b - c
                if 0 <= d <= 1000:
                    count += 1
    print(count)