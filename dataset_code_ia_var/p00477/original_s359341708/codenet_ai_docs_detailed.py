def sum_inputs(num_inputs=4):
    """
    Demande à l'utilisateur de saisir un certain nombre d'entiers, puis retourne la somme de ces entiers.
    
    Args:
        num_inputs (int): Le nombre de saisies à effectuer (par défaut 4).
    
    Returns:
        int: La somme des entiers saisis.
    """
    total = 0  # Initialisation de la somme totale
    for _ in range(num_inputs):
        # Demander à l'utilisateur de saisir un entier et additionner à la somme totale
        y = int(input())
        total += y
    return total

def count_full_minutes(total_seconds):
    """
    Calcule le nombre de minutes entières (groupes de 60 secondes) dans un nombre total de secondes.
    
    Args:
        total_seconds (int): Le nombre total de secondes.
    
    Returns:
        int: Le nombre de minutes entières contenues dans total_seconds.
    """
    c = total_seconds  # Copie du total de secondes pour décrémentation
    minute_count = 0   # Compteur de minutes
    while True:
        if c < 0:
            # Sortir de la boucle dès que le nombre de secondes devient négatif
            break
        else:
            # Retirer 60 secondes (une minute complète) et incrémenter le compteur
            c -= 60
            minute_count += 1
    minute_count -= 1  # La dernière itération dépasse 0, il faut donc retirer 1
    return minute_count

def secondes_restantes_apres_minutes(total_seconds):
    """
    Calcule le reste de secondes après avoir enlevé toutes les minutes complètes (modulo 60).
    
    Args:
        total_seconds (int): Le nombre total de secondes.
    
    Returns:
        int: Le nombre de secondes restantes (moins d'une minute).
    """
    return total_seconds % 60

def main():
    """
    Point d'entrée du programme.
    Demande à l'utilisateur quatre entiers, les additionne, puis affiche le nombre de minutes complètes
    et le nombre de secondes restantes.
    """
    # Obtenir la somme des entrées utilisateur
    t = sum_inputs()
    # Calculer le nombre de minutes entières dans la somme
    g = count_full_minutes(t)
    # Calculer le nombre de secondes restantes après avoir retiré les minutes entières
    r = secondes_restantes_apres_minutes(t)
    # Afficher les résultats
    print(g)
    print(r)

# Exécution du programme principal
if __name__ == "__main__":
    main()