from sys import stdin

N = int(stdin.readline())
Ls = sorted(map(int, stdin.readline().split()))

print(sum(Ls[i] for i in range(0, N, 2)))