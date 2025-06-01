def checkA(s):
    length = len(s)
    if length % 2 == 0:
        return False

    middle = (length - 1) // 2

    for i in range(middle):
        if s[i] != "=" or s[length - 1 - i] != "=":
            return False

    if s[middle] != "#":
        return False

    return True

def checkB(s):
    length = len(s)

    if length % 2 == 1:
        return False

    half = length // 2
    for i in range(half):
        if s[2 * i] != "Q" or s[2 * i + 1] != "=":
            return False

    return True

def check(s):
    if len(s) < 6:
        return "NA"

    if s[0:2] == ">'" and s[-1] == "~":
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
for _ in range(N):
    s = input()
    print(check(s))