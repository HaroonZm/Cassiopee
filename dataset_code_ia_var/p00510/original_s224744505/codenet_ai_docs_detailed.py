def calculate_max_value():
    """
    Calcule la valeur maximale atteinte après une série de n opérations,
    à partir d'une valeur initiale m. Chaque opération est composée de 
    deux entiers a et b : a est ajouté, b est soustrait à la valeur courante.
    Si la valeur courante devient négative, elle n'est plus modifiée mais 
    la simulation continue. La valeur maximale rencontrée durant la simulation 
    est renvoyée.

    Entrée utilisateur :
        - n : entier, nombre d'opérations à effectuer
        - m : entier, valeur initiale
        - puis n lignes de deux entiers séparés par un espace pour chaque opération (a b)

    Sortie :
        - Affiche la valeur maximale atteinte
    """
    n = int(input())  # Nombre d'opérations à effectuer
    m = int(input())  # Valeur initiale de la variable
    ans = c = m       # ans garde la valeur maximale atteinte, c la valeur courante
    
    # Parcourt les n opérations
    for i in range(n):
        # Lit deux valeurs entières sur la même ligne, séparées par un espace
        a, b = [int(x) for x in input().split()]
        
        # Si la valeur courante est négative, on stoppe la modification
        if c < 0:
            continue
        
        # Met à jour la valeur courante : ajoute a, soustrait b
        c += a - b
        
        # Met à jour la valeur maximale si nécessaire
        if ans < c:
            ans = c
        
        # Si la valeur courante tombe sous zéro, la valeur maximale devient 0
        if c < 0:
            ans = 0
    print(ans)

# Appel de la fonction principale
calculate_max_value()