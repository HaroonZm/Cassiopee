def count_matching_elements():
    """
    Compte le nombre d'éléments d'une liste (t) présents dans une autre liste (s).

    Prend l'entrée utilisateur pour :
      - La taille de la première liste (n), non utilisée dans la logique.
      - La première liste de chaînes, s.
      - Le nombre d'éléments à vérifier (q), non utilisé directement.
      - Une seconde liste de chaînes, t, dont chaque élément est recherché dans s.

    Affiche le nombre d'éléments de t qui apparaissent dans s.
    """
    # Lecture de la taille de la première liste (non utilisée ici, car la saisie n'est pas validée sur cette valeur)
    n = input()

    # Lecture de la liste de chaînes 's', séparation par espace et suppression des espaces inutiles
    s = input().strip().split(" ")

    # Lecture du nombre d'éléments à tester, 'q' (non utilisé explicitement ici)
    q = int(input().strip())

    # Lecture de la liste de chaînes 't' à rechercher dans 's'
    t = input().strip().split(" ")

    # Initialisation d'un compteur pour les correspondances trouvées
    count = 0
    # Parcours de chaque élément dans la liste 't'
    for i in t:
        # Si l'élément 'i' est présent dans 's', incrémente le compteur
        if i in s:
            count += 1
    # Affiche le nombre total de correspondances
    print(count)

# Appel de la fonction principale pour exécuter la logique
count_matching_elements()