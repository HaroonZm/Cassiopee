# Définition de la fonction 'hole' qui prend deux paramètres :
# 'query' : une liste représentant la requête de "trou" (tranche à retirer)
# 'n' : la taille du cube (c'est donc un cube de n x n x n)
def hole(query, n):
    # On récupère le premier élément de 'query', qui indique la direction ("xy", "xz" ou "yz")
    dir = query[0]

    # On convertit les 2 éléments suivants de 'query' en entiers après les avoir décrémentés de 1,
    # car Python utilise des indices à partir de 0 alors que l'énoncé suppose un départ à 1.
    # Cela donne les indices des lignes/colonnes/étages qu'on va retirer.
    [a, b] = [int(x) - 1 for x in query[1:]]

    # Si la direction est "xy" (donc une coupe selon z, à une position x=a et y=b):
    if dir == "xy":
        # On crée une liste, 'ret', où pour chaque valeur de z allant de 0 à n-1 (donc chaque 'niveau'),
        # on calcule l'index linéarisé dans le cube 3D de la case (a, b, z)
        # La formule est basée sur l'ordre z, y, x (première coordonnée variant le plus lentement)
        ret = [b * n + a + z * n ** 2 for z in range(n)]
    # Si la direction est "xz" (donc une coupe selon y, à une position x=a et z=b)
    elif dir == "xz":
        # Pour chaque valeur de y (allant de 0 à n-1), on calcule la case linéarisée (a, y, b)
        ret = [n ** 2 * b + a + y * n for y in range(n)]
    else:
        # Sinon (obligatoirement la direction "yz") (une coupe selon x, à une position y=a, z=b)
        # Pour chaque valeur de x (allant de 0 à n-1), on calcule la case (x, a, b)
        ret = [n ** 2 * b + a * n + x for x in range(n)]
    # On retourne la liste des indices correspondant à la coupe spécifiée par 'query'
    return ret

# Boucle infinie pour traiter plusieurs cas d'entrée jusqu'à ce qu'on rencontre la fin (n==0)
while (1):
    # On lit une ligne sur l'entrée standard et on la découpe en liste, chaque élément étant un nombre entier
    [n, h] = [int(x) for x in raw_input().split()]
    # Si la taille du cube est 0, cela indique qu'il faut arrêter le programme
    if n == 0:
        break
    else:
        # On initialise une liste vide 'bad', qui contiendra tous les indices "troués" qu'on rencontrera
        bad = []
        # On répète la boucle pour chaque "hole" spécifié par l'utilisateur
        for i in range(h):
            # On lit une requête (par ex "xz 2 4"), on la découpe en liste de chaînes
            query = raw_input().split()
            # On appelle la fonction 'hole' sur cette requête et on concatène le résultat à la liste 'bad'
            bad += hole(query, n)
        # On convertit la liste 'bad' en ensemble 'hset' pour éliminer les doublons
        hset = set(bad)
        # On affiche le nombre de cubes qui ne sont pas dans 'hset'
        # c'est-à-dire le nombre total de cubes (n^3) moins le nombre d'indices "troués"
        print n ** 3 - len(hset)