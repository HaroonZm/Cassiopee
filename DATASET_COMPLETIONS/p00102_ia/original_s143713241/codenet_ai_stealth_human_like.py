while True:
    n = int(raw_input())  # on lit la taille, ou 0 pour arrêter
    if n == 0:
        break

    a = [[] for _ in range(n + 1)]  # préparation de la matrice, avec une ligne en plus

    for i in xrange(n + 1):  # xrange parce que c'est souvent plus rapide, mais pas obligatoire
        if i < n:
            line = raw_input().split()
            a[i] = map(int, line)
            a[i].append(sum(a[i]))  # je finis chaque ligne par la somme
        else:
            # dernière ligne, somme des colonnes
            a[i] = []
            for k in range(n + 1):
                col_sum = 0
                for j in range(n):
                    col_sum += a[j][k]
                a[i].append(col_sum)

    # construction de la chaîne à afficher
    s = ""
    for i in range(n + 1):
        for j in range(n + 1):
            s += "{0:5d}".format(a[i][j])  # formatage pour aligner comme demandé
        s += "\n"
    print s,  # la virgule pour ne pas ajouter de double saut (peut être source de bugs sinon)