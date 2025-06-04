import sys

def read_initial_values():
    """
    Lit les valeurs initiales nécessaires pour le programme :
    n : nombre d'opérations à effectuer
    m : valeur de départ
    
    Returns:
        tuple: (n, m) où n est un int, m est un int
    """
    n = int(input())
    m = int(input())
    return n, m

def process_operations(n, initial_m):
    """
    Effectue la séquence d'opérations de modification de la valeur m.
    À chaque itération, la valeur m est augmentée puis diminuée selon les entrées utilisateur.
    Si la valeur m devient négative, affiche 0 puis termine immédiatement le programme.
    
    Args:
        n (int): Nombre d'opérations à effectuer.
        initial_m (int): Valeur initiale de m.
    
    Returns:
        list: Liste contenant m après chaque opération.
    """
    current_m = initial_m
    sequence = [current_m]  # Conserve la valeur initiale
    for i in range(1, n + 1):
        # Lit deux entiers de l'entrée standard pour cette opération
        a, b = map(int, input().split())
        # Met à jour la valeur de m
        current_m = current_m + a - b
        # Si m devient négatif, affiche 0 et quitte le programme
        if current_m < 0:
            print(0)
            sys.exit(0)
        # Ajoute la valeur courante à la séquence
        sequence.append(current_m)
    return sequence

def main():
    """
    Fonction principale du programme.
    Gère la lecture des entrées, le traitement des opérations,
    puis affiche la valeur maximale atteinte pendant le processus.
    """
    n, m = read_initial_values()
    values_sequence = process_operations(n, m)
    # Affiche la plus grande valeur atteinte au cours des opérations
    print(max(values_sequence))

# Lancement du programme uniquement si ce fichier est exécuté directement
if __name__ == '__main__':
    main()