def compute_square_difference(N, A):
    """
    Calcule la différence entre le carré de N et A.

    Paramètres:
        N (int): Un entier dont on veut calculer le carré.
        A (int): Un entier à soustraire du carré de N.

    Retourne:
        int: Le résultat de N*N - A.
    """
    return N * N - A

def main():
    """
    Fonction principale du programme.
    Demande à l'utilisateur deux entiers, puis affiche la différence entre le carré du premier et le second.
    """
    # Lecture du premier entier depuis l'entrée standard (N)
    N = int(input("Entrez un entier N : "))
    # Lecture du second entier depuis l'entrée standard (A)
    A = int(input("Entrez un entier A : "))
    # Calcul de la différence entre le carré de N et A
    result = compute_square_difference(N, A)
    # Affichage du résultat
    print(result)

# Exécute la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    main()