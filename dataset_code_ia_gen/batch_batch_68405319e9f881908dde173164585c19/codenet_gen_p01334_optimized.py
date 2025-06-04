import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        # lire la grille des sauts
        jumps = [tuple(map(int, input().split())) for _ in range(N)]
        # chaque ligne contient 2*N entiers
        # on transforme en un tableau 2D de dimensions N*N, avec pour chaque case (nx, ny)
        graph = [None] * (N*N)
        for i in range(N):
            for j in range(N):
                x = jumps[i][2*j]
                y = jumps[i][2*j+1]
                graph[i*N+j] = x*N + y

        visited = [0]*(N*N) # 0 = non visité, 1 = en cours d'exploration, 2 = exploré
        cycle_count = 0

        def dfs(u):
            nonlocal cycle_count
            visited[u] = 1
            v = graph[u]
            if visited[v] == 0:
                dfs(v)
            elif visited[v] == 1:
                # trouvé un cycle
                cycle_count += 1
            visited[u] = 2

        for node in range(N*N):
            if visited[node] == 0:
                dfs(node)

        print(cycle_count)

main()