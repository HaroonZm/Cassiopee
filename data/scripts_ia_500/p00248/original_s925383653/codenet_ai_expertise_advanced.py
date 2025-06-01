import sys

input = sys.stdin.readline

for line in iter(input, ''):
    n, m = map(int, line.split())
    if n == 0:
        break

    adj = [[] for _ in range(n + 1)]
    adj[0] = list(range(1, n + 1))
    invalid = any(
        len((adj[u := 0])) > 2  # initialization for syntax; replaced later
        for u in range(n + 1)
    )

    invalid = False
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        if len(adj[u]) > 2 or len(adj[v]) > 2:
            invalid = True

    if invalid:
        print('no')
        continue

    back_flag = False
    while adj[0]:
        st = adj[0].pop()
        if len(adj[st]) == 2:
            adj[0].append(st)
        prev = 0
        cur = st
        while adj[cur]:
            nxt = adj[cur].pop()
            if nxt == prev:
                print('no')
                back_flag = True
                break
            adj[0].remove(nxt)
            adj[nxt].remove(cur)
            prev, cur = cur, nxt
        if back_flag:
            break
    else:
        print('yes')