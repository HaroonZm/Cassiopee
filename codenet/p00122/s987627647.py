R1=range(-2,3)
R2=range(-1,2)
A1=[(x,y) for x in R1 for y in R1 if 3<x**2+y**2<6]
A2=[(x,y) for x in R2 for y in R2]
def fi(): return map(int,raw_input().split(" "))
def f(x,y,i):
  A=[A1,A2][i>0]
  return set([(x+dx,y+dy) for dx,dy in A if 0<=x+dx<10 and 0<=y+dy<10])

while 1:
  xf,yf=fi()
  if yf==xf==0: break
  ns=input()
  tmp=fi()
  PA=zip(tmp[0::2],tmp[1::2])
  FA=set([(xf,yf)])
  for xs,ys in PA:
    SA=f(xs,ys,1)
    tmp=set([])
    for xf,yf in FA: tmp=tmp|(SA&f(xf,yf,0))
    FA=tmp
  print ["NA","OK"][len(FA)>0]