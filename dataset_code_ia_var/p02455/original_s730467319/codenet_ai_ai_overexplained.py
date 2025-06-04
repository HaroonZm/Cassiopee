# On définit un ensemble vide nommé 'S' pour stocker des entiers uniques
S = set()

# On lit un entier de l'entrée standard, qui représente le nombre total d'opérations à effectuer
n = int(input())

# La boucle 'for' va s'exécuter 'n' fois, c'est-à-dire pour chaque opération à traiter
for i in range(n):
    # On lit une ligne de deux entiers séparés par un espace, on les convertit en entiers et on les assigne à 'q' et 'x'
    q, x = map(int, input().split())
    
    # Si la variable 'q' est égale à 0, cela indique une opération d'ajout
    if q == 0:
        # On vérifie si l'élément 'x' est déjà présent dans l'ensemble 'S'
        if x in S:
            # Si 'x' est déjà présent, on affiche le nombre d'éléments de l'ensemble
            print(len(S))
        else:
            # Si 'x' n'est pas présent, on l'ajoute à l'ensemble 'S'
            S.add(x)
            # Après l'ajout, on affiche le nouveau nombre d'éléments de l'ensemble
            print(len(S))
    else:
        # Si 'q' n'est pas égal à 0, cela indique une opération de test de présence
        # On crée un nouvel ensemble temporaire ne contenant que l'élément 'x'
        x = {x}
        # On vérifie si l'ensemble 'S' contient tous les éléments de l'ensemble temporaire '{x}'
        # Cela revient à vérifier si 'x' est dans 'S'
        if S >= x:
            # Si c'est le cas, on affiche 1 pour indiquer la présence de 'x'
            print(1)
        else:
            # Sinon, on affiche 0 pour indiquer l'absence de 'x'
            print(0)