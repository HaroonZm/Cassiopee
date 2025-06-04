def read_input():
    """
    Lit les données d'entrée depuis l'entrée standard. 
    Retourne N, l'ensemble A, M, et l'ensemble B.

    Returns:
        tuple: (N (int), A (set), M (int), B (set))
    """
    readline = open(0).readline  # Fonction utilitaire pour lire une ligne de l'entrée standard
    
    N = int(readline())  # Lit le nombre d'éléments de la première collection
    # Lit les éléments de la première collection, les convertit en int et les ajoute à un set
    A = set(map(int, readline().split()))
    
    M = int(readline())  # Lit le nombre d'éléments de la deuxième collection
    # Lit les éléments de la seconde collection, les convertit en int et les ajoute à un set
    B = set(map(int, readline().split()))
    
    return N, A, M, B

def is_m_sub_in_intersection(A, B, M):
    """
    Vérifie si la taille de l'intersection des ensembles A et B est exactement égale à M.

    Args:
        A (set): Premier ensemble d'entiers.
        B (set): Deuxième ensemble d'entiers.
        M (int): Taille attendue de l'intersection.

    Returns:
        int: 1 si la taille de l'intersection est exactement M, sinon 0.
    """
    intersection_size = len(A & B)  # Taille de l'intersection entre A et B
    return int(intersection_size == M)  # Retourne 1 si l'intersection a M éléments, sinon 0

def main():
    """
    Fonction principale : lit les entrées, vérifie la condition sur l'intersection, et affiche le résultat.
    """
    # Lecture des entrées
    N, A, M, B = read_input()
    # Calcul et affichage du résultat
    print(is_m_sub_in_intersection(A, B, M))

if __name__ == "__main__":
    main()