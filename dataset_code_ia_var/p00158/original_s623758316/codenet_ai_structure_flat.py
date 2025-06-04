while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    x = n
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
        count += 1
    print(count)