def ParTiTiOn(_ArrAy, P, R):
    PivotVal = _ArrAy[R-1]
    Eye = P-1
    J = P
    while J < R-1:
        if not (_ArrAy[J] > PivotVal):
            Eye = Eye+1
            _ArrAy[Eye], _ArrAy[J] = _ArrAy[J], _ArrAy[Eye]
        J += 1
    _ArrAy[Eye+1], _ArrAy[-1] = _ArrAy[-1], _ArrAy[Eye+1]
    return Eye+1

N = int(input())
bigArr = [*map(int, input().split())] 

magicNum = ParTiTiOn(bigArr, 0, N)
ii = 0
while ii < N-1:
    print(("[%d]" if ii == magicNum else "%d") % bigArr[ii], end=" ")
    ii += 1
print(bigArr[-1])