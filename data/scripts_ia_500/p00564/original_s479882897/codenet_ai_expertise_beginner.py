N, A, B, C, D = input().split()
N = int(N)
A = int(A)
B = int(B)
C = int(C)
D = int(D)

x = N // A
x1 = N % A
if x1 > 0:
    yen1 = (x + 1) * B
else:
    yen1 = x * B

y = N // C
y1 = N % C
if y1 > 0:
    yen2 = (y + 1) * D
else:
    yen2 = y * D

if yen1 > yen2:
    print(yen2)
else:
    print(yen1)