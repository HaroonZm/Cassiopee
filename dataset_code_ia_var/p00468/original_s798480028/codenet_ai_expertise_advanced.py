import sys
from collections import defaultdict

def main():
    readline = sys.stdin.readline

    while True:
        N = int(readline())
        M = int(readline())
        if N == 0 and M == 0:
            break

        adj = defaultdict(set)
        for _ in range(M):
            a, b = map(int, readline().split())
            adj[a].add(b)
            adj[b].add(a)

        count = 0
        one_neighbors = adj[1]
        for i in range(2, N + 1):
            if i in one_neighbors:
                count += 1
                continue
            if one_neighbors & adj[i]:
                count += 1
        print(count)

if __name__ == "__main__":
    main()