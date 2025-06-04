import sys
import threading

def main():
    sys_setrecursionlimit = sys.setrecursionlimit
    sys_setrecursionlimit(1 << 25)
    buf = sys.stdin.buffer
    readline = buf.readline
    read = buf.read

    N = int(readline())
    data = list(map(int, read().split()))

    A = []
    B = []
    for i in range(0, N + N - 2, 2):
        A.append(data[i])
    for i in range(1, N + N - 2, 2):
        B.append(data[i])

    INF = 10 ** 18 + 100
    S = [INF]
    for v in data[-N:]:
        S.append(v)

    graph = []
    for _ in range(N + 1):
        graph.append([])
    for i in range(N - 1):
        a = A[i]
        b = B[i]
        graph[a].append(b)
        graph[b].append(a)

    m = min(S)
    root = 0
    for i in range(N + 1):
        if S[i] == m:
            root = i
            break

    parent = [0] * (N + 1)
    order = []
    stack = [root]
    while len(stack):
        x = stack.pop()
        order.append(x)
        for y in graph[x]:
            if y == parent[x]:
                continue
            parent[y] = x
            stack.append(y)

    subtree_size = [1] * (N + 1)
    for i in range(len(order) - 1, -1, -1):
        v = order[i]
        subtree_size[parent[v]] += subtree_size[v]

    length = [0] * (N + 1)
    for i in range(N - 1):
        v = A[i]
        p = B[i]
        if parent[p] == v:
            v, p = p, v
        s = subtree_size[v]
        d = N - s - s
        if d == 0:
            length[v] = 0
        else:
            length[v] = (S[v] - S[p]) // d

    dist = [0] * (N + 1)
    for i in range(1, len(order)):
        v = order[i]
        p = parent[v]
        dist[v] = dist[p] + length[v]

    d_root = 0
    for v in dist:
        d_root += v
    x = (S[root] - d_root) * 2 // N

    answer = []
    for i in range(N - 1):
        v = A[i]
        p = B[i]
        if parent[p] == v:
            v, p = p, v
        if length[v] == 0:
            length[v] = x
        answer.append(length[v])

    for v in answer:
        print(v)

threading.Thread(target=main,).start()