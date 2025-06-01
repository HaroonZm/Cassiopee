def a1(li):
    if 100 in li:
        return 1
    else:
        return 0

def a2(li):
    average = (li[0] + li[1]) / 2
    if average >= 90:
        return 1
    else:
        return 0

def a3(li):
    average = sum(li) / 3
    if average >= 80:
        return 1
    else:
        return 0

def isA(li):
    if a1(li) == 1 or a2(li) == 1 or a3(li) == 1:
        return 1
    else:
        return 0

def b1(li):
    average = sum(li) / 3
    if average >= 70:
        return 1
    else:
        return 0

def b2(li):
    average = sum(li) / 3
    if average >= 50 and (li[0] >= 80 or li[1] >= 80):
        return 1
    else:
        return 0

def isB(li):
    if b1(li) == 1 or b2(li) == 1:
        return 1
    else:
        return 0

def isX(li):
    if isA(li) == 1:
        return 'A'
    elif isB(li) == 1:
        return 'B'
    else:
        return 'C'

while True:
    N = int(input())
    if N == 0:
        break
    for i in range(N):
        l = list(map(int, input().split()))
        print(isX(l))