def main():
    """
    Programme principal qui lit trois entiers saisis par l'utilisateur,
    les trie par ordre croissant et affiche le résultat sous forme formatée.
    """

    # Lire une ligne de l'entrée standard, séparer les valeurs par des espaces,
    # puis convertir chaque valeur en entier à l'aide de map.
    # 'raw_input()' lit une chaîne entrée par l'utilisateur.
    # 'split()' divise la chaîne en une liste de sous-chaînes.
    # 'map(int, ...)' applique int() à chaque sous-chaîne pour obtenir une liste d'entiers.
    user_input = map(int, raw_input().split())

    # Convertir l'objet map (en Python 2) ou list (en Python 3) en une liste explicite
    numbers = list(user_input)

    # Trier la liste des entiers par ordre croissant grâce à sort().
    numbers.sort()

    # Afficher les trois entiers triés dans un format spécifique
    # "%d %d %d" permet l'affichage formaté des trois entiers séparés par des espaces.
    print "%d %d %d" % (numbers[0], numbers[1], numbers[2])

# Point d'entrée du script
if __name__ == "__main__":
    main()