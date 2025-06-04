import sys  # Importe le module sys qui permet d'utiliser des fonctionnalités système, comme la sortie standard ou la gestion des arguments

while True:  # Boucle infinie qui ne sera arrêtée qu'en rencontrant un 'break' explicitement. Sert ici à permettre plusieurs entrées utilisateur successives.
    n = input()  # Demande une entrée à l'utilisateur. Par défaut, 'input' retourne une chaîne de caractères.
    # Comme l'utilisateur peut entrer n'importe quoi, il faut s'assurer que n est bien un entier.
    # Cependant, ici, le code original suppose un int, donc il faut convertir.
    n = int(n)  # Convertit la chaîne lue en entier. Si ce n'est pas possible, cela générera une exception.
    if n == 0:  # Vérifie si l'utilisateur a saisi 0. Si oui, on arrête la boucle infinie avec break.
        break

    # Création d'une grille carrée 'magic' de taille n×n remplie de zéros.
    # On utilise une compréhension de listes imbriquée.
    # La syntaxe [[0 for i in range(n)] for j in range(n)] fait :
    # Pour chaque j de 0 à n-1, crée une liste contenant n zéros (un pour chaque i de 0 à n-1).
    magic = [[0 for i in range(n)] for j in range(n)]

    # Calcul de la position initiale de la première valeur à placer dans le carré magique.
    # i est l'indice pour les colonnes, j pour les lignes. On commence classiquement au centre.
    i = n // 2  # Divise n par 2 (division entière), soit l'indice central de la colonne.
    j = n // 2 + 1  # Idem pour la ligne, mais décalé de 1 vers le bas.

    # Boucle pour placer tous les nombres de 1 à n*n dans la grille 'magic'.
    for number in range(1, n * n + 1):  # Parcourt les entiers de 1 à n*n inclus.
        magic[j % n][i % n] = number  # Place le nombre courant dans la grille, en tenant compte du modulo n (pour le rebouclage).
        # On vérifie si on vient de placer le dernier nombre dans la grille.
        if number == n * n:
            break  # Si oui, on arrête la boucle de placement.

        # On cherche la prochaine case où placer le nombre suivant.
        # Cas normal : si la diagonale en bas à droite est libre (contient zéro), on y va.
        if magic[(j + 1) % n][(i + 1) % n] == 0:
            i = (i + 1) % n  # Décale i (colonne) d'une case à droite, avec rebouclage si on dépasse n-1.
            j = (j + 1) % n  # Décale j (ligne) d'une case vers le bas, idem modulo n.
        else:
            # Si la diagonale en bas à droite n'est pas libre, il faut trouver la prochaine case vide dans une autre direction.
            i = (i + 1) % n  # D'abord, on décale d'une case à droite
            j = (j + 1) % n  # ...et une case vers le bas.
            while magic[j % n][i % n] != 0:  # Tant que la nouvelle case n'est pas libre...
                i = (i - 1) % n  # ...déplace i d'une case à gauche (toujours en prenant le modulo n).
                j = (j + 1) % n  # ...et j d'une case vers le bas.
                # On répète ce processus jusqu'à ce qu'on tombe sur une case vide.

    # Affichage du carré magique final.
    # On parcourt chaque ligne i de la grille.
    for i in range(n):
        # On crée une liste de chaînes (une pour chaque élément e de la ligne magic[i]),
        # chaque élément est formaté sur 4 caractères avec '%4d' pour un alignement propre.
        # On joint ensuite tous ces éléments en une seule chaîne, puis on affiche cette chaîne.
        print("".join(["%4d" % (e) for e in magic[i]]))  # Affiche la ligne complète sans espace entre les colonnes (collées côte à côte, alignées à 4 caractères).