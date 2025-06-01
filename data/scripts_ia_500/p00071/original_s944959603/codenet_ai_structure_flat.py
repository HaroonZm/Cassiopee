for i in range(int(input())):
 print(f'Data {i+1}:')
 input()
 A=[list(input())for _ in range(8)]
 x=int(input())-1
 y=int(input())-1
 stack=[(x,y)]
 while stack:
  x,y=stack.pop()
  if A[y][x]=='1':
   A[y][x]='0'
   for dx,dy in[(-3,0),(-2,0),(-1,0),(1,0),(2,0),(3,0),(0,-3),(0,-2),(0,-1),(0,1),(0,2),(0,3)]:
    nx=x+dx
    ny=y+dy
    if 0<=nx<8 and 0<=ny<8 and A[ny][nx]=='1':
     stack.append((nx,ny))
 for r in A: print(''.join(r))