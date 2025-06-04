t=int(input())
d={'U':(-1,0,'^'),'D':(1,0,'v'),'L':(0,-1,'<'),'R':(0,1,'>')}
for _ in range(t):
 h,w=map(int,input().split())
 m=[list(input()) for __ in range(h)]
 n=int(input())
 cmds=input()
 for i in range(h):
  for j in range(w):
   if m[i][j] in '^v<>':
    x,y=i,j
    break
 for c in cmds:
  if c=='S':
   dx,dy=0,0
   if m[x][y]=='^':dx,dy=-1,0
   elif m[x][y]=='v':dx,dy=1,0
   elif m[x][y]=='<':dx,dy=0,-1
   else:dx,dy=0,1
   nx,ny=x+dx,y+dy
   while 0<=nx<h and 0<=ny<w:
    if m[nx][ny]=='*':
     m[nx][ny]='.'
     break
    if m[nx][ny]=='#':break
    nx+=dx
    ny+=dy
  else:
   dx,dy,face=d[c]
   m[x][y]=face
   nx,ny=x+dx,y+dy
   if 0<=nx<h and 0<=ny<w and m[nx][ny]=='.': 
    m[x][y]='.'
    m[nx][ny]=face
    x,y=nx,ny
 for line in m:print(''.join(line))
 if _!=t-1:print()