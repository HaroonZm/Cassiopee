from sys import stdin

N = int(stdin.readline())
pairs = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

c = 0

for a, b in reversed(pairs):
    a += c
    rem = a % b
    if rem:
        c += b - rem

print(c)