import heapq

v, e, f = map(int, input().split())
n = v
inf = 1000000007
e_list = [[] for _ in range(n)]

edge_objs = []

for _ in range(e):
    a, b, c, d = map(int, input().split())
    # Add forward edge
    edge_fwd = {'to': b, 'cap': c, 'rev': len(e_list[b]), 'cost': d}
    e_list[a].append(edge_fwd)
    # Add backward edge
    edge_bwd = {'to': a, 'cap': 0, 'rev': len(e_list[a]) - 1, 'cost': -d}
    e_list[b].append(edge_bwd)

res = 0
h = [0] * n
prevv = [0] * n
preve = [0] * n
source = 0
sink = n - 1

while f > 0:
    pq = []
    dist = [inf] * n
    dist[source] = 0
    heapq.heappush(pq, (0, source))
    while pq:
        cost, vtx = heapq.heappop(pq)
        cost = -cost
        if dist[vtx] < cost:
            continue
        for i, edge in enumerate(e_list[vtx]):
            if edge['cap'] > 0 and dist[vtx] - h[edge['to']] < dist[edge['to']] - edge['cost'] - h[vtx]:
                dist[edge['to']] = dist[vtx] + edge['cost'] + h[vtx] - h[edge['to']]
                prevv[edge['to']] = vtx
                preve[edge['to']] = i
                heapq.heappush(pq, (-dist[edge['to']], edge['to']))
    if dist[sink] == inf:
        print(-1)
        exit()
    for vtx in range(n):
        h[vtx] += dist[vtx]
    d = f
    vtx = sink
    while vtx != source:
        d = min(d, e_list[prevv[vtx]][preve[vtx]]['cap'])
        vtx = prevv[vtx]
    f -= d
    res += d * h[sink]
    vtx = sink
    while vtx != source:
        e_list[prevv[vtx]][preve[vtx]]['cap'] -= d
        rev = e_list[prevv[vtx]][preve[vtx]]['rev']
        e_list[vtx][rev]['cap'] += d
        vtx = prevv[vtx]
print(res)