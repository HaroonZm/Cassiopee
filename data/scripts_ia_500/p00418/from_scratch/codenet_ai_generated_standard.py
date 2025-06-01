import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,R = map(int,input().split())
t = [0]*N
e = [0]*N
for i in range(N):
    ti,ei = map(int,input().split())
    t[i],e[i] = ti,ei

adj = [[] for _ in range(N)]
for _ in range(R):
    a,b,c = map(int,input().split())
    a-=1; b-=1
    adj[a].append((b,c))   # x_a - x_b <= c
    adj[b].append((a,-c))  # x_b - x_a <= -c

visited = [False]*N
def dfs(u, comp):
    stack = [u]
    comp_nodes = []
    while stack:
        v = stack.pop()
        if visited[v]: continue
        visited[v] = True
        comp_nodes.append(v)
        for w,_ in adj[v]:
            if not visited[w]:
                stack.append(w)
    return comp_nodes

def is_feasible(nodes, lb, ub):
    from collections import deque
    dist = [0]*(len(nodes))
    inq = [False]*len(nodes)
    count = [0]*len(nodes)
    idx = {v:i for i,v in enumerate(nodes)}
    q = deque()
    for i in range(len(nodes)):
        dist[i] = 0
        q.append(i)
        inq[i] = True
    while q:
        u = q.popleft()
        inq[u] = False
        v_u = nodes[u]
        if dist[u] < lb[v_u]:
            dist[u] = lb[v_u]
        if dist[u] > ub[v_u]:
            return None
        for w,c in adj[v_u]:
            if w not in idx: continue
            idxw = idx[w]
            if dist[idxw] > dist[u] - c:
                dist[idxw] = dist[u] - c
                if not inq[idxw]:
                    q.append(idxw)
                    inq[idxw] = True
                    count[idxw] += 1
                    if count[idxw] > len(nodes):
                        return None
    for i,v in enumerate(nodes):
        if dist[i]<lb[v] or dist[i]>ub[v]:
            return None
    return dist

ans = 0
visited = [False]*N
for i in range(N):
    if visited[i]: continue
    comp = dfs(i,[])
    lb = [0]*N
    ub = [0]*N
    for v in comp:
        lb[v] = 0
        ub[v] = t[v]
    dist = is_feasible(comp,lb,ub)
    if dist is None:
        # No feasible solution, then 0 usage for these machines
        continue
    # We have dist assigning upper bound usages satisfying all constraints with left side <= dist[u]
    # We want to assign x >= dist to maximize sum e_i*x_i, with x<=t_i, x - dist[u] >=0 fitting constraints
    # Constraints are inequalities x_a - x_b <= c_i, using dist as baseline, slack variables satisfy inequalities
    # We try to maximize sum e_i * x_i s.t. dist <= x_i <= t_i
    # Because constraints are already tight with dist, the slack variables form a polyhedron with 0 as baseline
    # No easy way to increase between dist and t_i, constraints apply to x_i - x_j differences
    # But slack variables (x_i - dist_i) must also satisfy x_i - x_j <= c_i - (dist_a - dist_b)
    # Because dist satisfy constraints, slacks must satisfy inequalities with rhs adjusted.
    # Slack variables >= 0; upper bounds = t_i - dist[i]
    # Now, slack variables: s_i = x_i - dist_i, want maximize sum e_i * s_i under constraints and 0<=s_i<= t_i-dist_i
    # We can greedily set slack variables s_i to their upper bound, and if constraints violated, decrease accordingly along paths.
    # But constraints can lower bound the difference of s_i - s_j.
    # This forms problem similar to difference constraints over slack variables, with upper bounds.

    # To solve:
    # 1) For each variable s_i, s_i <= ubs[i]= t[i] - dist[i]
    # 2) s_a - s_b <= c_i - (dist_a - dist_b)
    # 3) s_i >= 0
    # We want to maximize sum e_i * s_i with constraints.

    # This is a linear program with difference constraints and box constraints
    # Solution is found by assigning s_i as high as possible with constraints.
    # For each strongly connected component in slack graph, the minimal upper bound difference sum applies.

    # We can compute max s_i with Bellman-Ford on slack variables constraints:
    # s_a - s_b <= rhs  => s_a <= s_b + rhs

    # Let's construct graph of slack variables with edges (b->a) weight rhs
    slackN = len(comp)
    slackidx = {v:i for i,v in enumerate(comp)}
    slack_adj = [[] for _ in range(slackN)]
    for v in comp:
        for w,c in adj[v]:
            if w not in slackidx: continue
            a_,b_ = slackidx[v], slackidx[w]
            rhs = c - (dist[a_] - dist[b_])
            slack_adj[b_].append((a_,rhs))

    from collections import deque
    INF = 10**15
    low = [0]*slackN
    high = [t[v]-dist[slackidx[v]] for v in comp]
    val = [high[i] for i in range(slackN)]

    # For each edge b->a with weight rhs: val[a] <= val[b] + rhs
    # So val[i] <= high[i], val[i]>=0, and for each edge val[a]-val[b]<=rhs
    # We'll update val values iteratively:
    updated = True
    for _ in range(slackN):
        updated = False
        for u in range(slackN):
            for v, wght in slack_adj[u]:
                if val[v] > val[u] + wght:
                    val[v] = val[u] + wght
                    if val[v]<0:
                        val[v] = 0
                    if val[v] > high[v]:
                        val[v] = high[v]
                    updated = True
        if not updated:
            break
    else:
        # Negative cycle means no solution
        continue

    for i in range(slackN):
        if val[i]<0 or val[i]>high[i]:
            val[i] = min(max(val[i],0),high[i])
    res = 0
    for i,v in enumerate(comp):
        x_i = dist[i] + val[i]
        if x_i > t[v]:
            x_i = t[v]
        if x_i <0:
            x_i = 0
        res += e[v]*x_i
    ans += res

print(ans)