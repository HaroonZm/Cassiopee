import collections

V, E = map(int, input().split())
Elist = [[] for _ in range(V)]
edges = []

for _ in range(E):
    s, t, c = map(int, input().split())
    Elist[s].append({'to': t, 'cap': c, 'rev': len(Elist[t])})
    Elist[t].append({'to': s, 'cap': 0, 'rev': len(Elist[s])-1})

source, sink = 0, V-1
INF = float('inf')
maxflow = 0

while True:
    level = [-1] * V
    level[source] = 0
    que = collections.deque()
    que.append(source)
    while que:
        fr = que.popleft()
        for e in Elist[fr]:
            if e['cap'] > 0 and level[e['to']] < 0:
                level[e['to']] = level[fr] + 1
                que.append(e['to'])

    if level[sink] < 0:
        break

    itr = [0] * V
    stack = []
    flowsum = 0
    while True:
        stack.append((source, INF))
        path = []
        flow = 0
        while stack:
            v, up = stack.pop()
            if v == sink:
                flow = up
                break
            found = False
            for i in range(itr[v], len(Elist[v])):
                itr[v] = i
                e = Elist[v][i]
                if e['cap'] > 0 and level[v] < level[e['to']]:
                    stack.append((v, up))
                    stack.append((e['to'], min(up, e['cap'])))
                    path.append((v, i))
                    found = True
                    break
            if not found:
                if path:
                    path.pop()
        if flow == 0:
            break
        maxflow += flow
        now = source
        for v, i in path:
            e = Elist[v][i]
            e['cap'] -= flow
            Elist[e['to']][e['rev']]['cap'] += flow

print(maxflow)