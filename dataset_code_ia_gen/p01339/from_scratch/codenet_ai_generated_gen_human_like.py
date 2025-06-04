MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
inv_graph = [[] for _ in range(N)]
S_list = [-1]*N
for _ in range(M):
    S, D = map(int, input().split())
    S -= 1
    D -= 1
    graph[S].append(D)
    inv_graph[D].append(S)
    S_list[S] = D

visited = [False]*N
order = []

def dfs1(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs1(v)
    order.append(u)

for i in range(N):
    if not visited[i]:
        dfs1(i)

visited = [False]*N
component = [0]*N
curr_comp = 0

def dfs2(u):
    component[u] = curr_comp
    visited[u] = True
    for v in inv_graph[u]:
        if not visited[v]:
            dfs2(v)

for u in reversed(order):
    if not visited[u]:
        dfs2(u)
        curr_comp += 1

# Build condensed graph of SCCs
condensed_graph = [[] for _ in range(curr_comp)]
in_deg = [0]*curr_comp
for u in range(N):
    for v in graph[u]:
        cu = component[u]
        cv = component[v]
        if cu != cv:
            condensed_graph[cu].append(cv)
            in_deg[cv] += 1

# Count SCC sizes and detect cycles within SCC
scc_size = [0]*curr_comp
for i in range(N):
    scc_size[component[i]] += 1

# If scc's size >1 or there's a self-loop, it's a cycle (only 2 states: all fingers off or all on)
# Else (size=1 and no self-loop) => 2 states (finger off or on)
# Wait, per problem, cycles mean fingers in SCC must share state (all off or all on)
# So each cyclic SCC contributes 2 states.
# For acyclic SCC (single node, no self-loop), that finger can be chosen on or off independently: 2 states.

# However, because edges represent "S->D: If S bends, D bends", 
# for fingers in same SCC cycle, their states must be equal (all bend or all do not bend).
# So each SCC represent one group. So total number is product of 2 for each SCC.

# Each scc corresponds to one "unit" contributing 2 states
result = 1
for i in range(curr_comp):
    result = (result * 2) % MOD

print(result)