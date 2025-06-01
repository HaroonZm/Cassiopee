import sys as _s;from sys import stdin as _si;input=_si.readline
def _main():
 while 1:
  n,h=map(int,input().split())
  if n==0:break
  a=[]
  for _ in" "*h:
   c,p,q=input().split()
   p,q=int(p)-1,int(q)-1
   if c=="xy":a+=[p+(q<<9)+(z<<18)for z in range(n)]
   elif c=="xz":a+=[p+(y<<9)+(q<<18)for y in range(n)]
   else:a+=[x+(p<<9)+(q<<18)for x in range(n)]
  print(pow(n,3)-len(set(a)))
_main()