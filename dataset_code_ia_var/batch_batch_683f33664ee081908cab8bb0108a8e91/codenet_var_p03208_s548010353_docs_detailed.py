def find_min_diff_in_heights(N, K, H):
    """
    Trouve la différence minimale possible entre la plus grande et la plus petite valeur 
    parmi tous les ensembles de K hauteurs consécutives dans la liste H triée.

    Args:
        N (int): Le nombre total d'éléments dans la liste H.
        K (int): Le nombre d'éléments à sélectionner consécutivement.
        H (list of int): La liste des hauteurs.

    Returns:
        int: La différence minimale trouvée.
    """
    # Trie la liste H pour faciliter la comparaison des groupes consécutifs
    H.sort()
    # Initialise la réponse avec une valeur infinie pour garantir la première mise à jour
    ans = float("inf")
    # Parcourt tous les groupes de K éléments consécutifs dans la liste triée
    for i in range(N - K + 1):
        # Calcule la différence entre la plus grande et la plus petite valeur du groupe courant
        tmp = H[i + K - 1] - H[i]
        # Met à jour la réponse si une différence plus petite est trouvée
        ans = min(ans, tmp)
    # Retourne la différence minimale trouvée
    return ans

# Partie principale du programme
if __name__ == "__main__":
    # Lit les valeurs de N et K depuis l'entrée standard
    N, K = map(int, input().split())
    # Lit les N hauteurs et les stocke dans la liste H
    H = [int(input()) for _ in range(N)]
    # Appelle la fonction et affiche la réponse
    print(find_min_diff_in_heights(N, K, H))