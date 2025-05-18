def solve():
    from sys import stdin
    f_i = stdin
    
    N, K = map(int, f_i.readline().split())
    
    # Since min-heap is used, set the attribute to a negative value.
    F = [list(map(lambda x: -int(x), f_i.readline().split())) \
         for i in range(N)]
    
    D = int(f_i.readline())
    adj = [[] for i in range(N)]
    input_edge = [0] * N
    for i in range(D):
        a, b = map(int, f_i.readline().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        input_edge[b] += 1
    
    E1 = tuple(map(lambda x: int(x) - 1, f_i.readline().split()))
    
    from itertools import permutations
    # {evaluation order: list of tasks with no input edges}
    M = dict(zip(permutations(range(K)), [[] for i in range(24)]))
    for i in range(N):
        if not input_edge[i]:
            f = F[i]
            for E in M:
                # [sorted attributes] + [task number]
                M[E].append([f[e] for e in E] + [i])
    
    R = int(f_i.readline())
    from heapq import heapify, heappop, heappush
    for k in M:
        heapify(M[k])
    
    ans = []
    unprocessed = [True] * N
    for i in range(R):
        E2 = tuple(map(lambda x: int(x) - 1, f_i.readline().split()))
        m = E2[0]
        E2 = E2[1:]
        tasks = M[E1]
        
        # topological sort
        while len(ans) <= m:
            while True:
                t1 = heappop(tasks)
                if unprocessed[t1[-1]]:
                    break
            tn1 = t1[-1]
            unprocessed[tn1] = False
            ans.append(str(tn1 + 1))
            for tn2 in adj[tn1]:
                input_edge[tn2] -= 1
                if not input_edge[tn2]:
                    f = F[tn2]
                    for E in M:
                        heappush(M[E], [f[e] for e in E] + [tn2])
        E1 = E2
    
    # Processing the remaining tasks
    tasks = M[E1]
    while len(ans) < N:
        while True:
            t1 = heappop(tasks)
            if unprocessed[t1[-1]]:
                break
        tn1 = t1[-1]
        ans.append(str(tn1 + 1))
        for tn2 in adj[tn1]:
            input_edge[tn2] -= 1
            if not input_edge[tn2]:
                f = F[tn2]
                heappush(tasks, [f[e] for e in E1] + [tn2])
    print('\n'.join(ans))

solve()