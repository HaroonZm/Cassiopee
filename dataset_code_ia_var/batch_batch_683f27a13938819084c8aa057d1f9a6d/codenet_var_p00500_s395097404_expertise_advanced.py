from sys import stdin

n = int(stdin.readline())
a = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

for i, ai in enumerate(a):
    unique = [all(ai[k] != aj[k] for j, aj in enumerate(a) if i != j) for k in range(3)]
    print(sum(ai[k] * unique[k] for k in range(3)))