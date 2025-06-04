import sys
input=sys.stdin.readline

while True:
    N,M,T=map(int,input().split())
    if N==0 and M==0 and T==0:
        break
    p=[0]*N
    t=[0]*N
    k=[0]*N
    for i in range(N):
        pi,ti,ki=map(int,input().split())
        p[i],t[i],k[i]=pi,ti,ki
    adj=[[] for _ in range(N)]
    for _ in range(M):
        a,b=map(int,input().split())
        adj[a-1].append(b-1)

    # We can start and end anywhere.
    # Observations:
    # - Since any movement costs 0 time, time is only consumed by watching ads.
    # - Watch each ad at most k[i] times.
    # - Cannot watch ad multiple times consecutively without moving.
    # - But links to self allow repeated watches with movement.

    # For each node i, watching advertisement once costs t[i] time, gives p[i] points.
    # The max times we can watch is k[i].
    # The order of visits affects which ads can be watched.

    # We want maximum points in T seconds.

    # DP approach:
    # Because we can move at zero time and start anywhere,
    # the problem reduces to:
    # For each node i, the maximum total points from watching ad multiple times up to k[i],
    # with the constraint that we can't watch ad twice in a row without moving.

    # Since there are M edges and N nodes, and links may form cycles,
    # to maximize points, we want to be able to watch ads repeatedly.
    # Because moving cost is 0, multiple cycles can be traversed.

    # Since watching ad twice consecutively is forbidden,
    # but we can watch it multiple times if we move (even self loops count as movement)
    # So the only constraint is to not watch ad twice without moving.

    # So to watch ad x times in a node:
    # - Need at least x-1 moves away and back to node.
    # - Since time to move is zero, can do so instantly.
    # - So to watch k[i] times on node i, need to find paths with at least k[i]-1 edges starting and ending at i.
    # - But since we can start anywhere, and possibly pick a cycle of length 1 (self-loop), this is possible
    #   if self-loop exists or a cycle with node i exists to move backward & forward.

    # Key insight:
    # For each node i:
    #   Let max_watch_i = min(k[i], maximal number of times ad can be watched considering cycles)
    #
    # The problem reduces to:
    # For each node i:
    # - maximum number of times ad can be watched is k[i]
    # - watching it once costs t[i] sec, gives p[i] points.

    # Since moving cost is zero, the limiting factor is time T.
    # So the maximum times ad i can be watched is min(k[i], T//t[i]).

    # We want to select visits to nodes and watch ads accordingly.

    # Because we can move instantly, we can visit any sequence of nodes via cycles.

    # So the problem becomes:
    # We have N items (ads):
    # For each item i:
    #   weight: t[i]
    #   value: p[i]
    #   max count: min(k[i], T//t[i])
    #
    # We want to maximize sum of value*count with sum weight*count <= T.

    # BUT there is the constraint of not watching ad twice consecutively without moving.

    # Can we watch ad i multiple times in a row without moving? No.
    #
    # But since moving cost 0, and loops exist to return and re-watch, the adjacency graph determines possibility.

    # So need to check if node i is inside a strongly connected component with at least one edge:
    # because with cycles, we can come back after moving.
    # For node i with no self-loop nor cycles, we can watch ad only once (or zero).

    # So for each node:
    #   - Compute if in a SCC of size>1 or self-loop exists -> infinite re-visits possible (up to k[i])
    #   - else only allowed to watch at most once

    # Then treat ads as bounded knapsack items with:
    #   count = k[i] if node has cycles else 1
    #   cost = t[i]
    #   value = p[i]

    # Solve bounded knapsack with capacity T and these items.

    # Step 1: compute SCC to find nodes with cycles
    # Step 2: Build is_cycle_node[i]: True if node i can be revisited infinitely (has cycle)
    # Step 3: bounded knapsack with counts ci = k[i] or 1 accordingly.

    sys.setrecursionlimit(10**7)

    # SCC - Tarjan
    stack=[]
    on_stack=[False]*N
    ids=[-1]*N
    low=[0]*N
    id_counter=0
    scc_id=[-1]*N
    scc_cnt=0

    def dfs(u):
        nonlocal id_counter,scc_cnt
        ids[u]=id_counter
        low[u]=id_counter
        id_counter+=1
        stack.append(u)
        on_stack[u]=True
        for v in adj[u]:
            if ids[v]==-1:
                dfs(v)
                low[u]=min(low[u],low[v])
            elif on_stack[v]:
                low[u]=min(low[u],ids[v])
        if low[u]==ids[u]:
            while True:
                node=stack.pop()
                on_stack[node]=False
                scc_id[node]=scc_cnt
                if node==u:
                    break
            scc_cnt+=1

    for i in range(N):
        if ids[i]==-1:
            dfs(i)

    # For each SCC, check if it has cycle:
    # if size>1 => has cycle
    # else if edge inside gives self-loop

    scc_size=[0]*scc_cnt
    for i in range(N):
        scc_size[scc_id[i]]+=1

    scc_has_cycle=[False]*scc_cnt
    for u in range(N):
        cu=scc_id[u]
        for v in adj[u]:
            cv=scc_id[v]
            if cu==cv:
                if u==v or scc_size[cu]>1:
                    scc_has_cycle[cu]=True

    is_cycle_node=[False]*N
    for i in range(N):
        if scc_has_cycle[scc_id[i]]:
            is_cycle_node[i]=True

    # For each node i:
    # max watch count = min(k[i], T//t[i]) if is_cycle_node[i], else min(1, T//t[i])

    max_counts=[0]*N
    for i in range(N):
        m = T//t[i]
        if is_cycle_node[i]:
            max_counts[i]=min(k[i], m)
        else:
            max_counts[i]=1 if m>=1 else 0

    # Now do bounded knapsack with these items:
    # N<=100, T<=10000, max_counts[i] up to k[i] but bounded by T//t[i].

    # Use binary splitting to speed up bounded knapsack.

    dp=[0]*(T+1)

    for i in range(N):
        cnt=max_counts[i]
        ti=t[i]
        pi=p[i]
        c=1
        while cnt>0:
            use=min(c,cnt)
            w=ti*use
            v=pi*use
            for time in range(T, w-1,-1):
                if dp[time-w]+v>dp[time]:
                    dp[time]=dp[time-w]+v
            cnt-=use
            c*=2

    print(max(dp))