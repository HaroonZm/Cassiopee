# Définition de la fonction 'magic', qui construit un carré magique d'ordre 'n' dans la grille A (variable globale ici)
def magic(n):
    # On commence par initialiser la variable de comptage 'c' à 1.
    # Cette variable représente le prochain nombre à placer dans le carré magique.
    c = 1

    # On calcule la colonne de départ 'x'.
    # 'x' correspond à la moitié de 'n' (division entière flottante en python2).
    x = n / 2

    # Ensuite, on calcule la ligne de départ 'y'.
    # On commence une ligne plus bas que la moitié de 'n' (c'est-à-dire 'x+1').
    y = x + 1

    # On entre dans une boucle infinie (while 1) destinée à remplir le carré magique.
    while 1:
        # On place le nombre courant 'c' à la position [y][x] du tableau A.
        # Note : A est une liste de listes modifiée globalement.
        A[y][x] = c

        # On vérifie si on a placé le dernier nombre, c'est-à-dire si 'c' est égal à n*n.
        # Si c'est le cas, on quitte la boucle (carré rempli).
        if c == n * n:
            break

        # On entre dans une boucle infinie pour déterminer la prochaine position où placer le prochain nombre.
        while 1:
            # Le déplacement naturel pour un carré magique est une case en bas et une à droite (diagonale sud-est).
            # On utilise le modulo 'n' pour faire revenir au début si on dépasse les bornes (effet "tore").
            x, y = (x + 1) % n, (y + 1) % n

            # On vérifie si la position [y][x] est vide (contient 0).
            # Si oui, on sort de cette boucle interne pour placer le prochain nombre ici.
            if A[y][x] == 0:
                break

            # Si la position précédente n'était pas vide, on tente le décalage
            # On revient sur la colonne précédente puis descend encore d'une ligne (sud).
            x, y = (x - 1) % n, (y + 1) % n

            # On vérifie à nouveau si cette nouvelle position est vide.
            if A[y][x] == 0:
                break
            # Si aucune des deux n'est libre on recommence (mais normalement, l'une doit l'être.)

        # On incrémente 'c' pour préparer le prochain nombre à placer dans le carré.
        c += 1

    # La fonction ne retourne rien (None par défaut).
    return

# Boucle principale permettant de traiter plusieurs carrés magiques d'ordre donné par l'utilisateur.
while 1:
    # On lit l'entrée de l'utilisateur avec 'input' (renvoie un entier en python2).
    n = input()

    # Si l'utilisateur entre 0, on arrête la boucle principale.
    if n == 0:
        break

    # On crée un objet range de 0 à n-1 appelé 'N'.
    N = range(n)

    # Création et initialisation de la matrice A avec des zéros.
    # Chaque ligne de la matrice A est une liste de n zéros, réalisée pour chaque i dans N.
    A = [ [0] * n for i in N ]

    # On remplit la matrice A avec la fonction magic pour l'ordre 'n' donné.
    magic(n)

    # On parcourt les lignes de la matrice A pour afficher le carré magique.
    for i in N:
        # Pour chaque élément 'e' dans la ligne A[i], on construit une chaîne avec largeur 4 ('%4d' % e).
        # On joint cette liste de chaînes pour chaque élément 'e' pour obtenir une ligne entière du carré.
        print "".join(["%4d" % (e) for e in A[i]])
        # La ligne est affichée à l'écran, un carré par entrée de l'utilisateur.