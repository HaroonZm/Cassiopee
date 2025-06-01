while True:
    # Lire une ligne d'entrée de l'utilisateur, qui contient trois nombres séparés par des espaces
    # Ensuite, convertir chaque chaîne en entier et les assigner aux variables d, w et h respectivement
    d, w, h = map(int, input().split())
    
    # Vérifier si la variable d est égale à 0
    # Si c'est le cas, cela signifie que la boucle doit s'arrêter, donc utiliser 'break' pour sortir de la boucle infinie
    if d == 0:
        break
    
    # Calculer trois valeurs comme des sommes de carrés de paires de variables:
    # d^2 + w^2, w^2 + h^2, h^2 + d^2
    # Ces calculs donnent les carrés des distances maximales possibles selon différentes dimensions
    # Puis, prendre la plus petite de ces trois valeurs avec la fonction min()
    # Enfin, assigner cette valeur minimale à la variable d
    d = min(d**2 + w**2, w**2 + h**2, h**2 + d**2)
    
    # Lire un entier n depuis l'entrée, ce qui indique combien de fois nous allons répéter la vérification suivante
    n = int(input())
    
    # Commencer une boucle 'for' qui s'exécute n fois
    # L'itérateur i prend des valeurs de 0 jusqu'à n-1
    for i in range(n):
        # Lire un entier depuis l'entrée utilisateur, le multiplier par 2, puis élever le résultat au carré
        # Cela calcule le carré du double de cette valeur entrée, assignée à la variable d_i
        d_i = (int(input()) * 2) ** 2
        
        # Comparer d_i à la valeur d calculée précédemment
        # Si d_i est strictement supérieur à d, cela signifie que la condition est satisfaite
        if d_i > d:
            # Si la condition est vraie, afficher la chaîne de caractères "OK"
            print("OK")
        else:
            # Sinon, si la condition est fausse ou égale, afficher la chaîne de caractères "NA"
            print("NA")