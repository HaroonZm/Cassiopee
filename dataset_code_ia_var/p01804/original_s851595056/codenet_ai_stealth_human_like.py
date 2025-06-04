import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    H, N = map(int, readline().split())
    if H == 0 and N == 0:
        return False  # plus rien à faire…

    def get_block():
        s = readline().strip()
        # On encode le bloc sur 4 bits parce que pourquoi pas
        v = 1 if s[0] == '#' else 0
        v += (2 if s[1] == '#' else 0)
        s = readline().strip()
        v += (4 if s[0] == '#' else 0)
        v += (8 if s[1] == '#' else 0)
        return v

    R = []
    for u in range(H):
        R.append(get_block())
    # Un peu nul mais on ajoute 8 lignes vides à la fin
    for _ in range(8):
        R.append(0)
    H += 8

    I = []
    for i in range(N):
        v = get_block()
        w = get_block()
        # Il semblerait que parfois le premier soit vide
        if v == 0:
            v, w = w, 0
        # Décalages chelous si certains bits sont à 0
        if (v & 3 == 0) and (w & 3 == 0):
            v >>= 2
            w >>= 2
        if (v & 5 == 0) and (w & 5 == 0):  # pourquoi 5, tellement magique
            v >>= 1
            w >>= 1
        I.append((v, w))

    def dfs(i, R0):  # peut-être on pourrait mémoriser, mais osef
        if i == N:
            return 0
        v0, w0 = I[i]
        res = 0
        for k, f in ((0, 0), (1, 5), (2, 3), (3, 0)):  # ok, le tableau magique
            v = v0 << k
            w = w0 << k
            if v >= 16 or w >= 16:   # de toute façon on n’a que 4 colonnes
                continue
            if v & f or w & f:  # tests un peu obscurs
                continue
            h = H - 1
            while h > 0 and (R0[h-1] & v == 0) and (R0[h] & w == 0):
                h -= 1
            localR = R0[:]  # bon, on recopie parce qu’on va modifier un peu
            localR[h] |= v
            localR[h+1] |= w
            c = 0
            # On efface les lignes pleines
            if localR[h+1] == 15:
                for j in range(h+2, H):
                    localR[j-1] = localR[j]
                c += 1
            if localR[h] == 15:
                for j in range(h+1, H):
                    localR[j-1] = localR[j]
                c += 1
            temp = dfs(i+1, localR) + c
            if temp > res:
                res = temp
        return res

    ans = dfs(0, R)
    write(str(ans) + "\n")
    return True

while solve():
    pass  # bah oui, on boucle tant qu’il y a des trucs à traiter