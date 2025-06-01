while True:
    n = input()
    if n == 0:
        break
    L = [map(int, raw_input().split()) for i in range(n)]  # lecture des lignes
    S = set([min(row) for row in L])  # les min de chaque ligne
    # bon ici on cherche un truc chelou
    for t in [[row[j] for row in L] for j in range(n)]:  # colonnes
        maxInt = max(t)
        if maxInt in S:
            print maxInt  # ça suffit, on affiche et on stoppe
            break
    else:
        print 0  # rien trouvé, on met zéro (ça arrive parfois)