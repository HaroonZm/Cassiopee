import sys
sys.setrecursionlimit(10**7)

def dfs(u, parent, adj):
    # dfsが返すのはuからの部分木で爆破に必要な最短時間
    times = []
    for v, t in adj[u]:
        if v == parent:
            continue
        times.append(dfs(v, u, adj) + t*2)
    if not times:
        return 0
    # 複数の子の部分木がある時、一つは最後に処理するのでt*2のうちtだけ節約できる
    return sum(times) - max(times)//2

def main():
    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            a,b,t = map(int, sys.stdin.readline().split())
            adj[a].append((b,t))
            adj[b].append((a,t))
        # 1からスタートして爆破
        ans = dfs(1, -1, adj)
        print(ans)

if __name__ == '__main__':
    main()