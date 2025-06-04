def find_min_diff_between_k_elements(N, K, heights):
    """
    Trouve la différence minimale entre le maximum et le minimum parmi toutes les plages de K éléments
    consécutifs dans une liste de hauteurs triée.

    Args:
        N (int): Le nombre total d’éléments dans la liste de hauteurs.
        K (int): Le nombre d’éléments à considérer dans chaque plage.
        heights (list of int): La liste des hauteurs.

    Returns:
        int: La différence minimale obtenue entre le maximum et le minimum dans chaque sous-liste de taille K.
    """
    # Trie la liste des hauteurs pour faciliter la recherche de plages consécutives minimisant la différence
    sorted_heights = sorted(heights)
    # Initialise la réponse avec une valeur infinie, pour assurer que toute différence est plus petite
    min_diff = float("inf")
    # Parcourt toutes les plages consécutives de taille K dans la liste triée
    for i in range(N - K + 1):
        # Calcule la différence entre la hauteur maximale et minimale dans la plage courante
        current_diff = sorted_heights[i + K - 1] - sorted_heights[i]
        # Met à jour la différence minimale si nécessaire
        min_diff = min(min_diff, current_diff)
    # Retourne la valeur minimale trouvée
    return min_diff

if __name__ == "__main__":
    # Lecture de la première ligne d’entrée : N = nombre d’éléments, K = taille de la plage
    N, K = map(int, input().split())
    # Lecture des hauteurs fournies en entrée, une par ligne, pour un total de N entrées
    heights = [int(input()) for _ in range(N)]
    # Appel de la fonction principale de résolution et affichage du résultat
    result = find_min_diff_between_k_elements(N, K, heights)
    print(result)