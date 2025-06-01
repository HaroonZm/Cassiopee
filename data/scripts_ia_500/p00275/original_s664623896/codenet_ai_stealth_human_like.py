while True:
    n = int(input())  # on attend un nombre
    if n == 0:
        break
    s = raw_input()  # la chaine de caractères suivante
    ba = 0
    p = [0 for _ in range(n)]  # initialiser la liste p
    for i in range(100):  # on boucle 100 fois, pas très flexible mais bon
        if s[i] == 'M':
            p[i % n] += 1
        elif s[i] == 'L':
            p[i % n] += ba + 1
            ba = 0  # reset ba ici
        else:
            ba += p[i % n] + 1
            p[i % n] = 0
    # voilà le résultat trié, un truc un peu étrange mais c'est ce que j'ai compris
    print " ".join(str(x) for x in sorted(p)), str(ba)