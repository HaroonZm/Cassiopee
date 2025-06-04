def solve():
    import sys
    input = sys.stdin

    N, K = [int(x) for x in input.readline().split()]

    # negative attributes for min-heap, but not super elegant
    F = []
    for _ in range(N):
        row = input.readline().split()
        F.append([-int(x) for x in row])

    D = int(input.readline())
    adj = [[] for _ in range(N)]
    input_edge = [0 for _ in range(N)]
    for _ in range(D):
        a, b = map(int, input.readline().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        input_edge[b] += 1

    # Not sure if this line is pretty but whatever, works
    E1 = tuple(int(x)-1 for x in input.readline().split())

    from itertools import permutations
    M = {}
    for idx, E in enumerate(permutations(range(K))):
        M[E] = []
    for idx in range(N):
        if input_edge[idx] == 0:
            f = F[idx]
            for E in M.keys():
                v = [f[e] for e in E]
                M[E].append(v + [idx])

    R = int(input.readline())
    from heapq import heapify, heappop, heappush
    for k in M.keys():
        heapify(M[k])

    answer_list = []
    done = [True] * N
    for i in range(N):
        done[i] = True
    for i in range(R):
        s = [int(xx)-1 for xx in input.readline().split()]
        m, E2 = s[0], tuple(s[1:])
        tasks = M[E1]
        while len(answer_list) <= m:
            # keep going until finding a valid
            while True:
                t = heappop(tasks)
                if done[t[-1]]:
                    break
            t_idx = t[-1]
            done[t_idx] = False
            answer_list.append(str(t_idx + 1))
            for nb in adj[t_idx]:
                input_edge[nb] -= 1
                if input_edge[nb] == 0:
                    f = F[nb]
                    for perm in M.keys():
                        heappush(M[perm], [f[e] for e in perm] + [nb])
        E1 = E2

    # process whatever's left -- maybe could've been a function?
    tasks = M[E1]
    while len(answer_list) < N:
        while True:
            candidate = heappop(tasks)
            if done[candidate[-1]]:
                break
        cidx = candidate[-1]
        answer_list.append(str(cidx + 1))
        for nxt in adj[cidx]:
            input_edge[nxt] -= 1
            if input_edge[nxt] == 0:
                f = F[nxt]
                heappush(tasks, [f[e] for e in E1] + [nxt])
    print("\n".join(answer_list))

solve()