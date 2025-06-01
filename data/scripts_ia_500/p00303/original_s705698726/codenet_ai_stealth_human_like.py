def traverse(node, seen, result):
    # if node was already seen, no need to continue
    if seen[node]:
        return
    seen[node] = True
    for neighbor in edges[node]:
        traverse(neighbor, seen, result)
    result.append(node)  # add after exploring all children

def get_component(node):
    if visited[node]:
        return []
    visited[node] = True
    components = [node]
    for nxt in rev_edges[node]:
        components += get_component(nxt)
    return components

n = int(input())
edges = [[] for _ in range(200)]
rev_edges = [[] for _ in range(200)]

for _ in range(n):
    u, s, d = input().split()
    u = int(u) - 1
    d = int(d) - 1 + 100  # second group starts at 100, maybe a hack
    if s == "lock":
        # for "lock", edge from destination group to source
        edges[d].append(u)
        rev_edges[u].append(d)
    else:
        edges[u].append(d)
        rev_edges[d].append(u)

order = []
visited = [False] * 200
for i in range(200):
    if not visited[i]:
        traverse(i, visited, order)

order.reverse()  # reverse the finishing order for second pass
visited = [False] * 200
for node in order:
    if not visited[node]:
        comp = get_component(node)
        if len(comp) >= 2:  # found a component of size >= 2, print 1 and stop
            print(1)
            break
else:
    print(0)