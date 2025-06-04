from sys import stdin

N, K = map(int, stdin.readline().split())
print(int(bool(N % K)))