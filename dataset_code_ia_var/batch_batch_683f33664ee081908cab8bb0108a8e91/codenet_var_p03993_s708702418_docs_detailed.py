def count_special_pairs(N, A):
    """
    Compte le nombre de paires (i, j) vérifiant i < j, A[i] = j+1 et A[j] = i+1 dans la liste A.
    Une paire (i, j) est dite "spéciale" si A[A[i] - 1] - 1 == i.
    Le comptage est fait pour éviter de compter chaque paire deux fois,
    d'où la division finale par 2.

    Args:
        N (int): La taille de la liste A.
        A (list of int): Une liste d'entiers de longueur N, indexés à partir de 0.

    Returns:
        int: Le nombre de paires spéciales satisfaisant la condition décrite.
    """
    # Génère une liste booléenne où chaque élément vaut True (1) si la condition est satisfaite pour l'indice i, sinon False (0).
    special_pairs = [A[A[i] - 1] - 1 == i for i in range(N)]

    # La somme donne le double du nombre de paires spéciales car chaque paire (i, j) et (j, i) est comptée.
    # On divise donc par 2 pour obtenir le nombre réel de paires différentes.
    return sum(special_pairs) // 2

def main():
    """
    Fonction principale pour obtenir les entrées, calculer et afficher le résultat.
    """
    # Lecture de la taille de la liste.
    N = int(input())
    # Lecture de la liste d'entiers séparés par des espaces.
    A = list(map(int, input().split()))
    # Calcul et affichage du résultat.
    print(count_special_pairs(N, A))

if __name__ == "__main__":
    main()