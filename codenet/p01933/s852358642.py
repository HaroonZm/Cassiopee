import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
a = [int(readline())-1 for _ in [0]*N]
result = a.count(-1)

nodes = set()
node_add = nodes.add
hoge = set()
hoge_add = hoge.add
for i in range(N):
    if a[i] in hoge:
        node_add(a[i])
    hoge_add(a[i])

visited = set()
add = visited.add
startnode = {v: K-1 for v in {i for i in range(N) if a[i] > -1} - set(a)}
while startnode:
    nextnode = dict()
    for v, l in startnode.items():
        #print("start:", v, "length:", l)
        result += (v not in visited)
        add(v)
        v = a[v]
        while a[v] > -1 and v not in nodes and l > 0:
            #print(v)
            if v not in visited:
                result += 1
                add(v)
            l -= 1
            v = a[v]
        if a[v] > -1 and v in nodes and l > 0:
            #print("->", v)
            nextnode[v] = max(nextnode.get(v, 0), l-1)
    startnode = nextnode

print(result)