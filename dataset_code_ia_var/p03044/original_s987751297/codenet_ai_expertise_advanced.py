from collections import defaultdict, deque
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    neighbor = defaultdict(list)
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        neighbor[u].append((v, w))
        neighbor[v].append((u, w))

    color = [None] * (n + 1)
    color[1] = 0

    stack = [(1, 0)]
    while stack:
        v, accum = stack.pop()
        for u, w in neighbor[v]:
            if color[u] is None:
                color[u] = (accum + w) & 1
                stack.append((u, accum + w))

    print('\n'.join(map(str, color[1:])))

if __name__ == "__main__":
    main()