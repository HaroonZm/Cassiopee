def smpl(m,y,r):
    return m*(1+y*r/100.0)

def cmpnd(m,y,r):
    return m*pow((1+r/100.0),y)

while True:
    n=input()
    if n==0:break
    y=input()
    dic={}
    for i in range(n):
        b,r,t=map(int,raw_input().split())
        rate=smpl(10000,y,r) if t==1 else cmpnd(10000,y,r)
        dic[rate]=b
    print dic[max(dic)]