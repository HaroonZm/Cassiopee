c,*s=input()
n=len(s)
import itertools as it
a=0
for p in it.product(['','+'],repeat=n):
  t=c
  for i in range(n): t+=p[i]+s[i]
  a+=eval(t)
print(a)