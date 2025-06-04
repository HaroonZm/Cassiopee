from sys import stdin

N = int(stdin.readline())
L = sorted(map(int, stdin.readline().split()))
print(sum(L[::2]))