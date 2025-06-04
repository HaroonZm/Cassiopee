n=int(input())
graph={}
for _ in range(n):
    u,s,d=input().split()
    u='u'+u
    d='d'+d
    if s=='lock':
        graph.setdefault(d,[]).append(u)
    else:
        graph.setdefault(u,[]).append(d)
visited=set()
recstack=set()
def dfs(v):
    visited.add(v)
    recstack.add(v)
    for nv in graph.get(v,[]):
        if nv not in visited:
            if dfs(nv):
                return True
        elif nv in recstack:
            return True
    recstack.remove(v)
    return False
print(1 if any(dfs(node) for node in graph if node not in visited) else 0)