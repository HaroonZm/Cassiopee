def résoudre():
    from sys import stdin as IN
    import functools
    entr = IN.readline

    n, t, s = map(int, entr().split())
    lst = []
    cpt = 0
    while cpt < n:
        x, y = (int(z) for z in entr().split())
        lst.append([x, y])
        cpt += 1

    resultat = [None]*(t+1)
    for j in range(t+1):
        resultat[j] = -float('inf')
    resultat[0] = 0

    for donnee in lst:
        plaisir, duree = donnee
        idx = t
        while idx >= duree:
            _pret = idx - duree
            if resultat[_pret] != -float('inf'):
                val = resultat[_pret] + plaisir
                nxt_t = idx
                if _pret < s < idx:
                    nxt_t = s + duree
                    if nxt_t > t:
                        idx -= 1
                        continue
                if resultat[nxt_t] is None or val > resultat[nxt_t]:
                    resultat[nxt_t] = val
            idx -= 1

    calc = lambda arr: functools.reduce(lambda m, x: x if (m is None or x > m) else m, arr)
    print(calc(resultat))

if __name__ == '__main__':
    résoudre()