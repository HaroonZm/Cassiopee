def calculate_positive_difference_sum(N, V, C):
    """
    Calcule la somme des différences positives entre deux listes d'entiers.
    Pour chaque index i, si V[i] - C[i] > 0, ajoute cette différence à la somme totale.

    Args:
        N (int): Le nombre d'éléments dans les listes V et C.
        V (list of int): Liste des valeurs initiales.
        C (list of int): Liste des valeurs à soustraire de V.

    Returns:
        int: La somme des différences positives pour chaque index.
    """
    Ans = 0  # Variable pour stocker la somme totale des différences positives

    # Parcourt chaque index des listes V et C
    for i in range(N):
        # Vérifie si la différence est positive
        if V[i] - C[i] > 0:
            Ans += V[i] - C[i]  # Ajoute la différence à la somme totale

    return Ans

def main():
    """
    Lit les entrées utilisateur, effectue le calcul des différences positives 
    et affiche le résultat final.
    """
    # Lecture du nombre d'éléments
    N = int(input())

    # Lecture et conversion en liste d'entiers pour les valeurs V
    V = list(map(int, input().split()))

    # Lecture et conversion en liste d'entiers pour les valeurs C
    C = list(map(int, input().split()))

    # Appel de la fonction pour calculer la somme et affichage du résultat
    result = calculate_positive_difference_sum(N, V, C)
    print(result)

if __name__ == "__main__":
    main()