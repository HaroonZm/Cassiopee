from math import acos,sin,cos,radians
while 1:
    a,b,c,d=map(float,input().split())
    if a==b==c==d==-1:break
    a,c=radians(a),radians(c)
    print(int(6378.1*acos(sin(a)*sin(c) + cos(a)*cos(c)*cos(radians(d)-radians(b)))+0.5))