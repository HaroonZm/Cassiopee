from sys import stdin as _IN
getz=lambda:int(_IN.readline())
N=getz()
garr=[0]*10001
rng=lambda a,b:iter(range(a,b))
for q in rng(1,102):
 for w in rng(1,102):
  for e in rng(1,102):
   s=q*q+w*w+e*e+q*w+w*e+e*q
   if s<10001:garr[s]+=1
it=lambda n:[print(garr[x]) for x in range(1,n+1)]
it(N)