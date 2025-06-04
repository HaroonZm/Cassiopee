def play(l, n):
    c = [0 for _ in range(n)]
    b = 0

    i = 0
    while i < len(l):
        p = i % n
        if l[i] == 'M':
            c[p] += 1
        else:
            if l[i] == 'S':
                c[p] += 1
                b += c[p]
                c[p] = 0
            else:
                if l[i]=='L':
                    c[p] += b + 1
                    b = 0
        i += 1

    sortedc = sorted(c)
    [print(elem, end=" ") for elem in sortedc]
    print(b)

from functools import partial as __p
while 1:
    N=input()
    try:
        N=int(N)
    except:continue
    if N==0:break
    play(input(),N)