from functools import reduce  # Importation de la fonction 'reduce' du module 'functools', utilisée pour appliquer une fonction cumulativement aux éléments d'une séquence

while True:  # Début d'une boucle infinie, qui continuera jusqu'à ce qu'une condition de sortie soit rencontrée
    n = input()  # Lecture d'une chaîne de caractères saisie par l'utilisateur; stockée dans la variable 'n'

    if n == "0000":  # Vérification si l'entrée est exactement la chaîne "0000"
        break  # Si c'est le cas, on quitte la boucle infinie, terminant ainsi le programme

    # Si la longueur de la chaîne 'n' est inférieure à 4 caractères:
    # On complète la chaîne avec des zéros ('0') à gauche jusqu'à obtenir une longueur de 4 caractères
    # Ceci est fait pour uniformiser la taille des nombres manipulés par la suite
    n = n if len(n) >= 4 else n.zfill(4)

    # Vérification si tous les caractères de la chaîne 'n' sont identiques
    # Explication détaillée :
    # - [n[0] == i for i in n] crée une liste de booléens où chaque élément indique si le caractère correspondant
    #   dans 'n' est égal au premier caractère n[0]
    # - reduce(lambda x,y: x and y, [...]) applique la fonction 'and' entre tous les éléments de la liste,
    #   ce qui aboutit à True uniquement si tous les éléments sont True (donc tous les caractères égaux)
    if reduce(lambda x, y: x and y, [n[0] == i for i in n]):

        # Si tous les chiffres sont identiques, la situation ne permet pas d'atteindre 6174 (la constante de Kaprekar)
        # On affiche donc "NA" pour dire que ce n'est pas applicable
        print("NA")

    else:  # Si tous les chiffres ne sont pas identiques, on peut procéder au calcul de Kaprekar

        cnt = 0  # Initialisation d'un compteur à zéro, qui va compter le nombre d'itérations nécessaires pour atteindre 6174

        while n != "6174":  # Tant que le nombre n'est pas égal à 6174, on continue les transformations

            # 'sorted(n)' trie les caractères de la chaîne 'n' dans l'ordre croissant, renvoyant une liste de caractères
            s = ''.join(sorted(n))  # Ces caractères triés en ordre croissant sont recombinés en une nouvelle chaîne 's'

            # 'sorted(n, reverse=True)' trie les caractères en ordre décroissant
            l = ''.join(sorted(n, reverse=True))  # Ces caractères triés en ordre décroissant sont recombinés en une chaîne 'l'

            # On convertit les deux chaînes 'l' et 's' en entiers,
            # puis on fait la soustraction 'l' - 's' comme étape clé de la routine de Kaprekar
            n = str(int(l) - int(s))  # On reconvertit le résultat en chaîne de caractères pour les prochaines opérations

            # Comme le résultat de la soustraction peut avoir moins de 4 chiffres (par ex. 7 au lieu de 0007),
            # on complète la chaîne avec des zéros à gauche pour que sa longueur soit de 4 caractères
            n = n if len(n) >= 4 else n.zfill(4)

            cnt += 1  # À chaque itération, on incrémente le compteur pour enregistrer une étape supplémentaire

        # Une fois que le nombre atteint 6174, on sort de la boucle et on affiche le nombre d'itérations nécessaires
        print(cnt)