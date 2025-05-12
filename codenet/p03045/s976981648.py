import sys
def input():
    return sys.stdin.readline()[:-1]

N,M = list(map(int,input().split()))

e_list = [[] for i in range(N)]

for i in range(M):
    x,y,z = list(map(int,input().split()))
    x,y = x-1,y-1
    e_list[x].append(y)
    e_list[y].append(x)

from collections import deque

def BFS(vi,color,color_list):
    Q = deque([vi])
    color_list[vi]=color
    while len(Q)>0:
        v = Q.pop()
        for v1 in e_list[v]:
            if color_list[v1]==-1:
                color_list[v1]=color
                Q.appendleft(v1)

color_list = [-1]*N
color = 0

for i in range(N):
    if color_list[i]==-1:
        BFS(i,color,color_list)
        color+=1

print(color)