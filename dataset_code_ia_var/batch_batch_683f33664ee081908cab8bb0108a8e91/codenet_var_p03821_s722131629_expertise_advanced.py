from sys import stdin

N = int(stdin.readline())
pairs = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

count = 0
for a, b in reversed(pairs):
    mod = (count + a) % b
    if mod:
        count += b - mod

print(count)