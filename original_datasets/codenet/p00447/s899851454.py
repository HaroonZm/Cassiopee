def f(e):
 a=sorted([list(map(int,input().split()))for _ in[0]*int(e)],key=lambda x:x[0])
 b=sorted([list(map(int,input().split()))for _ in[0]*int(input())],key=lambda x:x[0])
 for s,t in b:
  u,v=a[0]
  x,y=s-u,t-v
  for u,v in a:
   if[u+x,v+y]not in b:break
  else:return print(x,y)
for e in iter(input,'0'):f(e)