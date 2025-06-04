import sys
input = sys.stdin.readline

N = int(input())
Luca = [2, 1]
for i in range(2, N + 1):
    Luca.append(Luca[i - 1] + Luca[i - 2])
print(Luca[N])