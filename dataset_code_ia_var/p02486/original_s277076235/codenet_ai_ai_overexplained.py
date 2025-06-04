# Démarre une boucle infinie, qui continuera de s'exécuter jusqu'à ce qu'une instruction 'break' l'interrompe explicitement
while True:
    # Lecture d'une ligne de l'entrée standard (typiquement l'utilisateur) avec raw_input()
    # La méthode raw_input() lit une ligne de texte que l'utilisateur tape et retourne une chaîne de caractères
    # La méthode split() divise la chaîne en une liste de sous-chaînes en découpant là où il y a des espaces
    # map(int, ...) applique la fonction int à chaque élément de la liste, convertissant chaque sous-chaîne en un entier
    # On obtient ainsi deux entiers, n et x
    n, x = map(int, raw_input().split())
    
    # On vérifie si les deux entiers lus sont tous les deux égaux à zéro, ce qui sert de condition d'arrêt
    if n == 0 and x == 0:
        # Si la condition est remplie, on quitte la boucle en utilisant break
        break
    
    # On initialise une variable ans à zéro.
    # Cette variable va servir à compter combien de triplets d'entiers distincts (i, j, k) existent
    # tels que i < j < k et i + j + k == x
    ans = 0
    
    # Première boucle for, où i prend toutes les valeurs possibles de 1 à n inclusivement
    # Cela signifie qu'on va considérer tous les entiers possibles pour i de 1 jusqu'à n
    for i in range(1, n + 1):
        # Deuxième boucle for, où j prend toutes les valeurs possibles de i + 1 à n inclusivement
        # On s'assure alors que j est strictement supérieur à i, garantissant que les indices sont distincts et ordonnés
        for j in range(i + 1, n + 1):
            # Troisième boucle for, où k prend toutes les valeurs possibles de j + 1 à n inclusivement
            # Ainsi, k est strictement supérieur à j, ce qui garantit l'unicité et l'ordre des indices
            for k in range(j + 1, n + 1):
                # On vérifie ici si la somme des trois nombres i, j et k est strictement égale à x
                if i + j + k == x:
                    # Si c'est le cas, on incrémente ans de 1 pour noter qu'on a trouvé un triplet valide
                    ans += 1
    # Affiche le résultat courant (le nombre de triplets trouvés pour cette entrée)
    # La fonction print (sans parenthèses en Python 2) affiche ans à l'écran
    print ans