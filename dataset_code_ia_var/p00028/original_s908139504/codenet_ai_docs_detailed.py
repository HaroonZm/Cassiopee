def count_occurrences():
    """
    Lit des entiers depuis l'entrée standard jusqu'à l'EOF et compte
    le nombre d'occurrences de chaque entier.
    Affiche ensuite tous les entiers avec la fréquence maximale, triés par ordre croissant de leur première apparition.

    Comportement détaillé :
    - Lit les entiers via raw_input() jusqu'à EOF.
    - Stocke le compte de chaque entier dans un dictionnaire.
    - Après EOF, identifie la plus grande valeur d'occurrence et affiche
      tous les entiers qui possèdent cette fréquence (un nombre par ligne).
    - Les entiers affichés sont ceux avec la fréquence maximale, dans l'ordre
      où ils sont rencontrés lors du tri par fréquence décroissante puis
      valeur de l'entier croissante en cas d'égalité.
    """
    dic = {}  # Dictionnaire pour stocker le compte de chaque entier
    while True:
        try:
            # Lecture d'un entier depuis l'entrée standard
            num = int(raw_input())
            # Si l'entier n'est pas encore dans le dictionnaire, l'ajouter avec un compte de 1
            if num not in dic:
                dic[num] = 1
            else:
                # Sinon, incrémenter son compte
                dic[num] = dic[num] + 1
        except EOFError:
            # Fin de la saisie, on traite les résultats
            max_num = 0  # Pour stocker la fréquence maximale rencontrée
            index = 0    # Compteur pour savoir combien d'entiers avec max_num ont été affichés
            # Parcours du dictionnaire trié par fréquence décroissante
            for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
                if index == 0:
                    # À la première itération, on définit la fréquence maximale
                    max_num = v
                if max_num != v:
                    # On s'arrête dès qu'on tombe sur une fréquence inférieure à la maximale
                    break
                # Affichage de l'entier ayant la fréquence maximale
                print k
                index += 1
            break

# Exécution de la fonction principale
count_occurrences()