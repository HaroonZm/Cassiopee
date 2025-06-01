N, A, B, C, D = input().split()
N = int(N)
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if N % A == 0 and N % C == 0:
    X = (N // A) * B
    Y = (N // C) * D
    if X < Y:
        print(X)
    else:
        print(Y)
elif N % A == 0 and N % C != 0:
    X = (N // A) * B
    Y = ((N // C) + 1) * D
    if X < Y:
        print(X)
    else:
        print(Y)
elif N % A != 0 and N % C == 0:
    X = ((N // A) + 1) * B
    Y = (N // C) * D
    if X < Y:
        print(X)
    else:
        print(Y)
else:
    X = ((N // A) + 1) * B
    Y = ((N // C) + 1) * D
    if X < Y:
        print(X)
    else:
        print(Y)