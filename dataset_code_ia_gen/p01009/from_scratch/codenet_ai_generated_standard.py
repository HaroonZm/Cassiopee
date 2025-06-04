import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

N,Q=map(int,input().split())
parent=[i for i in range(N+1)]
dist=[0]*(N+1)

def find(x):
    if parent[x]==x:
        return x
    r=find(parent[x])
    dist[x]+=dist[parent[x]]
    parent[x]=r
    return r

def union(a,b,c):
    ra=find(a)
    rb=find(b)
    if ra!=rb:
        parent[rb]=ra
        dist[rb]=dist[a]-dist[b]+c

for _ in range(Q):
    line=input().split()
    if line[0]=="IN":
        A,B,C=map(int,line[1:])
        union(A,B,C)
    else:
        A,B=map(int,line[1:])
        ra=find(A)
        rb=find(B)
        if ra!=rb:
            print("WARNING")
        else:
            print(dist[B]-dist[A])