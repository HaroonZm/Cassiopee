def calculate_maximum_operation():
    """
    Lit deux entiers depuis l'entrée standard, calcule la somme, la différence et le produit de ces deux entiers,
    puis affiche la valeur maximale parmi ces trois résultats.

    Entrée :
        Deux entiers séparés par un espace (exemple : "3 5")

    Sortie :
        Un entier, qui est le maximum des valeurs A+B, A-B, A*B
    """

    # Lire une ligne depuis l'entrée standard, la séparer en deux éléments,
    # puis convertir chaque élément en entier A et B
    A, B = map(int, input().split())
    
    # Calculer la somme de A et B
    sum_ab = A + B
    # Calculer la différence de A et B
    diff_ab = A - B
    # Calculer le produit de A et B
    prod_ab = A * B

    # Trouver la valeur maximale parmi la somme, la différence et le produit
    result = max(sum_ab, diff_ab, prod_ab)

    # Afficher la valeur maximale
    print(result)

# Appeler la fonction principale pour exécuter le programme
calculate_maximum_operation()