V, E, K = map(int, input().split())
edges = [[] for _ in range(V)]
for _ in range(E):
    v1, v2, c = map(int, input().split())
    edges[v1].append((v2, c))

from collections import deque
max_steps = 100
# dp[node][steps] = max_score achievable at node with steps edges used
dp = [[-1]*(max_steps+1) for _ in range(V)]
# parent[node][steps] = (prev_node, prev_steps)
parent = [[None]*(max_steps+1) for _ in range(V)]

queue = deque()
# Initialize: from any node, 0 steps, score 0
for i in range(V):
    dp[i][0] = 0
    queue.append((i,0))

best_steps = None
best_score = -1
best_node = None

while queue:
    node, step = queue.popleft()
    if step == max_steps:
        continue
    cur_score = dp[node][step]
    for nxt, cost in edges[node]:
        nstep = step+1
        nscore = cur_score + cost
        if dp[nxt][nstep] < nscore:
            dp[nxt][nstep] = nscore
            parent[nxt][nstep] = (node, step)
            queue.append((nxt,nstep))
            if nscore >= K:
                if best_steps is None or nstep < best_steps or (nstep == best_steps and nscore > best_score):
                    best_steps = nstep
                    best_score = nscore
                    best_node = nxt

if best_steps is not None:
    print(best_steps)
    if best_steps <= 100:
        path = []
        cur_node = best_node
        cur_step = best_steps
        while cur_step > 0:
            path.append(cur_node)
            cur_node, cur_step = parent[cur_node][cur_step]
        path.append(cur_node)
        print(' '.join(map(str, path[::-1])))
else:
    print(-1)