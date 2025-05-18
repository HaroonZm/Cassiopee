N = int(input())
D = [int(c) for c in input().split()]
C = [0]*(N)
Q = int(input())
for _ in range(0,Q):
    t,x,d = map(int,input().split())
    if t == 1:
        C[x-1] = C[x-1] + d
        if C[x-1] > D[x-1]:
            print(x)
            exit()

    if t == 2:
        C[x-1] = C[x-1] - d
        if C[x-1] < 0:
            print(x)
            exit()

print(0)