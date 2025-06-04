import math
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(0)
    else:
        p = int(math.log(n,4))
        l = [None for _ in range(p)]
        x = n
        for i in range(p):
            l[i] = x // (4 ** (p - i))
            x = x % (4 ** (p - i))
        l.append(x)
        print(*l, sep="")