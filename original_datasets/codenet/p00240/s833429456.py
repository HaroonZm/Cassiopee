while True:
    n = int(input())
    if n == 0: break  
    y = float(input())
    id, vmax = -1, 0
    for i in range(n):
        b, r, t = map(int, input().split())
        if t == 1: m = y*(r/100)+1
        else: m = (r/100+1)**y
        if id < 0 or m >= vmax: id, vmax = b, m
    print(id)