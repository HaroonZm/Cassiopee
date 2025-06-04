#!/usr/bin/env python3

def count_divisors(n):
    """
    Calcule le nombre de diviseurs entiers positifs de n.
    
    Paramètres
    ----------
    n : int
        Nombre entier pour lequel calculer le nombre de diviseurs.
    
    Retourne
    -------
    int
        Nombre de diviseurs de n.
    """
    divisor_count = 0
    # Parcourt tous les entiers de 1 à n inclus
    for a in range(1, n + 1):
        # Si a est un diviseur de n, on incrémente le compteur
        if n % a == 0:
            divisor_count += 1
    return divisor_count

def main():
    """
    Demande à l'utilisateur un nombre entier N,
    puis cherche et affiche le plus petit entier n tel que
    le nombre de diviseurs de n soit exactement N.
    """
    # Lit l'entrée utilisateur et convertit en entier
    N = int(input())
    n = 1  # Commence à 1 (plus petit candidat possible)
    # Boucle jusqu'à trouver l'entier n ayant exactement N diviseurs
    while True:
        # Appelle count_divisors pour obtenir le nombre de diviseurs de n
        if count_divisors(n) == N:
            print(n)
            break  # Sortie de la boucle dès le premier n trouvé
        n += 1  # Passe au nombre suivant

if __name__ == "__main__":
    main()