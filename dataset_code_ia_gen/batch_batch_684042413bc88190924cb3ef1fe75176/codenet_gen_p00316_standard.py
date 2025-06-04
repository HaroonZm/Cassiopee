import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,M,K = map(int,input().split())
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
club = [-1]*(N+1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
        # merge club info
        if club[y] == -1 and club[x] != -1:
            club[y] = club[x]
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
        # merge club info
        if club[x] == -1 and club[y] != -1:
            club[x] = club[y]

def get_club(x):
    return club[find(x)]

for i in range(1,K+1):
    t,*a = map(int,input().split())
    if t == 1:
        a1,a2 = a
        r1 = find(a1)
        r2 = find(a2)
        if r1 == r2:
            continue
        # check for contradiction in club assignment
        c1 = club[r1]
        c2 = club[r2]
        if c1 != -1 and c2 != -1 and c1 != c2:
            print(i)
            exit()
        unite(a1,a2)
    else:
        c,x = a
        r = find(c)
        if club[r] == -1:
            club[r] = x
        elif club[r] != x:
            print(i)
            exit()
print(0)