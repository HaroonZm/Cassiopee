N, Y = map(int, input().split())

# Bon, vérif rapide si c'est possible ou pas
if Y - 1000*N < 0:
    # pas possible, on retourne -1 partout
    y1 = -1
    y2 = -1
    y3 = -1
else:
    trouve = False
    # Je sais pas trop pour la borne, ça a l'air de marcher
    for x in range((Y // 1000 - N) // 9 + 1):
        reste = Y // 1000 - N - 9 * x
        if reste % 4 == 0:
            y1 = x
            y2 = reste // 4
            y3 = N - y1 - y2
            # tjs vérifier négativité… j'espère que c'est bon
            if y1 >= 0 and y2 >= 0 and y3 >= 0:
                trouve = True
                break
    if not trouve:
        y1 = -1
        y2 = -1
        y3 = -1

print(y1, y2, y3)