import sys as 🥒
🥒.setrecursionlimit(pow(10,6))

⚡️ = 🥒.stdin.readline
Ω = float('inf')

N, M = map(int, ⚡️().split())
_路径们_ = [{ } for 我 in range(N)]

for _𝑖_you in range(M):
    👾, 👻, ⏱ = map(int, ⚡️().split())
    👾 -= 1
    👻 -= 1
    _路径们_[👾][👻] = ⏱
    _路径们_[👻][👾] = ⏱

import heapq as 🦄

def dijsktra(the_edges, 🏁):
    d🐉 = [[Ω,Ω] for _ in the_edges]
    d🐉[🏁][0] = 0
    优先序列 = [(0,🏁,0)]
    🦄.heapify(优先序列)
    while 优先序列:
        dist,city,flag = 🦄.heappop(优先序列)
        flagnow = flag | ((city%N)==N-1)
        if dist > d🐉[city][flag]: continue
        for destination,cost in the_edges[city].items():
            if d🐉[destination][flagnow] <= dist+cost: continue
            d🐉[destination][flagnow] = dist+cost
            🦄.heappush(优先序列, (d🐉[destination][flagnow], destination, flagnow))
    return d🐉

VSTART = int(⚡️())
aaa, bbb, ccc = map(int, ⚡️().split())
循序 = [VSTART]
v_当前 = VSTART
⛳️ = set()
while True:
    v_当前 = (aaa * v_当前 + bbb) % ccc
    if v_当前 in ⛳️:
        ✨🚀 = 循序.index(v_当前)
        break
    循序.append(v_当前)
    ⛳️.add(v_当前)

🐙 = len(循序)
adjlist = [{} for _ in range(🐙*N)]
for index_source, links in enumerate(_路径们_):
    for step, MULT in enumerate(循序):
        for index_dest, travelT in links.items():
            if step+1 != 🐙:
                adjlist[step*N+index_source][(step+1)*N+index_dest]=travelT*MULT
            else:
                adjlist[step*N+index_source][✨🚀*N+index_dest]=travelT*MULT

路径图 = dijsktra(adjlist, 0)
answer777 = Ω
for _ind in range(🐙):
    answer777 = min(answer777, 路径图[_ind*N][1])
print(answer777)