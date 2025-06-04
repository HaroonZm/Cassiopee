import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    while True:
        N, Q = map(int, input().split())
        if N == 0 and Q == 0:
            break

        parent = [0] * (N+1)
        parent[1] = 1
        for i in range(2, N+1):
            p = int(input())
            parent[i] = p

        # DSU structure: for each node, keep the nearest marked ancestor as its parent in DSU
        dsu = list(range(N+1))

        def find(x):
            if dsu[x] != x:
                dsu[x] = find(dsu[x])
            return dsu[x]

        def union(x):
            dsu[x] = find(parent[x])

        # Initially only root (node 1) is marked, so dsu[1] = 1
        # Unmarked nodes have dsu[x] initially pointing to themselves.

        total = 0
        for _ in range(Q):
            op, v = input().split()
            v = int(v)
            if op == 'M':
                # Mark v: union v with its parent in DSU
                union(v)
            else:
                # Q v: print the nearest marked ancestor
                ans = find(v)
                total += ans
        print(total)

if __name__ == '__main__':
    main()