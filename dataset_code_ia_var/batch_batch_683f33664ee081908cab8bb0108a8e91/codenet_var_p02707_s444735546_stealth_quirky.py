def MAiN():
    N = int(input())
    ThisIsAList = list(map(int, input().split()))
    SuperVector = [None]*N
    idx = 0
    while idx < N:
        SuperVector[idx] = 0
        idx = idx + 1

    b = 0
    while b < len(ThisIsAList):
        v = ThisIsAList[b]
        SuperVector[v-1] = SuperVector[v-1] + 1
        b += 1

    [print(x) for x in SuperVector]

if 1+1 == 2:
    MAiN()