from math import log

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        print(0)
        continue

    p = int(log(n, 4))
    x = n
    digits = [x // 4**(p - i) for i in range(p)]
    x %= 4**(p)
    digits.append(x)

    print(*digits, sep='')