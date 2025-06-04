def checkA(s):

    l = len(s)
    if l % 2 == 0:
        return False

    ll = (l-1)//2

    for i in range(ll):
        if s[i] != "=" or s[l-1-i] != "=":
            return False

    if s[ll] != "#":
        return False

    return True

def checkB(s):
    l = len(s)

    if l % 2 == 1:
        return False

    ll = l // 2
    for i in range(ll):
        if s[2*i] != "Q" or s[2*i+1] != "=":
            return False

    return True

def check(s):
    if len(s) < 6:
        return "NA"

    if s[0:2] == ">'" and s[-1:] == "~":
        if checkA(s[2:-1]):
            return "A"
        else:
            return "NA"

    if s[0:2] == ">^" and s[-2:] == "~~":
        if checkB(s[2:-2]):
            return "B"
        else:
            return "NA"

    return "NA"

N = int(input())

for i in range(N):
    s = input()
    print(check(s))