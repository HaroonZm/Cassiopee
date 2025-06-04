import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

color = [-1]*(V+1)
def dfs(u,c):
    color[u] = c
    for w in adj[u]:
        if color[w]<0:
            if not dfs(w,1-c):
                return False
        elif color[w]==c:
            return False
    return True

total_max_edges = V*(V-1)//2
added = 0
for v in range(1,V+1):
    if color[v]<0:
        nodes = [v]
        color[v] = 0
        stack = [v]
        count0 = 1
        count1 = 0
        edges = 0
        bip = True
        while stack:
            u = stack.pop()
            for w in adj[u]:
                edges += 1
                if color[w]<0:
                    color[w]=1-color[u]
                    if color[w]==0:
                        count0+=1
                    else:
                        count1+=1
                    stack.append(w)
                elif color[w]==color[u]:
                    bip = False
        edges//=2
        if not bip:
            print(-1)
            exit()
        max_edges = count0*count1
        added += max_edges - edges

print(added if added>0 else -1)