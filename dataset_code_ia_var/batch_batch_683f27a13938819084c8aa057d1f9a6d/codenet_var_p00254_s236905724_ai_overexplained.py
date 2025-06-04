from functools import reduce  # Importe la fonction reduce du module functools, qui permet d'appliquer une fonction de manière cumulative à une séquence d'éléments.

while True:  # Lance une boucle infinie qui ne se termine que lorsqu'elle rencontre un 'break'.
    n = input()  # Lit une ligne entrée par l'utilisateur et la stocke dans la variable 'n'. La fonction input() retourne toujours une chaîne de caractères.

    if n == "0000":  # Vérifie si la chaîne saisie par l'utilisateur est exactement "0000".
        break  # Si la condition est vraie, la boucle se termine immédiatement.

    # Si la longueur de 'n' est inférieure à 4, complète avec des zéros à gauche pour obtenir une chaîne de 4 caractères.
    # Sinon, conserve la chaîne telle quelle.
    n = n if len(n) >= 4 else n.zfill(4)
    # n.zfill(4) renvoie une nouvelle chaîne, de longueur 4, en ajoutant autant de '0' que nécessaire à gauche.

    # Crée une liste de booléens où chaque élément est le résultat de la comparaison entre le premier caractère et les suivants.
    # [n[0] == i for i in n] vérifie si tous les caractères de 'n' sont égaux au premier caractère 'n[0]'.
    # Par exemple, pour n='5555' -> [True, True, True, True]. Pour n='1212' -> [True, False, True, False].
    # reduce(lambda x,y: x and y, ...) effectue un "ET logique" progressif sur toute la liste pour vérifier si tous sont True.
    if reduce(lambda x, y: x and y, [n[0] == i for i in n]):
        print("NA")  # Affiche "NA" si tous les chiffres de 'n' sont identiques (par exemple, "1111").
    else:
        cnt = 0  # Initialise un compteur à zéro. Ce compteur mesure le nombre d'itérations nécessaires pour atteindre 6174.

        # Boucle qui s'exécute tant que 'n' est différent de "6174".
        while n != "6174":
            # Trie la chaîne 'n' par ordre croissant pour obtenir la plus petite combinaison possible des chiffres.
            s = ''.join(sorted(n))  # Par exemple, si n="4321", sorted(n) donne ['1','2','3','4'], on les joint en "1234".

            # Trie la chaîne 'n' par ordre décroissant pour obtenir la plus grande combinaison possible des chiffres.
            l = ''.join(sorted(n, reverse=True))  # Par exemple, si n="1234", on obtient "4321".

            # Convertit les deux chaînes en entiers, les soustrait, puis convertit le résultat en chaîne.
            # Ceci applique l'étape principale de la "constante de Kaprekar".
            n = str(int(l) - int(s))

            # Après la soustraction, on doit s'assurer que 'n' a exactement 4 chiffres (remplissage par des zéros à gauche si nécessaire).
            n = n if len(n) >= 4 else n.zfill(4)

            cnt += 1  # Incrémente le compteur d'une unité à chaque itération de la boucle.

        print(cnt)  # À la sortie de la boucle, affiche le nombre total d'itérations nécessaires pour arriver à 6174.