# Définition de la fonction print_board
def print_board(A, n):
    # Cette fonction prend en entrée une matrice A de taille n x n et affiche ses éléments ligne par ligne.
    # La fonction va parcourir chaque ligne et chaque colonne pour construire une chaîne de caractères
    # représentant chaque ligne avec un espacement aligné selon le nombre de chiffres de chaque élément.

    # Boucle sur chaque indice de ligne i allant de 0 à n-1
    for i in range(n):
        s = ""  # Chaîne vide pour la construction de la ligne à afficher

        # Boucle sur chaque indice de colonne j allant de 0 à n-1
        for j in range(n):
            # On convertit l'élément courant A[i][j] en chaîne pour pouvoir traiter la longueur (nombre de chiffres)
            st = str(A[i][j])

            # Alignement à droite selon la longueur du nombre à afficher :
            # Si le nombre a un seul chiffre
            if len(st) == 1:
                s += "   "  # On ajoute trois espaces pour l'alignement à droite des unités
            # Si le nombre a deux chiffres
            elif len(st) == 2:
                s += "  "  # On ajoute deux espaces pour aligner les dizaines
            # Si le nombre a trois chiffres
            elif len(st) == 3:
                s += " "   # On ajoute un espace pour aligner les centaines

            # On ajoute le nombre lui-même sous forme de chaîne à la ligne courante
            s += str(st)
        # On affiche la ligne construite (tous les éléments de la ligne i de la matrice)
        print(s)

# Définition de la fonction check_leftdown
def check_leftdown(A, h, w, n):
    # Cette fonction calcule et retourne les nouveaux indices (h, w) qui correspondent à un déplacement
    # 'en bas à gauche' dans la matrice A en fonction des règles définies, en tenant compte des débordements.
    # h : index de la ligne courante
    # w : index de la colonne courante
    # n : taille de la matrice

    # Si le prochain déplacement vers le bas dépasse la taille maximale de la matrice (débordement bas)
    if h + 1 > n - 1:
        # On dépasse par le bas, donc on va chercher une case libre dans la colonne de gauche
        w -= 1  # On se déplace d'une colonne vers la gauche (diminution de w)

        # Parcourt les lignes de la colonne nouvellement sélectionnée pour trouver la première case vide (valeur 0)
        for x in range(n):
            if A[x][w] == 0:
                h = x  # On note la ligne vide trouvée
                break  # On arrête la recherche dès qu'on trouve une case vide

    else:
        # Si déplacement normal possible (pas de débordement en bas)
        # On vérifie également un éventuel débordement à gauche
        if w - 1 < 0:
            # Si on dépasse par la gauche, on va tout à droite pour la nouvelle ligne
            w = n  # Valeur temporaire pour l'algorithme, ensuite corrigée dans les autres parties
            h += 1  # On avance d'une ligne
        else:
            # Déplacement standard : une case en bas et une à gauche
            h += 1
            w -= 1

    # Retourne les nouveaux indices de ligne et colonne
    return h, w

# Définition de la fonction check_rightdown
def check_rightdown(A, h, w, n):
    # Cette fonction calcule et retourne les nouveaux indices (h, w) qui correspondent à un déplacement
    # 'en bas à droite' dans la matrice A selon certaines conditions et le contenu de la matrice.
    # h : index de la ligne courante
    # w : index de la colonne courante
    # n : taille de la matrice

    # Vérifie d'abord si on va dépasser le bas de la matrice au prochain déplacement
    if h + 1 > n - 1:

        # Cas où, en plus de dépasser le bas, on dépasse aussi la colonne de droite (coin bas droit)
        if w + 1 > n - 1:
            None  # On ne fait rien ici (instruction vide, en fait inutile dans ce contexte)
        else:
            # Sinon, si on ne déborde qu'à droite, on se déplace d'une colonne à droite
            w += 1

        # Recherche dans la colonne nouvellement sélectionnée la première case vide (valeur 0)
        for x in range(n):
            if A[x][w] == 0:
                h = x  # On note la ligne vide trouvée
                break  # On arrête la boucle dès qu'on trouve une case vide

    else:
        # Sinon, on est encore dans la matrice sans déborder vers le bas
        if w + 1 > n - 1:
            # Si on doit aller à droite mais qu'on dépasse la dernière colonne, on repasse à la première colonne
            w = 0  # Revient à la colonne 0 (très à gauche)
            h += 1  # On avance d'une ligne
        else:
            # Cas standard : une case en bas et une à droite
            h += 1
            w += 1

            # Si la case où on veut aller est déjà remplie (valeur différente de zéro)
            if A[h][w] != 0:
                # Il faut alors réagir avec la logique de déplacement en bas à gauche
                h, w = check_leftdown(A, h, w, n)  # On appelle récursivement la fonction dédiée

    # Retourne les nouveaux indices de ligne et colonne
    return h, w

# Point d'entrée du programme principal
if __name__ == '__main__':

    # Boucle infinie pour traiter une séquence d'entrées utilisateur successives
    while True:
        try:
            # Tente de lire un entier qui spécifie la taille de la matrice à traiter
            n = int(input())  # Conversion en int de la chaîne entrée via le clavier

            # Condition d'arrêt : si l'utilisateur entre 0 (la matrice nulle ne sera pas affichée)
            if n == 0:
                break  # On sort de la boucle principale et donc on termine le programme

            # Initialisation de la matrice carrée n x n entièrement remplie de zéros
            # A est une liste de listes contenant n lignes et n colonnes
            A = [[0 for i in range(n)] for j in range(n)]

            # Calcul du nombre total d'éléments à remplir (n lignes * n colonnes)
            cnt = n * n

            # Boucle sur tous les éléments de la matrice pour les remplir séquentiellement
            for x in range(cnt):
                # Cas particulier pour le tout premier élément à placer dans la matrice
                if x == 0:
                    # Calcul de la position centrale de la matrice
                    mid = n // 2  # Division entière pour obtenir l'indice du milieu

                    # Calcul des indices initiaux de la première case à remplir :
                    h = mid + 1  # L'indice de la ligne de départ (décalé vers le bas du centre)
                    w = mid      # L'indice de la colonne de départ (le centre exact)
                    A[h][w] = x + 1  # On remplit la case déterminée avec la valeur 1 (x commence à 0)
                else:
                    # Pour tous les autres éléments, on calcule la prochaine position selon la logique de déplacement
                    h, w = check_rightdown(A, h, w, n)  # On obtient les nouveaux indices de ligne et colonne
                    A[h][w] = x + 1  # On remplit cette nouvelle case avec la valeur suivante (succession naturelle)

            # Quand la matrice est entièrement remplie, on affiche le résultat via la fonction d'affichage dédiée
            print_board(A, n)

        # En cas de fin de fichier lors de la saisie (Ctrl+D sous Linux, Ctrl+Z sous Windows), le programme s'arrête proprement
        except EOFError:
            break  # Sortir de la boucle en cas d'erreur d'entrée (fin de fichier)