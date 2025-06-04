from math import ceil

N, A, B, C, D = map(int, input().split())

X = ceil(N / A) * B
Y = ceil(N / C) * D

print(min(X, Y))