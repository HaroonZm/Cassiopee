N = int(input())
for i in range(N):
    L = []
    while 1:
        *s, = map(int, input().split())
        if s[-1] == 0:
            L.extend(s[:-1])
            break
        L.extend(s)
    G = []
    st = []
    cur = 0
    for s in L:
        if s > 0:
            G.append([])
            if st:
                u = [cur, s-1]
                v = st[-1]
                v[1] -= 1
                G[u[0]].append(v[0])
                G[v[0]].append(u[0])
                st.append(u)
                while st and st[-1][1] == 0:
                    st.pop()
            else:
                st.append([cur, s])
            cur += 1
            continue
        u = st[s-1]; u[1] -= 1
        v = st[-1]; v[1] -= 1
        G[u[0]].append(v[0])
        G[v[0]].append(u[0])
        while st and st[-1][1] == 0:
            st.pop()
    for i, vs in enumerate(G):
        vs.sort()
        print(i+1, *map(lambda x: x+1, vs))