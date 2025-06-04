while True:
    N = int(input())
    if N == 0:
        break

    parent = {}
    diff = {}

    def find(x):
        if parent[x] != x:
            orig = parent[x]
            parent[x] = find(parent[x])
            diff[x] += diff[orig]
        return parent[x]

    def union(x, y, val):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return diff[x] - diff[y] == val
        parent[ry] = rx
        diff[ry] = diff[x] - diff[y] - val
        return True

    pairs = []
    inconsistent = False
    for _ in range(N):
        line = input()
        # "1 A = 10^x B"
        parts = line.split()
        A = parts[1]
        x_str = parts[3]
        x = int(x_str.split('^')[1])
        B = parts[4]

        if A not in parent:
            parent[A] = A
            diff[A] = 0
        if B not in parent:
            parent[B] = B
            diff[B] = 0

        # Check union, if inconsistent found, record it
        if not union(A, B, x):
            inconsistent = True

    print("No" if inconsistent else "Yes")