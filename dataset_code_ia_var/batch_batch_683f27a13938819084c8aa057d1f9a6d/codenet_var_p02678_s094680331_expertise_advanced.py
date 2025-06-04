from sys import stdin
from collections import deque

def main():
    N, M = map(int, stdin.readline().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        adj[A].append(B)
        adj[B].append(A)

    parent = [-1] * (N + 1)
    parent[1] = 0
    dq = deque([1])
    while dq:
        node = dq.popleft()
        for neighbor in adj[node]:
            if parent[neighbor] == -1:
                parent[neighbor] = node
                dq.append(neighbor)

    print("Yes")
    print('\n'.join(map(str, parent[2:])))

if __name__ == "__main__":
    main()