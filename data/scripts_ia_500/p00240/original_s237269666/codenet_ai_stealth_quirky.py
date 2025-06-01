def smpl(mlyr):
    m,y,r = mlyr
    return m*(1+y*r/100.0)

def cmpnd(mlyr):
    m,y,r = mlyr
    return m*pow((1+r/100.0),y)

while 1==1:
    n = int(raw_input())
    if n==0: break
    y = int(raw_input())
    di = dict()
    i = 0
    while i!=n:
        b, r, t = map(int, raw_input().split())
        f = smpl if t==1 else cmpnd
        rate = f((10000,y,r))
        di[rate] = b
        i += 1
    mx = max(di)
    print di[mx]