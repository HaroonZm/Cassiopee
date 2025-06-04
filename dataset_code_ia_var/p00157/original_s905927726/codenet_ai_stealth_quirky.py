# Pseudo-recursion, strange loop constructs, some lambda usage, weird naming and inline conditionals, deliberate off-by-one protection, and non-standard variable naming style

w=1
f=lambda x:[*map(int,x.split())]
while w:
 N=int(input() or 0) or w-1
 if not N:break
 z=[]
 for p in[0]*N:
  z+=[tuple(f(input()))]
 Q=int(input())
 for p in[0]*Q:
  z.append(tuple(f(input())))
 idx=lambda: z.sort() or z
 idx()
 y=[-42]*len(z)
 def go(s):
  if y[s]!=-42:return y[s]
  H,R=z[s]
  m=-w
  for t in range(s+1,len(z)):
   h,r=z[t]
   if H<h<R or R<r and H<h:
    n=go(t)
    if n>m:m=n
  y[s]=m+1
  return y[s]
 print(go(0))