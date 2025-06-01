from collections import deque
H,W,N=map(int,input().split())
e='X'*(W+2)
M=e+''.join('X'+input()+'X'for _ in[0]*H)+e
moves=(1,-1,W+2,-W-2)
def search(start,goal):
 queue=deque()
 queue.append((start,0))
 visited=[1]*len(M)
 visited[start]=0
 while queue:
  pos,dist=queue.popleft()
  for delta in moves:
   nxt=pos+delta
   if M[nxt]!='X' and visited[nxt]:
    if M[nxt]==goal:
     return nxt,dist+1
    visited[nxt]=0
    queue.append((nxt,dist+1))
pos=M.find('S')
total=0
for target in map(str,range(1,N+1)):
 pos,step=search(pos,target)
 total+=step
print(total)