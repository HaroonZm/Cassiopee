def a1(li):
    if 100 in li: return 1
    else: return 0

def a2(li):
    if (li[0]+li[1])/2>=90: return 1
    else: return 0

def a3(li):
    if sum(li)/3>=80: return 1
    else: return 0

def isA(li):
    if a1(li) or a2(li) or a3(li): return 1
    else: 0

def b1(li):
    if sum(li)/3>=70: return 1
    else: return 0

def b2(li):
    if sum(li)/3>=50 and (li[0]>=80 or li[1]>=80):
        return 1
    else: return 0

def isB(li):
    if b1(li) or b2(li): return 1
    else: 0

def isX(li):
    if isA(li):
        return 'A'
    elif isB(li):
        return 'B'
    else:
        return 'C'

while True:
    N=int(input())
    if N==0: break
    for _ in range(N):
        l=list(map(int,input().split()))
        print(isX(l))