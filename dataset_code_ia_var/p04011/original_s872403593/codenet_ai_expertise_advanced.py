from sys import stdin

N, K, X, Y = (int(x) for x in (stdin.readline(), stdin.readline(), stdin.readline(), stdin.readline()))

print(N * X if N <= K else K * X + (N - K) * Y)