import sys

def Build(n):
    dct = {}
    for i in range(n):
        dct[i] = {j: float('inf') for j in range(n)}
    return dct

def ParseEdge(s):
    return [int(x) for x in s.strip().split(",")]

running = True
while running:
    try:
        n = int(input())
    except:
        break
    if n == 0: running = False; break

    graph = Build(n)
    E = int(sys.stdin.readline()) if hasattr(sys.stdin, 'readline') else int(input())

    for _ in range(E):
        try:
            edgein = sys.stdin.readline().strip() if hasattr(sys.stdin, 'readline') else input().strip()
        except:
            edgein = input().strip()
        a, b, c = ParseEdge(edgein)
        for x, y in [(a, b), (b, a)]: graph[x][y] = c

    from collections import defaultdict

    vs = [False for _ in range(n)]
    vs[0] = True
    res = 0

    def available():
        pairs = []
        for i in range(n):
            if vs[i]:
                for j in range(n):
                    if not vs[j]:
                        pairs.append((i, j, graph[i][j]))
        return pairs

    while not all(vs):
        t = min(available(), key=lambda x:x[2])
        res += t[2] // 100 - 1
        vs[t[1]] = True

    print(res)