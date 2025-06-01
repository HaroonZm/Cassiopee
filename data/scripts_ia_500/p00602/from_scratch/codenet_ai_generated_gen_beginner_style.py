def fibonacci_mod(n, mod):
    f = [1, 1]
    for i in range(2, n+1):
        f.append((f[i-1] + f[i-2]) % mod)
    return f[1:n+1]

def count_connected_subsets(V, d, N=1001):
    fib = fibonacci_mod(V, N)
    visited = [False] * V
    count = 0
    for i in range(V):
        if not visited[i]:
            count += 1
            # BFS to find all nodes connected to i
            queue = [i]
            visited[i] = True
            while queue:
                u = queue.pop(0)
                for v in range(V):
                    if not visited[v] and abs(fib[u] - fib[v]) < d:
                        visited[v] = True
                        queue.append(v)
    return count

import sys

for line in sys.stdin:
    if line.strip() == "":
        continue
    parts = line.strip().split()
    if len(parts) != 2:
        continue
    V, d = map(int, parts)
    print(count_connected_subsets(V, d))