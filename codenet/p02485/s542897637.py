while 1:
    n = input()
    sum = 0
    if n == 0:
        break
    while n > 0:
        sum += (n % 10)
        n /= 10
    print sum