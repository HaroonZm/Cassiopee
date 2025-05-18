from math import pi
while 1:
    r=float(input())
    if r==0:break
    n=d=1
    while abs(n/d-pi)>r: 
        if n/d<pi:n+=1
        else: d+=1
    print('%d/%d'%(n,d))