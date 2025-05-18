import sys
sys.setrecursionlimit(10 ** 7)

def resolve():
    def dfs1(r_topo, par):
        for i in reversed(r_topo):
            stack = [i]
            while stack:
                idx = stack.pop()
                for to in G[idx]:
                    if to == par[i]:
                        continue
                    dist[idx] = max(dist[idx], dist[to] + 1)

    def dfs2(idx, d_par, par):
        stack = [(idx,d_par, par)]
        while stack:
            idx, d_par, par = stack.pop()
            d_child = []
            d_child.append((0, -1))
            for to in G[idx]:
                if to == par:
                    d_child.append((d_par + 1, to))
                else:
                    d_child.append((dist[to] + 1, to))
            d_child.sort(reverse=True)
            ans[idx] = d_child[0][0]
            for to in G[idx]:
                if to == par:
                    continue
                nx_d_par = d_child[d_child[0][1] == to][0]
                stack.append((to, nx_d_par, idx))
                #dfs2(to, nx_d_par, idx)

    N = int(input())
    if N == 1:
        return print(0)

    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    topo = []
    P = [-1] * N
    node = [0]
    while node:
        s = node.pop()
        topo.append(s)
        for to in G[s]:
            if to == P[s]:
                continue
            P[to] = s
            node.append(to)

    dist = [0]*N
    ans = [0] * N
    dfs1(topo,P)
    dfs2(0, 0, -1)
    for i in range(N):
        print((N - 1) * 2 - ans[i])

if __name__ == '__main__':
    resolve()