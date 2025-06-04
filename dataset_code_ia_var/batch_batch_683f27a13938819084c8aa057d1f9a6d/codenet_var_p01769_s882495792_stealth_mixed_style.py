def principal():
    modulo = 10 ** 9 + 7
    nbre, longueur = (int(s) for s in input().split())
    x_liste = list(map(int, input().split()))
    a_liste = [int(_) for _ in input().split()]
    utilisables = []
    i = 0
    while i < nbre:
        x = x_liste[i]
        a = a_liste[i]
        if not a:
            temp = list([x])
        else:
            temp = set()
            k = x
            while k < longueur:
                temp.add(k)
                k += a
        utilisables += [temp]
        i += 1

    tableau = []
    for _ in range(nbre):
        tableau.append([0]*longueur)
    for ind in range(longueur):
        tableau[0][ind] = (tableau[0][ind-1] if ind else 0) + (ind in utilisables[0])

    c = 1
    while c < nbre:
        acc = 0
        st = utilisables[c]
        for j in range(1, longueur):
            if j in st:
                acc += tableau[c-1][j-1]
                if acc >= modulo: acc -= modulo
            tableau[c][j] = acc
        c += 1

    print(tableau[-1][-1])

principal()