import math as M
def R(A): return (A[0]**2+A[1]**2)**.5
def I(i): return [map(int,raw_input().split()) for _ in [0]*i]
def C(a,b): return a>b or abs(a-b)<1e-6
def f(e1):
  tx,ty,sx,sy=e1
  x=[]
  st=[tx-sx,ty-sy]; rst=R(st)
  for e2 in WP:
    wx,wy,r=e2
    wt=[tx-wx,ty-wy]; rwt=R(wt)
    sw=[wx-sx,wy-sy]; rsw=R(sw)
    F=[rwt<r,rsw<r]
    c=1
    if F==[1,0] or F==[0,1]: return 0
    elif F==[0,0]:
      a=M.pi/2-M.acos(r/rsw)
      b=M.acos(round((sw[0]*st[0]+sw[1]*st[1])/rsw/rst,4))
      if C(a,b) and C(rst**2,rsw**2-r**2): return 0
    x.append(c)
  return all(x)

while 1:
  n=input()
  if n==0: break
  WP=I(n)
  P=I(input())
  for e in P: print ["Safe","Danger"][f(e)]