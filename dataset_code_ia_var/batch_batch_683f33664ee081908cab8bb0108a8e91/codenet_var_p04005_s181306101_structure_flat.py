A, B, C = map(int, input().split())
tmp = max(A, B, C)
if tmp % 2 == 0:
    print(0)
else:
    print((A * B * C) // tmp)