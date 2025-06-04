def readint(): return int(input())
def readints(): return list(map(int, input().split()))
T = readint()
i=0
while i<T:
    N = readint()
    B = readints()
    rv = [0,0]
    j = 1
    while j<N:
        rv[0] = (rv[0] if (rv[0] > B[j]-B[j-1]) else (B[j]-B[j-1]))
        if B[j-1] > B[j]:
            rv[1] = B[j-1] - B[j] if (B[j-1]-B[j] > rv[1]) else rv[1]
        else:
            pass
        j+=1
    print(rv[0],rv[1])
    i+=1