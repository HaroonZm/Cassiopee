import math

while True:
    n = int(raw_input())
    if n == 0:
        break
    A = raw_input().split()
    A = [int(x) for x in A]
    E = []
    D = []
    for a in A:
        if a % 2 == 0:
            E.append(a)
        else:
            D.append(a)
    E.sort()
    D.sort()

    g = 2
    el = E[0]
    for i in range(100):
        if (el >> i) % 2:
            g = g ** i
            break
    newE = []
    for e in E:
        newE.append(e / g)
    E = newE

    k1 = int(math.sqrt(D[0]*E[0]/E[1]))
    ga = E[0] / k1

    for i in range(len(E)):
        E[i] = E[i] / ga

    print int(g * ga)
    E_int = []
    for e in E:
        E_int.append(int(e))
    print " ".join([str(x) for x in E_int])