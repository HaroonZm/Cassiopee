while True:
    a = b = 0
    n = int(input())
    if n == 0:
            break
    for i in range(n):        
        c, d = map(int, input().split())
        if c > d:
            a+=c+d
        elif c < d:
            b+=c+d
        else:
            a+=c
            b+=d
    print(a, b)