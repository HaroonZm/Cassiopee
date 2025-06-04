def get_position_value(a: int, b: int, n: int) -> int:
    """
    Calcule une valeur basée sur la position (a, b) dans une grille de taille n x n.
    La valeur retournée dépend du minimum parmi les distances de (a, b) aux côtés de la grille :
    - renvoie 3 si ce minimum modulo 3 vaut 0
    - renvoie 1 si ce minimum modulo 3 vaut 1
    - renvoie 2 sinon

    Args:
        a (int): La coordonnée de la ligne (entier, 1-indexé)
        b (int): La coordonnée de la colonne (entier, 1-indexé)
        n (int): La taille de la grille (n x n)

    Returns:
        int: La valeur calculée selon la règle décrite.
    """
    # Calculer la distance minimale de (a, b) aux quatre côtés de la grille
    min_dist = min(a, b, n - a + 1, n - b + 1)
    # Dépend du modulo 3 de cette distance
    if min_dist % 3 == 0:
        return 3
    elif min_dist % 3 == 1:
        return 1
    else:
        return 2

def main():
    """
    Lit les entrées utilisateur pour la taille de la grille et le nombre de requêtes,
    puis traite chaque requête et affiche la valeur correspondante.
    """
    # Lecture de la taille de la grille carrée (n x n)
    n = int(input())
    # Lecture du nombre de requêtes à traiter
    k = int(input())
    
    # Traite chacune des k requêtes
    for _ in range(k):
        # Lecture des coordonnées a et b pour chaque requête
        a, b = map(int, input().split())
        # Calcul de la valeur basée sur la position et affichage
        result = get_position_value(a, b, n)
        print(result)

if __name__ == "__main__":
    main()