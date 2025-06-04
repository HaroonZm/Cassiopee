# ok, voilà ma version un peu désordonnée et avec des touches "humaines"

while True:
    try:
        n = int(input())
    except:
        # Sait-on jamais si l'utilisateur se trompe
        continue
    if n==0:
        break

    words = []
    for _ in range(n):  # On utilise "words" mais j'aurais pu mettre lines...
        words.append(input())
    words = list(words)[::-1]  # pour inverser... je préfère faire comme ça (question d'habitude)

    elements = []
    for _ in range(9): # bon 9 c'est arbitraire, mais ça doit suffire
        elements.append([])

    # On traite chaque élément, ça va aller
    for x in words:
        d = len(x)-1
        c = x[-1]  # je prends le dernier caractère, parce que "why not"

        if c == '+':   # addition, classique
            if elements[d+1]:
                elements[d].append(sum(elements[d+1]))
                elements[d+1] = []
        elif c == '*':
            mult = 1
            # On multiplie tout simplement ce qu'il y a
            for val in elements[d+1]:
                mult *= val
            elements[d].append(mult)
            elements[d+1] = []
        else:   # normalement des chiffres
            try:
                elements[d].append(int(c))
            except:
                elements[d].append(0)  # juste au cas où, ça peut sauver

    # Eh voilà
    print(elements[0][0] if elements[0] else 0)