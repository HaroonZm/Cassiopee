for e in iter(input,'0'):
 a=[[*map(int,input().split())]for _ in[0]*int(e)]
 s,t=min(a)
 b={tuple(map(int,input().split()))for _ in[0]*int(input())}
 m=max(b)[0]-max(a)[0]+s
 for x,y in b:
  if x<=m:
   for u,v in a:
    if(x+u-s,y+v-t)not in b:break
   else:print(x-s,y-t);break