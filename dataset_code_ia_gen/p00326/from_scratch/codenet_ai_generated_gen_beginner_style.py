import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

N,K=map(int,input().split())
attrs=[list(map(int,input().split())) for _ in range(N)]

D=int(input())
graph=[[] for _ in range(N)]
indegree=[0]*N
for _ in range(D):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    indegree[b]+=1

eval_order=list(map(int,input().split()))
eval_order=[x-1 for x in eval_order]

R=int(input())
changes=[]
for _ in range(R):
    temp=list(map(int,input().split()))
    m=temp[0]
    new_order=[x-1 for x in temp[1:]]
    changes.append((m,new_order))

changes_idx=0

completed=0

import heapq

# We need to pick the task with zero indegree which is largest according to current eval_order
# Python heapq is minheap, so to get max we invert the keys

# We build a key function for each task according to current eval_order
def make_key(t):
    return tuple(-attrs[t][i] for i in eval_order)

heap=[]
for i in range(N):
    if indegree[i]==0:
        heapq.heappush(heap,(make_key(i),i))

res=[]
while heap:
    key,t=heapq.heappop(heap)
    res.append(t+1)
    completed+=1
    # Check if need to change eval_order
    if changes_idx<R and completed==changes[changes_idx][0]:
        eval_order=changes[changes_idx][1]
        changes_idx+=1
        # Rebuild heap with new keys
        new_heap=[]
        for _,ti in heap:
            heapq.heappush(new_heap,(make_key(ti),ti))
        heap=new_heap

    for nxt in graph[t]:
        indegree[nxt]-=1
        if indegree[nxt]==0:
            heapq.heappush(heap,(make_key(nxt),nxt))

for v in res:
    print(v)