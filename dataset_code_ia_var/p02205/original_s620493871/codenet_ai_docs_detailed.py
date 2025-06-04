def process_sequence(n, a, b):
    """
    Traite une séquence d'opérations arithmétiques en fonction d'une valeur n et de deux entiers a et b.

    À chaque itération de la boucle (n % 12 fois):
    - Si l'index d'itération est pair, a devient a - b.
    - Si l'index d'itération est impair, b devient a + b.

    Args:
        n (int): Nombre d'opérations à effectuer.
        a (int): Première valeur entière initiale.
        b (int): Deuxième valeur entière initiale.

    Returns:
        tuple: Les valeurs finales de a et b sous la forme (a, b).
    """
    n = n % 12  # Réduit le nombre de tours à n modulo 12
    for i in range(n):
        if i % 2:  # Si l'index est impair
            b = a + b
        else:      # Si l'index est pair
            a = a - b
    return a, b

def main():
    """
    Fonction principale: récupère les entrées utilisateur, traite la séquence et affiche les résultats.
    """
    # Lit un entier n depuis l'entrée utilisateur
    n = int(input())
    # Lit deux entiers, a et b, séparés par un espace
    a, b = map(int, input().split())
    # Appelle la fonction process_sequence pour calculer les nouvelles valeurs de a et b
    a_final, b_final = process_sequence(n, a, b)
    # Affiche les valeurs finales de a et b
    print(a_final, b_final)

if __name__ == "__main__":
    main()