while True:
    n = input().split()
    n[0] = int(n[0])
    n[1] = int(n[1])
    if n[0] == 0:
        break
    count = 0
    for i in range(n[0], n[1] + 1):
        num = i
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        if num == 1:
            count += 1
    print(count)