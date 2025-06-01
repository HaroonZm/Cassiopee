import math

while True:
    try:
        m, n = map(int, input().split())
        f2 = int(math.log(n, 2)) + 1
        f3 = int(math.log(n, 3)) + 1
        f5 = int(math.log(n, 5)) + 1
        c = 0
        for i in range(f2):
            for j in range(f3):
                for k in range(f5):
                    if m <= (2 ** i) * (3 ** j) * (5 ** k) <= n:
                        c += 1
        print(c)
    except ValueError:
        break