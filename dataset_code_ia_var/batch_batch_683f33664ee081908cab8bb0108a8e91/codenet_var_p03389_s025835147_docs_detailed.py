def calculate_minimum_steps(A, B, C):
    """
    Calcule le nombre minimal d'opérations nécessaires pour rendre les longueurs A, B, et C égales,
    en ajoutant 1 à deux des trois longueurs à chaque opération.
    
    Args:
        A (int): Première longueur initiale.
        B (int): Deuxième longueur initiale.
        C (int): Troisième longueur initiale.
    
    Returns:
        int: Nombre minimal d'opérations requises.
    """
    # Calculer la somme totale des trois longueurs.
    sum_l = A + B + C

    # Trouver la longueur maximale parmi les trois.
    max_l = max(A, B, C)

    # Calculer la différence à combler pour aligner toutes les valeurs sur la longueur maximale.
    # Comme chaque opération permet d'augmenter deux longueurs de 1, le nombre minimal
    # d'opérations est déterminé à partir de la différence diff = 3*max_l - sum_l.
    dif = 3 * max_l - sum_l

    # Si la différence est paire, on peut la combler exactement en diff // 2 opérations.
    if dif % 2 == 0:
        return dif // 2
    else:
        # Si elle est impaire, il faut ajouter 2 opérations supplémentaires pour ajuster.
        return (dif // 2) + 2


def main():
    """
    Lit trois entiers depuis l'entrée standard, calcule et affiche le nombre minimal d'opérations requises
    pour égaliser les trois longueurs.
    """
    # Lecture des trois entiers de l'utilisateur via input standard.
    A, B, C = list(map(int, input().split()))
    
    # Calcul et affichage du résultat.
    result = calculate_minimum_steps(A, B, C)
    print(result)


# Lancement du programme principal si ce fichier est exécuté comme script principal.
if __name__ == "__main__":
    main()