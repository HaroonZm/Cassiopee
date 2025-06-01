import sys
import threading
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        adj = [[] for _ in range(n+1)]
        degree = [0]*(n+1)
        for _ in range(m):
            u,v = map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1

        color = [ -1 ]*(n+1)
        def dfs(s):
            stack = [s]
            color[s]=0
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if color[w]==-1:
                        color[w] = 1 - color[u]
                        stack.append(w)
                    elif color[w]==color[u]:
                        return False
            return True

        def check_path_component(s):
            stack = [s]
            comp_nodes = []
            while stack:
                u = stack.pop()
                if color[u] == -2:
                    continue
                color[u] = -2
                comp_nodes.append(u)
                for w in adj[u]:
                    if color[w] != -2:
                        stack.append(w)
            for u in comp_nodes:
                deg = 0
                for w in adj[u]:
                    if w in comp_nodes:
                        deg+=1
                if deg>2:
                    return False
            ends = sum(1 for u in comp_nodes if sum(1 for w in adj[u] if w in comp_nodes)==1)
            if ends == 0 and len(comp_nodes)>1:
                return False
            if ends>2:
                return False
            return True

        ok = True
        color = [-1]*(n+1)
        for i in range(1,n+1):
            if color[i]==-1:
                if not dfs(i):
                    ok = False
                    break
        if not ok:
            print("no")
            continue

        color = [-1]*(n+1)
        # check if each connected component is a path graph (degree <=2, exactly two ends with degree 1 or zero ends if one node)
        visited = [False]*(n+1)
        def dfs_component(s):
            stack = [s]
            comp = []
            visited[s] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for w in adj[u]:
                    if not visited[w]:
                        visited[w]=True
                        stack.append(w)
            return comp

        for i in range(1,n+1):
            if not visited[i]:
                comp = dfs_component(i)
                degcnt = 0
                deg_one = 0
                degs = [0]*len(comp)
                idx = {v:ind for ind,v in enumerate(comp)}
                for u in comp:
                    cnt = 0
                    for w in adj[u]:
                        if w in idx:
                            cnt+=1
                    degs[idx[u]] = cnt
                    if cnt>2:
                        ok = False
                        break
                if not ok:
                    break
                ends = sum(1 for d in degs if d==1)
                if ends == 0 and len(comp)>1:
                    ok = False
                    break
                if ends>2:
                    ok = False
                    break

        print("yes" if ok else "no")

threading.Thread(target=main).start()