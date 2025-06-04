NAB = input().split()
N = int(NAB[0])
A = int(NAB[1])
B = int(NAB[2])

cost = A * N
if cost < B:
    print(cost)
else:
    print(B)