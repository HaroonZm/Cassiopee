def generate_sequence(n, m):
    """
    Génère une séquence de longueur n composée de zéros et de m, selon la parité de n.
    
    Si n est impair :
        - La séquence contient (n // 2) zéros suivis de (n // 2 + 1) m.
    Si n est pair :
        - La séquence contient (n // 2 - 1) zéros suivis de (n // 2 + 1) m.

    Args:
        n (int): La longueur de la séquence à générer.
        m (int): La valeur à utiliser dans la deuxième partie de la séquence.

    Returns:
        list: La séquence générée sous forme de liste d'entiers.
    """
    if n % 2:  # Vérifie si n est impair
        # Construit la séquence: (n//2) zéros suivis de (n//2 + 1) m
        sequence = [0] * (n // 2) + [m] * (n // 2 + 1)
    else:  # Si n est pair
        # Construit la séquence: (n//2 - 1) zéros suivis de (n//2 + 1) m
        sequence = [0] * (n // 2 - 1) + [m] * (n // 2 + 1)
    return sequence

def main():
    """
    Fonction principale qui lit les entrées utilisateur, génère la séquence et l'affiche.

    L'utilisateur doit saisir deux entiers séparés par un espace :
    - n : la longueur de la séquence à produire,
    - m : la valeur utilisée après les zéros.
    """
    # Lecture et conversion des entrées utilisateur
    n, m = map(int, input().split())
    # Génération de la séquence selon les règles spécifiées
    result_sequence = generate_sequence(n, m)
    # Affichage de la séquence, en séparant les éléments par des espaces
    print(*result_sequence)

if __name__ == "__main__":
    main()