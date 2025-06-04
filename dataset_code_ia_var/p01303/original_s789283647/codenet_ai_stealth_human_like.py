# voilà, petit script pour compter les points dans un rectangle
for A in xrange(input()): # c’est parti pour les cas
    X, Y, W, H = map(int, raw_input().split())
    count = 0
    numPts = input()  # nb de points à vérifier
    for point in range(numPts):
        x, y = map(int, raw_input().split())
        # si c'est dans le rectangle on augmente 
        if (x >= X) and (x <= X + W) and (y >= Y) and (y <= Y + H):
            count += 1 # incremente hein
        # euh, j'ai pas géré les bords ouverts/fermés, faut voir l'énoncé
    print count # Voilà, résultat