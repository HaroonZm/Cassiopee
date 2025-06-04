def main23():
    # Demande à l'utilisateur de saisir une chaîne de caractères (peut-être vide)
    strbuf = input("")  # strbuf contiendra la saisie de l'utilisateur sous forme de chaîne de caractères

    # Création d'une liste nommée 'flag' destinée à stocker des valeurs booléennes
    # Chaque élément de la liste flag représentera la présence (True) ou absence (False) d'une direction spécifique
    # Les directions sont associées aux index de la façon suivante :
    # flag[0]: 'N' (Nord)
    # flag[1]: 'W' (Ouest)
    # flag[2]: 'S' (Sud)
    # flag[3]: 'E' (Est)
    flag = []

    # Remplir la liste flag avec quatre éléments False, car au début on n'a trouvé aucune direction
    for i in range(4):      # Boucle qui va de i = 0 à i = 3 compris (4 valeurs au total)
        flag.append(False)  # Ajoute la valeur False à la fin de la liste flag à chaque itération

    # Parcours de chaque caractère de la chaîne strbuf à l'aide de son indice i
    for i in range(len(strbuf)):
        # Si le caractère à la position i dans strbuf est la lettre 'N'
        # Met à jour flag[0] pour indiquer que la direction nord est présente
        if strbuf[i] == 'N':
            flag[0] = True
        # Si le caractère courant est 'W', on met flag[1] à True
        if strbuf[i] == 'W':
            flag[1] = True
        # Si c'est 'S', flag[2] devient True
        if strbuf[i] == 'S':
            flag[2] = True
        # Si c'est 'E', flag[3] devient True
        if strbuf[i] == 'E':
            flag[3] = True

    # Vérification de la cohérence des paires de directions opposées :
    # Il faut que si le nord ('N') est présent, le sud ('S') le soit aussi, et inversement — pas de nord ou de sud isolé
    # Pareil pour ouest ('W') et est ('E')
    # Première condition : présence de 'N' sans 'S', ou inversement
    if (flag[0] and not(flag[2])) or (flag[2] and not(flag[0])):
        # Si l'une des paires opposées n'est pas complète, on affiche "No"
        print("No")
    # Deuxième condition : présence de 'W' sans 'E', ou inversement
    elif (flag[1] and not(flag[3])) or (flag[3] and not(flag[1])):
        # Ici aussi, si ouest et est ne sont pas tous les deux présents ou absents, on affiche "No"
        print("No")
    else:
        # Si toutes les paires sont cohérentes (les deux directions opposées sont présentes ou toutes deux absentes)
        print("Yes")

# Cette condition vérifie si ce fichier Python est exécuté en tant que programme principal.
# En Python, __name__ est une variable spéciale qui vaut '__main__' si le script est lancé directement.
# Cela permet d'éviter que main23() ne soit lancé si ce code est importé dans un autre script.
if __name__ == '__main__':
    main23()