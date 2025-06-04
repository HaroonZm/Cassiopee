def find_min_difference(N, K, H):
    """
    Calcule la différence minimale entre la hauteur maximale et minimale parmi toutes les
    sous-séquences de K hauteurs dans une liste donnée de hauteurs.

    Args:
        N (int): Le nombre total de hauteurs.
        K (int): La taille de la sous-liste à examiner.
        H (list of int): Liste des hauteurs.

    Returns:
        int: La différence minimale trouvée.
    """
    # Trie la liste des hauteurs afin de faciliter la recherche de sous-listes consécutives optimales
    H.sort()
    # Initialisation d'une liste pour stocker toutes les différences possibles
    differences = []

    # Parcours chaque sous-liste consécutive de taille K
    for i in range(N - K + 1):
        # Calcule la différence entre la plus grande et la plus petite valeur de la sous-liste
        diff = H[i + K - 1] - H[i]
        differences.append(diff)
    
    # Retourne la différence minimale parmi toutes les sous-listes examinées
    return min(differences)

def main():
    """
    Fonction principale qui gère la lecture des entrées utilisateur, le calcul et l'affichage du résultat.
    """
    # Lecture des valeurs de N (nombre d'éléments) et K (taille de la sous-liste)
    N, K = map(int, input().split())
    # Lecture des hauteurs, une par ligne, et stockage dans une liste
    H = [int(input()) for _ in range(N)]
    # Calcul et affichage de la différence minimale
    print(find_min_difference(N, K, H))

# Exécution de la fonction principale si le script est lancé directement
if __name__ == "__main__":
    main()