from collections import deque
import sys
f=sys.stdin
def paintout_graph(s,g,color):
 cnt,pre_color=0,s[0]
 que=[0]
 for pos in que:
  if s[pos]==pre_color:
   s[pos]=color
   cnt+=1
   que.extend(g[pos])
 return cnt
def bfs(s,graph):
 que=deque([(s,0,0)])
 while True:
  s,pre_cnt,depth=que.popleft()
  pre_color=s[0]
  colors=['R','G','B']
  colors.remove(pre_color)
  for si,color in zip((s,s[:]),colors):
   cnt=paintout_graph(si,graph,color)
   if cnt==len(si):
    return depth
   if cnt==pre_cnt:
    break
   que.append((si,cnt,depth+1))
def paintout_sq(s,color,w,h,x,y):
 neighbor,pre_color=set(),s[y*w+x]
 que=deque([(x,y)])
 while len(que):
  x,y=que.pop()
  pos=y*w+x
  if s[pos]==pre_color:
   s[pos]=color
   if 0<x: que.append((x-1,y))
   if 0<y: que.append((x,y-1))
   if x+1<w: que.append((x+1,y))
   if y+1<h: que.append((x,y+1))
  elif s[pos]!=color and isinstance(s[pos],int):
   neighbor.update([s[pos]])
 return neighbor
while True:
 w,h=map(int,f.readline().split())
 if w==h==0:
  break
 s=[f.readline().split() for _ in range(h)]
 s=[y for x in s for y in x]
 p=[]
 graph={}
 for y in range(h):
  for x in range(w):
   pos=y*w+x
   if s[pos] in ('R','G','B'):
    k=len(p)
    p.append(s[pos])
    neighbor=paintout_sq(s,k,w,h,x,y)
    neighbor=list(neighbor)
    try:
     graph[k].extend(neighbor)
    except KeyError:
     graph[k]=neighbor
    for ni in neighbor:
     try:
      graph[ni].append(k)
     except KeyError:
      graph[ni]=[k]
 print(bfs(p,graph))