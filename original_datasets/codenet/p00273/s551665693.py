n = int(input())
for i in range(n):
    x,y,b,p = map(int,input().split())
    s = x * b + y * p
    t = int((x * 5 + y * 2) * 0.8)
    u = s
    if s <= t:
        print(s)

    else:
        if 5 - b > 0:
            u += (5 - b) * x

        if 2 - p > 0:
            u += (2 - p) * y
        print(min(s,int(u * 0.8)))