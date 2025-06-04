import sys

sys.setrecursionlimit(10**7)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot == yroot:
        return False
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1
    return True

def main():
    input = sys.stdin.readline
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        edges = []
        for _ in range(m):
            a, b, cost = map(int, input().split())
            edges.append((cost, a, b))
        edges.sort()
        parent = [i for i in range(n)]
        rank = [0]*n
        total_cost = 0
        for cost, a, b in edges:
            if union(parent, rank, a, b):
                total_cost += cost
        print(total_cost)

if __name__ == "__main__":
    main()