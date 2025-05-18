from itertools import product
"""
-> は @と表記する
"""

variables = set(list("abcdefghijk"))

def formula(S, X, i):
    if S[i] == "T":
        return 1, i+1
    elif S[i] == "F":
        return 0, i+1
    elif S[i] in variables:
        return X[S[i]], i+1
    elif S[i] == "-":
        i += 1
        that, i = formula(S, X, i)
        return (not that), i
    else:
        i += 1
        this, i = formula(S, X, i)
        op = S[i]
        i += 1
        that, i = formula(S, X, i)
        i += 1

        if op == "*":
            return this&that, i
        elif op == "+":
            return this|that, i
        elif op ==  "@":
            return (not this)|that, i
        else:
            raise

S = input()
T, F = 1, 0
while S != "#":
    S = S.replace("->", "@")
    while "--" in S:
        S = S.replace("--", "")
    L, R = S.split("=")
    for v in range(2**11):
        X = {}
        for a, x in zip(list("abcdefghijk"), format(v, "b").zfill(11)):
            X[a] = int(x)
        l, _ = formula(L, X, 0)
        r, _ = formula(R, X, 0)
        if int(l) != int(r):
            print("NO")
            break
    else:
        print("YES")
    S = input()