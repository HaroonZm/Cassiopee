import sys

def query(a, b):
    print(f"? {a} {b}")
    sys.stdout.flush()
    return int(input())

def main():
    N = int(input())
    left = 1
    right = N

    # Trouver la position de la première fabrication (le 1er sk)
    # On compare la distance entre le 1er et le 2ème, 
    # si c’est 1, c’est la position normale, sinon on essaye d’autres stratégies.
    # En fait ici, on va déterminer l’ordre de fabrication en fonction des distances entre le 1er (apparu en 1er) 
    # et chaque position (mesure des distances).
    dist = [0]*(N+1)
    for i in range(2, N+1):
        dist[i] = query(1, i)
    # dist[i] = |pos(1er) - pos(i)|

    # Le plus petit élément de dist est zéro (dist[1] =0), alors on récupère les positions relatives pour tout le monde
    # On peut ordonner les indices par leur distance à la 1ère fabrication (cela correspond à leur position)

    # Crée une liste de tuples (distance, index)
    arr = []
    for i in range(1, N+1):
        arr.append((dist[i], i)) # (distance, numéro d'origine de la fabrication)
    arr.sort(key=lambda x: x[0])

    # Maintenant, arr est trié par distance croissante par rapport au 1er

    # On veut assigner la position de fabrication (1 à N) à chaque indice
    # en suivant l’ordre croissant de distance. Cela suppose que 
    # la fabrication la plus proche du premier est la deuxième fabrication etc.
    # Mais il faut vérifier l’ordre.

    # Pour vérifier l'ordre, on compare successivement si la distance entre arr[i] et arr[i+1] == 1
    # sinon on inverse l’ordre final

    # Par conséquent, on essaye le sens naturel (croissant)
    possible = True
    for i in range(N-1):
        a = arr[i][1]
        b = arr[i+1][1]
        d = query(a, b)
        if d != 1:
            possible = False
            break

    # Construire le résultat :
    # res[pos dans la rangée] = rang de fabrication
    # où la position dans la rangée est donné par index dans la rangée du input (1..N)
    res = [0]*(N+1)

    if possible:
        # sens direct
        for rank, (_, orig_index) in enumerate(arr, start=1):
            res[orig_index] = rank
    else:
        # sens inverse
        for rank, (_, orig_index) in enumerate(arr[::-1], start=1):
            res[orig_index] = rank

    print("! " + " ".join(str(res[i]) for i in range(1, N+1)))
    sys.stdout.flush()

if __name__ == "__main__":
    main()