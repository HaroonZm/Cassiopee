def main():
    """
    Lit deux entiers n et m depuis l'entrée standard.
    Génère une liste de taille n dont les p premiers éléments valent 0 et les suivants valent m,
    puis affiche cette liste décomposée (non encapsulée, séparée par des espaces).
    """
    # Lire deux entiers n et m depuis l'entrée utilisateur.
    n, m = map(int, input().split())
    # Calculer le point de coupure p : nombre de zéros désiré au début de la liste.
    # On veut à peu près la moitié, arrondi vers le haut, donc n//2+1.
    p = n // 2 + 1
    # Créer une liste :
    # Les p premiers éléments sont 0, le reste sont m, pour un total de n éléments.
    result_list = [0] * p + [m] * (n - p)
    # Afficher la liste "décomposée", c'est-à-dire chaque élément séparé par un espace.
    print(*result_list)

if __name__ == "__main__":
    main()