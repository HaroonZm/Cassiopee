def check_list_equality():
    """
    Lit une ligne de nombres entiers séparés par des espaces depuis l'entrée utilisateur,
    les trie par ordre croissant, puis vérifie si les éléments aux indices 0 à 3, 4 à 7
    et 8 à 11 sont égaux par blocs. Affiche 'yes' si les trois blocs ont des valeurs identiques
    respectivement (chaque bloc d'indices contient la même valeur), sinon affiche 'no'.
    """
    # Lecture de l'entrée utilisateur sous forme d'une chaîne de caractères
    user_input = input()
    # Conversion de la chaîne en une liste d'entiers, suivie d'un tri croissant
    lst = sorted(map(int, user_input.split()))
    # Vérification des trois blocs de 4 éléments consécutifs pour l'égalité de chacun
    # On compare le premier et le dernier élément de chaque bloc (indices 0 et 3, 4 et 7, 8 et 11)
    if lst[0] == lst[3] and lst[4] == lst[7] and lst[8] == lst[11]:
        # Si les trois blocs contiennent chacun la même valeur, afficher 'yes'
        print("yes")
    else:
        # Sinon, afficher 'no'
        print("no")

# Appel de la fonction principale pour exécuter le programme
check_list_equality()