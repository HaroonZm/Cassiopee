# Création d'une liste contenant les groupes sanguins possibles
l = ["A", "B", "AB", "O"]  # Ici, 'l' est une liste d'éléments chaîne de caractères représentant les groupes sanguins

# Création d'un dictionnaire pour compter le nombre d'occurrences de chaque groupe sanguin
# Les clés sont les types sanguins, et les valeurs initiales sont à 0
dict = {"A": 0, "B": 0, "AB": 0, "O": 0}

# Boucle infinie pour lire les entrées de l'utilisateur
while True:
    try:
        # On attend que l'utilisateur saisisse une chaîne sous la forme "n,s" (par exemple "1,A")
        # input() lit une ligne depuis l'entrée standard (typiquement le clavier)
        # La méthode split(",") coupe la chaîne à chaque virgule et retourne une liste de deux éléments
        n, s = input().split(",")
        # Ici, n correspond à la partie avant la virgule et s à la partie après la virgule
    except:
        # Si une exception se produit (par exemple, EOFError quand il n'y a plus d'entrée à lire, ou ValueError)
        # La boucle se termine avec le mot-clé break
        break
    # On incrémente le compte du groupe sanguin correspondant dans le dictionnaire
    # Cela suppose que s est bien un des groupes "A", "B", "AB" ou "O"
    dict[s] += 1

# Après avoir fini de lire les entrées, on affiche les comptages dans l'ordre des groupes sanguins définis dans la liste l
for i in l:  # Pour chaque valeur i dans la liste l (donc successivement "A", "B", "AB", puis "O")
    # dict[i] donne le nombre d'entrées de ce groupe sanguin, on l'affiche grâce à print()
    print(dict[i])