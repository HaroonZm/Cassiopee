from collections import deque

def topologicalSort(v,e):
    global color,out,indeg
    color=["white" for _ in range(v)]
    indeg=[[0,[]] for _ in range(v)]
    out=[]

    for i in range(e):
        s,t=map(int,input().split())
        indeg[s][0] +=1
        indeg[t][1] +=[s]

    for i in range(v):
        if indeg[i][0]==0 and color[i]=="white":
            BFS(i)

    return out[::-1]

def BFS(s):
    Q=deque([])
    Q.append(s)
    color[s]="gray"
    while len(Q)!=0:
        u=Q.popleft()
        out.append(u)

        for i in indeg[u][1]:
            indeg[i][0] -=1
            if indeg[i][0]==0 and color[i]=="white":
                color[i]="gray"
                Q.append(i)

v,e=map(int,input().split())
for i in topologicalSort(v,e):
    print(i)