import sys

# Démarrage d'une boucle infinie qui continuera jusqu'à ce qu'on décide explicitement de la stopper
while True:
    # Lecture d'une entrée utilisateur. input() récupère une chaîne de caractères saisie au clavier.
    n = input()
    # La valeur lue est par défaut une chaîne, on doit vérifier si elle représente un entier égale à 0.
    # On convertit n en entier avec int(n).
    # Si l'entier est 0, cela signifie qu'on veut arrêter notre programme donc on sort de la boucle.
    if int(n) == 0:
        break
    
    # Conversion de n en entier à ce stade pour l'utiliser dans des opérations arithmétiques.
    n = int(n)
    
    # Création d'une liste de listes (matrice) de dimension n x n remplie avec des zéros.
    # Cela va servir à stocker la construction finale du carré magique.
    # 
    # La compréhension de liste imbriquée fonctionne ainsi :
    # - Le premier for j in range(n) crée une liste de n éléments,
    # - Chaque élément de cette liste est lui-même une liste de n zéros,
    #   générée par [0 for i in range(n)].
    magic = [[0 for i in range(n)] for j in range(n)]
    
    # Initialisation de la position de départ dans la matrice, pour placer le premier nombre.
    # Selon la méthode du carré magique, on commence au milieu de la première ligne.
    # En Python 3, la division classique / retourne un float, il faut utiliser // pour un entier.
    # Donc on utilise n//2 pour obtenir un entier.
    i = n // 2  # colonne (indice horizontal)
    j = n // 2 + 1  # ligne (indice vertical)
    
    # Parcours de tous les nombres de 1 à n*n inclus, qui devront être placés dans la matrice.
    for number in range(1, n * n + 1):
        # On place le nombre courant à la position [j][i] dans la matrice.
        magic[j][i] = number
        
        # Si c'est le dernier nombre à placer, on peut s'arrêter ici.
        if number == n * n:
            break
        
        # Vérification de la case diagonale en bas à droite de la case courante.
        # On utilise le modulo (%) pour effectuer un "wrap around" quand on atteint les bordures de la matrice.
        # Cela signifie que si j+1 ou i+1 dépasse n-1, on revient au début (indice 0).
        if magic[(j + 1) % n][(i + 1) % n] == 0:
            # Si cette case est vide (contient 0), on déplace la position à cette nouvelle case diagonale.
            i, j = (i + 1) % n, (j + 1) % n
        else:
            # Sinon, si la case est occupée, on essaye un autre déplacement.
            # On recommence par essayer la même case comme pour le cas précédent.
            i, j = (i + 1) % n, (j + 1) % n
            # Tant que la case actuelle est occupée (non zéro), on recule d'une case en colonne
            # et avance d'une case en ligne, toujours avec le modulo pour rester dans la matrice.
            while magic[j][i] != 0:
                i, j = (i - 1) % n, (j + 1) % n
    
    # Affichage du carré magique final.
    # On parcourt chaque ligne (range(n)) et pour chaque ligne on imprime les éléments formatés.
    # Le format "%4d" signifie que chaque nombre entier prendra 4 caractères, aligné à droite.
    for i in range(n):
        # Pour chaque ligne, on crée une liste de chaînes formatées correspondant aux nombres,
        # puis on concatène cette liste pour n'imprimer qu'une seule chaîne par ligne.
        print("".join(["%4d" % (e) for e in magic[i]]))