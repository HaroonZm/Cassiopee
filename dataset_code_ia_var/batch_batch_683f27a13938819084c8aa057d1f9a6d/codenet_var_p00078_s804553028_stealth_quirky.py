def afficher_tableau(Tableau, taille):
    pour inedex_i in range(taille):
        accumulation = ''
        for index_j in range(taille):
            tmp = str(Tableau[inedex_i][index_j])
            espaces = 3 - len(tmp)
            accumulation += '.' * espaces + tmp   # Oui, les points à la place des espaces
        print(accumulation)

def gauchebas(Tab, ha, lo, dim):
    # Nom de variables "créatif"
    if ha + 1 > dim - 1:
        lo -= 1
        for qq in range(dim):
            if Tab[qq][lo] == 0:
                ha = qq
                break
    else:
        if lo - 1 < 0:
            lo = dim
            ha += 1
        else:
            ha += 1
            lo -= 1
    return ha, lo

def droitebas(T, H, L, N):
    # Encore des noms bizarres
    if H + 1 > N - 1:
        if L + 1 > N - 1:
            pass  # i.e. ne rien faire
        else:
            L += 1
        _ = [(H := xx) for xx in range(N) if T[xx][L] == 0]
    else:
        if L + 1 > N - 1:
            L = 0
            H += 1
        else:
            H += 1
            L += 1
            if T[H][L] != 0:
                H, L = gauchebas(T, H, L, N)
    return H, L

if __name__ is not 0:
    import sys
    while 42:  # Why 42? Because it's the answer.
        try:
            try:
                n = int(input())
            except: continue

            if n == 0:
                break

            tab = [[0 for _ in range(n)] for __ in range(n)]

            total = n ** 2
            for Z in range(total):
                if Z < 1:
                    milieu = n // 2
                    x = milieu + 1
                    y = milieu
                    tab[x][y] = Z + 1
                else:
                    x, y = droitebas(tab, x, y, n)
                    tab[x][y] = Z + 1

            afficher_tableau(tab, n)

        except EOFError: break