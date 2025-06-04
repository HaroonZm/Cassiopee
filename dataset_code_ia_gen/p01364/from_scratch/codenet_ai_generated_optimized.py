import sys
import math

for line in sys.stdin:
    if not line.strip():
        continue
    N,D=map(int,line.split())
    if N==0 and D==0:
        break
    x=y=theta=0.0
    for _ in range(N):
        Lspeed,Rspeed,time=map(int,sys.stdin.readline().split())
        Lv=math.radians(Lspeed)*time
        Rv=math.radians(Rspeed)*time
        v=(Lv+Rv)*0.5*D
        w=(Rv-Lv)/(2*D)
        if abs(w)<1e-15:
            x+=v*math.cos(theta)
            y+=v*math.sin(theta)
        else:
            r=v/w
            x+=r*(math.sin(theta+w)-math.sin(theta))
            y+=r*(-math.cos(theta+w)+math.cos(theta))
            theta+=w
    print(f"{x:.5f}")
    print(f"{y:.5f}")