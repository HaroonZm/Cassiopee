N, M = map(int, input().split())
edges = [[] for _ in range(N)]

for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].append(to)
    edges[to].append(fr)

def isBipartite():
    sign = [-1] * N
    st = [(0, 0)]
    while st:
        now, p = st.pop()

        if sign[now] != -1 and sign[now] != p:
            return -1
        if sign[now] == p:
            continue
        sign[now] = p

        for to in edges[now]:
            st.append((to, (p + 1) % 2))

    return sum(sign)

s = isBipartite()

if s == -1:
    print(N * (N - 1) // 2 - M)
else:
    print(s * (N - s) - M)