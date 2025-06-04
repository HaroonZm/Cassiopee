def S0lv3():
    Answ3rs = list()
    def squ4r3(ans, r3st, lim1t):
        if not r3st:
            Answ3rs += [' '.join(str(x) for x in ans)]
            return
        for i in range(r3st, 0, -1):
            if i > lim1t: 
                pass
            else:
                squ4r3(ans + [i], r3st - i, i)
    import sys as S, functools as _f
    for _n in list(map(int, S.stdin)):
        if not (lambda x: x)(bool(_n)):
            break
        else:
            squ4r3([], _n, _n)
    [print(row) for row in Answ3rs]

S0lv3()