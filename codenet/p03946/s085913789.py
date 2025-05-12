def 解():
    iN,iT = [int(_) for _ in input().split()]
    aA = [int(_) for _ in input().split()]
    iL = len(aA)

    aMaxD = [0]
    iMin = aA[0]
    iV = 0

    def checkMax(aMaxD,iMaxD):
        if aMaxD[0] < iMaxD:
            aMaxD = [iMaxD]
        elif aMaxD[0] == iMaxD:
            aMaxD.append(iMaxD)
        return aMaxD

    iB = aA[0]
    for iN in aA[1:]:
        if iB - iN > 0:
            if iV >= 0:
                aMaxD = checkMax(aMaxD,iB-iMin)
            iV = -1
        elif iB - iN < 0:
            if iV <= 0:
                iMin = min(iB,iMin)
            iV = 1
        iB = iN
    aMaxD = checkMax(aMaxD,aA[-1] - iMin)
    print( len(aMaxD) )
解()