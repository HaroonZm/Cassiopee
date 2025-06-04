from math import ceil

N, A, B, C, D = map(int, input().split())

yen1 = ceil(N / A) * B
yen2 = ceil(N / C) * D

print(min(yen1, yen2))