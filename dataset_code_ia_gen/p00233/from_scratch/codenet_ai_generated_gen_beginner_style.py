while True:
    n = int(input())
    if n == 0:
        break

    if n == 0:
        print(0)
        continue

    result = ""
    num = n
    while num != 0:
        r = num % -10
        num = num // -10
        if r < 0:
            r += 10
            num += 1
        result = str(r) + result

    print(result)