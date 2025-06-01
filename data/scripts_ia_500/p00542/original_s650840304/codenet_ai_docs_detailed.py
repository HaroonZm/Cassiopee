def calculate_value():
    """
    Lit six entiers depuis l'entrée standard, effectue des calculs spécifiques, et affiche le résultat.
    
    Étapes du calcul :
    - Récupère les quatre premiers entiers et les stocke dans un tuple `x`.
    - Récupère les deux entiers suivants et les stocke dans un tuple `y`.
    - Calcule la somme de tous les éléments de `x`.
    - Trouve la valeur minimale dans `x`.
    - Soustrait la valeur minimale de la somme pour obtenir la somme des trois plus grandes valeurs dans `x`.
    - Trouve la valeur maximale dans `y`.
    - Additionne la somme des trois plus grandes valeurs de `x` avec la valeur maximale de `y`.
    - Affiche le résultat final.
    """
    # Lecture des six entiers depuis l'entrée standard
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    
    # Création d'un tuple avec les quatre premiers entiers
    x = (a, b, c, d)
    # Création d'un tuple avec les deux derniers entiers
    y = (e, f)
    
    # Trouver la valeur minimale dans les quatre premiers entiers
    min_x = min(x)
    # Calculer la somme des quatre premiers entiers
    sum_x = sum(x)
    # Calculer la somme des trois plus grandes valeurs en soustrayant la plus petite valeur
    sum_three_largest = sum_x - min_x
    # Trouver la valeur maximale parmi les deux derniers entiers
    max_y = max(y)
    # Calculer la valeur finale en ajoutant la somme des trois plus grandes valeurs aux plus grande valeur parmi y
    g = sum_three_largest + max_y
    
    # Afficher le résultat final
    print(g)

# Exécution de la fonction
calculate_value()