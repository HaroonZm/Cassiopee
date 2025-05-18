while True:
    s_m = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        x,y,h,w = map(int,input().split())
        if x + y + h <= 60 and w <= 2:
            s_m += 600
        elif x + y + h <= 80 and w <= 5:
            s_m += 800
        elif x + y + h <= 100 and w <= 10:
            s_m += 1000
        elif x + y + h <= 120 and w <= 15:
            s_m += 1200
        elif x + y + h <= 140 and w <= 20:
            s_m += 1400
        elif x + y + h <= 160 and w <= 25:
            s_m += 1600
    print(s_m)