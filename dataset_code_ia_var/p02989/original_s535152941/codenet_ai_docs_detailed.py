def main():
    """
    Lit un nombre entier N, puis une liste de N entiers.
    Trie la liste, puis affiche la différence entre les éléments situés à la position médiane
    et juste avant la médiane dans la liste triée.
    """

    # Lecture de la taille de la liste
    N = int(input())

    # Lecture de la liste de valeurs, convertie en entiers
    d = [int(x) for x in input().split()]

    # Trie la liste d'entiers en ordre croissant
    d.sort()

    # Calcule l'indice de la médiane (partie entière de N/2)
    h = N // 2

    # Affiche la différence entre l'élément à la médiane et celui juste avant
    # Ceci est utile dans certains contextes comme le calcul de l'écart minimal entre deux moitiés d'ensemble trié
    print(d[h] - d[h - 1])

if __name__ == "__main__":
    main()