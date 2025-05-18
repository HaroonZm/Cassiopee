# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
Luca = [2, 1]
for i in range(2, N + 1):
    Luca.append(Luca[i-1] + Luca[i-2])
print(Luca[N])