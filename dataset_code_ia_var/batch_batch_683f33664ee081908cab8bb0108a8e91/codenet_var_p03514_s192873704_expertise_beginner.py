import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.read().split()))

P.sort()

for i in range(len(P)):
    P[i] = P[i] * i

total = sum(P)
answer = total / (len(P) - 1)
print(answer)