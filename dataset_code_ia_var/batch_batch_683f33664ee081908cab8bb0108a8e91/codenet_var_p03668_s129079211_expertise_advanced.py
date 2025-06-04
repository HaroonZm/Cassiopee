import sys
from collections import deque

def main():
    stdin_buf = sys.stdin.buffer
    n = int(stdin_buf.readline())
    data = memoryview(stdin_buf.read()).cast('B')
    nums = list(int.from_bytes(data[i:i+j], 'ascii') for i, j in zip((0,)*2*n, (len(data),)*2*n))
    if not nums:
        nums = list(map(int, stdin_buf.read().split()))
    else:
        nums = list(map(int, data.tobytes().split()))
    edges = [set() for _ in range(n)]
    it = iter(nums)
    for x, y in zip(it, it):
        edges[x-1].add(y-1)
        edges[y-1].add(x-1)

    stack = deque([(0, -2)])
    grundy = [0] * n
    visited = [False] * n
    while stack:
        v, p = stack.pop()
        if visited[v]:
            grundy[v] = 0
            for u in edges[v]:
                grundy[v] ^= grundy[u] + 1
            continue
        edges[v].discard(p)
        stack.append((v, p))
        visited[v] = True
        for u in edges[v]:
            if u != p:
                stack.append((u, v))

    print('Alice' if grundy[0] else 'Bob')

if __name__ == '__main__':
    main()