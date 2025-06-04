# Démarrer une boucle infinie qui ne s'arrêtera que si une certaine condition de sortie est remplie
while True:
    # Lire une ligne de l'entrée standard, la diviser en trois entiers, puis affecter à m, nMin, nMax
    # map permet d'appliquer la fonction 'int' à chaque partie de la ligne obtenue par input().split() (qui coupe la ligne en morceaux)
    m, nMin, nMax = map(int, input().split())
    
    # Vérifier si toutes les valeurs d'entrée sont nulles,
    # ce qui indique la condition d'arrêt du programme
    if m == 0 and nMax == 0 and nMin == 0:
        # Quitter la boucle infinie et donc arrêter le programme
        break

    # Initialiser une liste vide 'P' pour stocker des entiers
    P = []
    # Initialiser une variable 'Max' à 0, elle servira à garder la différence maximale trouvée
    Max = 0
    # Initialiser une variable 'ans' à 0, elle représentera la meilleure valeur de n à afficher
    ans = 0

    # Boucle sur 'm' rangs, où chaque itération va lire un entier et l'ajouter à la liste 'P'
    for i in range(m):
        # Lire un entier via input (l'utilisateur doit saisir un entier à chaque itération)
        nombre_lu = int(input())
        # Ajouter l'entier lu à la liste 'P' à l'aide de la méthode append
        P.append(nombre_lu)
    else:
        # Après la lecture des m entiers, effectuer une nouvelle boucle pour trouver la valeur de n optimale
        # Le nombre d'itérations est (nMax - nMin + 1), car nous analysons tous les indices de n dans cet intervalle inclusif
        for i in range(nMax - nMin + 1):
            # Pour chaque 'i', on considère n = nMin + i, qui parcourt toutes les valeurs de n entre nMin et nMax inclus
            # Si nous sommes à la première itération (i == 0) ou si la valeur Max jusqu'ici est inférieure ou égale à la nouvelle différence calculée
            # entre P[nMin + i - 1] et P[nMin + i], alors on met à jour Max et ans
            if i == 0 or Max <= P[nMin + i - 1] - P[nMin + i]:
                # Mettre à jour Max pour stocker la nouvelle différence maximale trouvée à cette itération
                Max = P[nMin + i - 1] - P[nMin + i]
                # Mettre à jour 'ans' pour mémoriser la valeur actuelle de n (où la différence maximale a lieu)
                ans = nMin + i
        else:
            # Lorsque la boucle sur les valeurs de n est terminée, afficher la valeur optimale trouvée
            print(ans)