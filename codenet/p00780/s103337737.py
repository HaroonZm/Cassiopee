def f(x):
    if x == 2:
        return 1
    if x < 2 or x % 2 == 0:
        return 0
    i = 3
    while i <= x ** (1/2):
        if x % i == 0:
            return 0
        i += 2
    return 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        a = 0
        for i in range(1, n // 2 + 1):
            m = n - i
            if f(m) == 1 and f(i) == 1:
                a += 1
        print(a)