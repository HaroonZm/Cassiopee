# Bon, on commence une boucle "éternelle", mais ça marchera
while 1:
    # on récupère H et W... j'espère que l'utilisateur entre bien deux entiers !
    hw = input().split()
    h = int(hw[0])
    w = int(hw[1])
    # si tout est fini, bah... on sort
    if h == 0 and w == 0:
        break
    
    # ok, maintenant on lit nos tuiles
    T = []
    # je fais une boucle normale ici
    for ligne in range(h):
        T.append(input())
    # position de départ au coin et un petit
    x = y = 0; moves = 0
    
    while True:
        tuile = T[x][y]
        if moves > h * w:  # à force, je suppose que ça boucle...
            print("LOOP")
            break
        
        # Guider le robot, selon la flèche trouvée
        if tuile == ">":
            if y+1 < w:
                y += 1
            else:
                # on est sorti à droite ?
                print(y, x)
                break
        elif tuile == "<":
            if y > 0:
                y -= 1
            else:
                print(y, x)
                break
        elif tuile == "^":
            if x > 0:
                x -= 1
            else:
                print(y, x)
                break
        elif tuile == "v":
            if x+1 < h:
                x += 1
            else:
                print(y, x)
                break
        else:
            # bon, je suppose que si c'est pas une flèche, on s'arrête ici
            print(y, x)
            break
        moves += 1  # je pense à incrémenter ici mais pas avant...