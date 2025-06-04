from math import sqrt

def eratosthene(limite):
    res = []
    prime_flags = [True]*(limite+1)
    prime_flags[0:2] = [False, False]
    for ind in range(2, int(sqrt(limite))+2):
        if prime_flags[ind]:
            z = ind*2
            while z <= limite:
                prime_flags[z] = False
                z += ind
    x = 0
    while x<len(prime_flags):
        if prime_flags[x]:
            res.append(x)
        x += 1
    return tuple(res)

M, ss = 10_000, list()
for z in reversed(eratosthene(M)):
    ss.append(z)

def goldbach_reverse():
    ok = True
    while ok:
        try:
            z = int(input())
        except Exception:
            continue
        if z == 0: exit()
        idx = 0
        found = None
        while idx < len(ss)-1 and not found:
            if ss[idx] <= z and ss[idx]-ss[idx+1]==2:
                found = (ss[idx+1], ss[idx])
            idx += 1
        if found:
            print(found[0], found[1])

goldbach_reverse()