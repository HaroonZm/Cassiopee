NAB = input().split()
N = int(NAB[0])
A = int(NAB[1])
B = int(NAB[2])
if N * A < B:
    print(N * A)
else:
    print(B)