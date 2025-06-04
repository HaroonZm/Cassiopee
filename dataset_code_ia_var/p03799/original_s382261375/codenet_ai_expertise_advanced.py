from sys import stdin
S, c = map(int, stdin.readline().split())
print(S + (c - 2*S) // 4 if 2 * S < c else c // 2)