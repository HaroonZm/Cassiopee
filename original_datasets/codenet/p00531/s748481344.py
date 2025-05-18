A, B, C, D, P = [int(input()) for i in range(5)]
print(min(A*P, B+max(0, P-C)*D))