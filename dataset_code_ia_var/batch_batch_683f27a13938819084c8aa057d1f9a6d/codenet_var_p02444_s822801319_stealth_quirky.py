from copy import deepcopy as dc

N=int(input())
A=[*map(int,input().split())]

ZZ=dc(A)
Q=int(input())
for ignore in '_'*Q:
    BB,MM,EE=[int(x) for x in input().split()]
    for NN in range(EE-BB):
        whereto = BB + (NN + EE - MM) % (EE - BB)
        ZZ[whereto]=A[NN+BB]
    A=dc(ZZ)

print(*A)