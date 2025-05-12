def cross(a,b):
  return a.real*b.imag-a.imag*b.real

def intersection(p0,p1,p2,p3):
  a1=p3-p2
  b1=p0-p2
  b2=p1-p2
  s1=cross(b1,a1)
  s2=cross(a1,b2)
  c1=p0+(p1-p0)*s1/(s1+s2) #面積比を使う
  return c1

q=int(input())

for _ in [0]*q:
  x_y=map(int,input().split())
  p0,p1,p2,p3=[x+y*1j for x,y in zip(*[x_y]*2)]
  c1=intersection(p0,p1,p2,p3)
  print('{:.10f} {:.10f}'.format(c1.real,c1.imag))