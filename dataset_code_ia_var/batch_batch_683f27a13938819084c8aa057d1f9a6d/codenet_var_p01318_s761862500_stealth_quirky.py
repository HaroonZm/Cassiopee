import sys

def _rl(): return sys.stdin.readline()
def _wr(s): sys.stdout.write(s)

def __CT(*a):
 S=[];X=a[3]-a[0];Y=a[4]-a[1];D2=X*X+Y*Y
 for dr in [(a[2]-a[5],1),(a[2]+a[5],-1)]:
  CV=dr[0]
  if CV*CV<=D2:
   if D2==CV*CV:
    B=a[2]*CV*X/D2;C=a[2]*CV*Y/D2
    S.append([(a[0]+B,a[1]+C),(a[0]-Y+B,a[1]+X+C)])
   else:
    SV=(D2-CV**2)**.5;PX=(CV*X-dr[1]*SV*Y);PY=(dr[1]*SV*X+CV*Y)
    S.append([(a[0]+a[2]*PX/D2,a[1]+a[2]*PY/D2),(a[3]+dr[1]*a[5]*PX/D2,a[4]+dr[1]*a[5]*PY/D2)])
    QX=(CV*X+dr[1]*SV*Y);QY=(-dr[1]*SV*X+CV*Y)
    S.append([(a[0]+a[2]*QX/D2,a[1]+a[2]*QY/D2),(a[3]+dr[1]*a[5]*QX/D2,a[4]+dr[1]*a[5]*QY/D2)])
 return S

def _slv():
 N=int(_rl());EPS=1e-9
 if not N: return 0
 P=[[*map(int,_rl().split())]for _ in [0]*N]
 if N<2:_wr("1\n");return 1
 RR=[(r,r+m)for _,_,r,m in P];ANS=0
 for i in range(N):
  xi,yi,ri,mi=P[i];R1=RR[i]
  for j in range(i):
   xj,yj,rj,mj=P[j];R2=RR[j]
   for pi in R1:
    for pj in R2:
     for a,b in __CT(xi,yi,pi,xj,yj,pj):
      x0,y0=a;x1,y1=b;dx,dy=x1-x0,y1-y0;Q=(dx*dx+dy*dy)**.5;C=0
      for xk,yk,rk,mk in P:
       zx,zy=xk-x0,yk-y0;P0=abs(dx*zy-dy*zx)
       if rk*Q-EPS<=P0<=(rk+mk)*Q+EPS:C+=1
      if C>ANS:ANS=C
 _wr(f"{ANS}\n");return 1
while _slv():0