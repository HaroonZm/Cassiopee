R = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0, ")": 0}
n = int(input())
for _ in range(n):
    L = []
    t = ''
    line = input()[:-1]
    for e in line:
        if e.isdigit():
            t += e
        else:
            if t:
                L.append(t)
                t = ''
            L.append(e)
    if t:
        L.append(t)
    P = []
    S = []
    for i in L:
        if i == "(":
            S.append(i)
        elif i == ")":
            while S[-1] != "(":
                P.append(S.pop())
            S.pop()
        elif i in R:
            while S and R[S[-1]] >= R[i]:
                P.append(S.pop())
            S.append(i)
        else:
            P.append(i)
    while S:
        P.append(S.pop())
    S = []
    for x in P:
        if x in "+-*/":
            b = S.pop()
            a = S.pop()
            S.append(str(int(eval(a + x + b))))
        else:
            S.append(x)
    print(' '.join(S))