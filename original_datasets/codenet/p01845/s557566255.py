import math
while True:
    r,w,c,vr = map(int,input().split())
    if r==w==0: break
    r = math.ceil((w*c-r)/vr) if w*c-r>=0 else 0
    print(r)