import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

"""
・pseudo-tree graph
・in_deg = 1が保証されているので、向きの揃ったcycleがある
・1箇所の2択を決めれば全部決まる
"""

N = int(readline())
parent = [0] + list(map(int,read().split()))

child = [[] for _ in range(N+1)]
for i,x in enumerate(parent):
    child[x].append(i)

out_deg = [len(x) for x in child]

out_deg

G = [-1] * (N+1)

# とりあえず唯一のサイクル以外を処理：out_deg=0の頂点を捨てていく

stack = [i for i,x in enumerate(out_deg) if not x]
while stack:
    x = stack.pop()
    se = set(G[c] for c in child[x])
    g = 0
    while g in se:
        g += 1
    G[x] = g
    p = parent[x]
    out_deg[p] -= 1
    if not out_deg[p]:
        stack.append(p)

"""
・grundy数の候補は2種。
・片方決め打って計算。2周grundy数を計算してstableになっていればよい。
"""

for i,x in enumerate(out_deg[1:],1):
    if x==1:
        root = i
        break

cycle_len = sum(out_deg[1:])

is_stable = False
x = root
for _ in range(cycle_len*2+10):
    se = set(G[c] for c in child[x])
    g = 0
    while g in se:
        g += 1
    if g == G[x]:
        is_stable = True
        break
    G[x] = g
    x = parent[x]

answer = 'POSSIBLE' if is_stable else 'IMPOSSIBLE'
print(answer)