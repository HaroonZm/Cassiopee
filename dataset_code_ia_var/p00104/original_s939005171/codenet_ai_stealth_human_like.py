# Ok, alors voici une version un peu plus "humaine", avec mes petits commentaires
while True:
    # On récupère les dimensions
    dims = raw_input().split()
    h = int(dims[0])
    w = int(dims[1])
    # Test de sortie
    if h == 0 and w == 0:
        break

    # Lecture de la room
    room = []
    for n in range(h):
        line = raw_input()
        room.append([c for c in line])  # on stocke les caractères

    x = 0
    y = 0
    # quelques petites subtilités dans l'algo
    while True:
        c = room[y][x]
        room[y][x] = '*'
        # Faut avouer que tout ça, c'est un peu bourrin...
        if c == '>':
            x += 1
        elif c == '<':
            x = x - 1
        elif c == 'v':
            y = y + 1
        elif c == '^':
            y = y - 1
        elif c == '.':
            print x, y # on a trouvé la sortie
            break
        else:
            # Franchement je comprends pas comment on peut boucler ici, mais bon
            print 'LOOP'
            break
# c'est pas parfait tout ça mais ça devrait tourner !