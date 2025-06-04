def read_input():
    """
    Lit le nombre d'éléments 'N' suivi de 'N' paires d'entiers depuis l'entrée standard.
    Pour chaque paire (x, y), calcule x + y et x - y et retourne deux listes distinctes:
    - La liste des x + y
    - La liste des x - y

    Returns:
        tuple:
            N (int): Le nombre total de paires
            X (list of int): Liste des x + y pour chaque paire
            Y (list of int): Liste des x - y pour chaque paire
    """
    N = int(input())  # Lecture du nombre de paires de points
    X = []  # Liste pour stocker les résultats de x + y
    Y = []  # Liste pour stocker les résultats de x - y
    for _ in range(N):
        x, y = map(int, input().split())  # Lecture de la paire d'entiers
        X.append(x + y)  # Ajout de x + y à la liste X
        Y.append(x - y)  # Ajout de x - y à la liste Y
    return N, X, Y

def compute_max_difference(X, Y):
    """
    Calcule la plus grande différence entre la valeur maximale et minimale
    pour chaque liste (X et Y), puis retourne la plus grande de ces deux différences.

    Args:
        X (list of int): Liste des x + y
        Y (list of int): Liste des x - y

    Returns:
        int: La valeur maximale parmi (max(X) - min(X)) et (max(Y) - min(Y))
    """
    # Recherche des valeurs maximales pour X et Y respectivement
    max_X = max(X)
    max_Y = max(Y)
    # Recherche des valeurs minimales pour X et Y respectivement
    min_X = min(X)
    min_Y = min(Y)
    # Calcul de la différence pour X et pour Y
    diff_X = max_X - min_X
    diff_Y = max_Y - min_Y
    # On retourne la plus grande différence des deux
    return max(diff_X, diff_Y)

def main():
    """
    Fonction principale qui coordonne la lecture des données, le calcul
    de la différence maximale, et affiche le résultat.
    """
    # Lecture des entrées et initialisation des listes X et Y
    N, X, Y = read_input()
    # Calcul de la différence maximale
    ans = compute_max_difference(X, Y)
    # Affichage de la réponse finale
    print(ans)

if __name__ == "__main__":
    main()