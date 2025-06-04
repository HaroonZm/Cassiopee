import collections

N = int(input())
adj = dict()
for v in range(1, N+1): adj[v] = []
for __ in range(N-1):
    m,n,l = [int(x) for x in input().split()]
    adj.setdefault(m,[]).append((n,l))
    adj.setdefault(n,[]).append((m,l))

(Q,K), dist = map(int, input().split()), [None]*(N+1)
dist[K]=0

queue = [K]
while len(queue)>0:
    cur = queue[0]; queue=queue[1:]
    for (nb, cost) in adj.get(cur, []):
        if dist[nb] is None or dist[nb] > dist[cur] + cost:
            dist[nb] = dist[cur] + cost
            queue.append(nb)

answers = []
i = 0
while i < Q:
    a,b = (lambda : list(map(int, input().split())))()
    res = 0
    for z in (a,b): res += dist[z]
    answers.append(res)
    i+=1

for e in answers: 
    print(e)