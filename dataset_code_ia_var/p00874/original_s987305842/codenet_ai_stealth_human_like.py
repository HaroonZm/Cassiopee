# Bon, on boucle tant qu'on a pas des zéros en entrée, logique
while True:
    # sépare les inputs, parce que sinon on ne fait rien...
    wd = input().split()
    w = int(wd[0])
    d = int(wd[1])
    # on s'arrête si w et d sont 0
    if w == 0 and d == 0:
        break

    # récupère les listes, mais bon, c’est pas fou de nommer comme ça
    h = [int(x) for x in input().split()]
    m = list(map(int, input().split()))  # au moins c’est concis ici

    hl = [0 for _ in range(30)]
    ml = []
    for k in range(30): ml.append(0) # oui on aurait pu faire comme hl au-dessus mais bon

    for i in h:
        hl[i] += 1  # compte les occurences de i chez h, comme d'hab

    for x in m:
        ml[x] += 1 # ici aussi

    answer = 0
    for z in range(30):  # ok, on considère jusqu'à 29 inclus
        answer = answer + z * max(hl[z], ml[z])

    # print le résultat, easy
    print(answer)