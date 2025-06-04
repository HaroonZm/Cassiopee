def main():
    import sys
    sys.setrecursionlimit(10**7)

    def dfs(u):
        nonlocal idx
        visited[u] = True
        on_stack[u] = True
        stack.append(u)
        v = graph[u]
        if not visited[v]:
            dfs(v)
        elif on_stack[v]:
            # cycle detected
            cycle_nodes = 0
            for i in range(len(stack)-1, -1, -1):
                cycle_nodes +=1
                if stack[i] == v:
                    break
            nonlocal cycle_count
            cycle_count += 1
        on_stack[u] = False
        stack.pop()

    for line in sys.stdin:
        N = line.strip()
        if N == '0':
            break
        N = int(N)
        graph = [0]*(N*N)
        for i in range(N):
            data = sys.stdin.readline().strip().split()
            for j in range(N):
                x = int(data[2*j])
                y = int(data[2*j+1])
                graph[i*N+j] = x*N + y

        visited = [False]*(N*N)
        on_stack = [False]*(N*N)
        stack = []
        cycle_count = 0
        for u in range(N*N):
            if not visited[u]:
                dfs(u)
        print(cycle_count)

if __name__ == '__main__':
    main()