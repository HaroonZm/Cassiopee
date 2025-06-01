from sys import stdin
W = list(range(1, int(stdin.readline()) + 1))
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split(','))
    W[a-1], W[b-1] = W[b-1], W[a-1]
print(*W, sep='\n')