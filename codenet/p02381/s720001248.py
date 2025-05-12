while 1:
    n = int(input())
    if n == 0: break
    s = [int(x) for x in input().split()]
    m = sum(s) / len(s)
    tmp = 0
    for _ in s:
        tmp += (_ - m) ** 2
    alpha = (tmp / len(s)) ** 0.5
    print(format(alpha,  '.6f'))