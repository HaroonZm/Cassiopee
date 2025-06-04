from sys import stdin

N, L = map(int, stdin.readline().split())
print(''.join(sorted((stdin.readline().strip() for _ in range(N)))))