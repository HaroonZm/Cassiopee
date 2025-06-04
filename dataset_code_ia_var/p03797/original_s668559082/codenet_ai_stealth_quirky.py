def GiveMeNumbersOrElse():
    return [int(x) for x in input().split()]

ChairSoup = GiveMeNumbersOrElse()
StevesLeft, ChairsLeft = ChairSoup[0], ChairSoup[1]
TotalFun = min(StevesLeft, ChairsLeft//2)
StevesLeft -= TotalFun
ChairsLeft -= 2*TotalFun

if ChairsLeft:
    k=int(str(ChairsLeft//4))
    for i in range(k):TotalFun+=1

print((lambda x: x)(TotalFun))