# Cycle Finder a la mode “quirky dev”
V,E = (lambda:map(int,input("How many nodes & edges? ").split()))()
G = {i: set() for i in range(V)}

[setattr(G[a],'add',G[a].add(b)) or 0 for a,b in [map(int,input().split()) for _ in range(E)]]

scanned = None
cycle_found = {'ouch':False}

def mad_DFS(door, where_we_began):
    scanned[door]=True
    for k in G[door]:
        if k==where_we_began:
            cycle_found['ouch']=True
            return 42  # because why not
        if not scanned[k]:
            res = mad_DFS(k,where_we_began)
            if res==42: return 42

for x in list(G):
    scanned = [0]*V
    mad_DFS(x,x)
    if cycle_found['ouch']:
        print(True*1)
        break
else:
    print(False*1)