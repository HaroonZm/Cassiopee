def sieve():
    # Définition de la limite supérieure pour le crible
    L = 1299710  # La variable L représente la limite supérieure (exclue) pour notre recherche de nombres premiers

    # Initialisation d'une liste vide pour stocker les nombres premiers trouvés
    primes = []

    # Création d'une liste booléenne pour déterminer si un indice représente un nombre premier.
    # La liste isPrime a une longueur de L. Chaque élément est initialisé à True.
    # Cela suppose que tous les nombres sont premiers au départ (vrai).
    isPrime = [True for _ in range(L)]
    # La compréhension de liste ci-dessus itère du nombre 0 à (L-1) et met True pour chaque élément.

    # On commence la recherche de nombres premiers à partir de 2, car 0 et 1 ne sont pas premiers.
    for i in range(2, L):
        # On vérifie si i est encore marqué comme premier
        if isPrime[i]:
            # Si c'est le cas, alors i est un nombre premier, on l'ajoute à la liste des nombres premiers
            primes.append(i)

            # On va maintenant marquer tous les multiples de i comme non premiers (faux).
            # On commence à i*i, car tout multiple plus petit de i a déjà été traité.
            # On va jusqu'à L (exclu), avec un pas de i.
            for j in range(i * i, L, i):
                isPrime[j] = False  # On marque ce nombre comme non premier
                # Cela signifie que tout nombre entre i*i et L, incrementé de i, ne peut pas être premier

    # On retourne la liste complète des nombres premiers trouvés
    return primes

def getPrimeGap(num, primes):
    # Cette fonction permet de calculer l'écart ("gap") entre deux nombres premiers autour de 'num'
    # Si 'num' est dans la liste des nombres premiers, l'écart est 0

    if num in primes:
        # Vérifie si le nombre donné est déjà un nombre premier
        return 0  # Si oui, il n'y a pas d'écart

    # On parcourt les indices de la liste des nombres premiers jusqu'à l'avant-dernier élément
    # On choisit 100000 - 1, car on utilisera primes[i + 1] dans la boucle
    for i in range(100000 - 1):
        # On cherche l'intervalle [primes[i], primes[i + 1]] autour de 'num'
        # Si primes[i] est plus petit que 'num' et primes[i + 1] est plus grand que 'num', alors on a trouvé nos bornes
        if primes[i] < num and primes[i + 1] > num:
            # On retourne la différence entre les deux bornes,
            # qui donne l'écart des premiers autour de 'num'
            return primes[i + 1] - primes[i]

# Point d'entrée du programme. Ceci s'assure que le code suivant ne s'exécute que si le fichier est exécuté directement.
if __name__ == '__main__':
    # On génère une liste de nombres premiers à l'aide de la fonction 'sieve'
    primes = sieve()

    # On démarre une boucle infinie qui ne s'arrêtera que si on reçoit une entrée spéciale
    while True:
        # On lit une ligne depuis l'entrée standard et on la convertit en entier
        num = int(input())

        # Si l'utilisateur entre 0, on quitte la boucle, donc on arrête le programme
        if num == 0:
            break

        # Sinon, on utilise la fonction getPrimeGap pour calculer et afficher l'écart entre nombres premiers
        print(getPrimeGap(num, primes))