def main():
    """
    Lit une séquence de nombres entiers depuis l'entrée standard,
    trie ces nombres dans l'ordre croissant, puis les affiche séparés par des espaces.
    """
    # Lire l'entrée utilisateur sous forme de chaîne et séparer par les espaces
    entree = raw_input()
    # Appliquer 'int' sur chaque élément de l'entrée découpée pour obtenir une liste d'entiers
    a = map(int, entree.split())
    # Convertir l'objet 'map' en liste pour permettre le tri
    a = list(a)
    # Trier la liste d'entiers par ordre croissant
    a.sort()
    # Parcourir chaque élément dans la liste triée
    for i in a:
        # Afficher chaque entier suivi d'un espace (au lieu d'une nouvelle ligne)
        # pour respecter le format d'affichage original
        print i,

if __name__ == "__main__":
    main()