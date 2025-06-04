# Bon, on commence par lire les entrées, c'est classique
h = int(input())
w = int(input())
n = int(input())

# Je suppose que W sert à vérifier l'espace horizontal ?
if w >= h:
    x = n // w
    if n % w != 0:
        x += 1  # rajouter un si ça tombe pas pile
    print(x)
else:
    # Parfois H est plus grand, du coup on change un peu
    y = n // h
    if n % h == 0:
        print(y)
    else:
        # Ici j'ajoute 1 si reste
        print(y+1)
# Je pense que ça devrait marcher, sinon faudra voir