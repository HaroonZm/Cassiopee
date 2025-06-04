# Importation de modules standards de la bibliothèque Python :
import sys  # Ce module permet d'interagir avec le système, notamment pour la gestion des entrées/sorties.
import math  # Ce module fournit des fonctions mathématiques de base (non utilisé ici mais importé quand même).
import os  # Ce module permet d'interagir avec le système d'exploitation, par exemple pour lire les variables d'environnement.

# Lecture de l'entrée standard ou d'un fichier selon le contexte d'exécution.
PYDEV = os.environ.get('PYDEV')  # On lit la variable d'environnement 'PYDEV'.
if PYDEV == "True":  # On vérifie si 'PYDEV' est exactement la chaîne "True".
    # Si c'est le cas, on redirige l'entrée standard (sys.stdin) pour qu'elle lise les données d'un fichier texte.
    sys.stdin = open("sample-input.txt", "rt")  # On ouvre le fichier en mode texte pour lecture uniquement.

# Définition de la fonction 'magic_square' pour générer un carré magique de taille 'n x n'.
def magic_square(n):
    # Initialisation d'une grille carrée de taille maximale.
    # On crée une liste de listes contenant initialement des zéros.
    sq = [[0 for _ in range(16)] for __ in range(16)]  # La taille 16 est utilisée car la contrainte maximale de n <= 15.

    # Calcul des coordonnées de départ pour remplir la première case du carré magique.
    # La position de départ dépend souvent de la méthode employée (ici, pour des carrés impairs).
    nowx = n // 2  # On commence au centre horizontal de la grille (division entière).
    nowy = n // 2 + 1  # On commence une ligne sous le centre vertical.

    # On place la valeur '1' à la position de départ calculée précédemment.
    sq[nowy][nowx] = 1

    # Remplissage progressif du carré magique de 2 à n^2 inclus (les valeurs à placer dans la grille).
    for i in range(2, n ** 2 + 1):  # On commence par 2 car 1 a déjà été placé.
        nowx += 1  # On décale la position courante d'une colonne vers la droite (augmentation de x).
        nowy += 1  # On décale la position courante d'une ligne vers le bas (augmentation de y).

        # On entre dans une boucle qui cherche la première cellule vide selon l'algorithme du carré magique.
        while True:
            if nowx >= n:  # Si on déborde du bord droit de la grille,
                nowx = 0  # on revient à la première colonne (coordonnée circulaire).
            if nowx < 0:  # Si on déborde du bord gauche,
                nowx = n - 1  # on va à la dernière colonne.
            if nowy >= n:  # Si on déborde vers le bas de la grille,
                nowy = 0  # on revient à la première ligne.
            if sq[nowy][nowx] != 0:  # Si la case actuelle est déjà occupée,
                nowx -= 1  # on recule d'une colonne vers la gauche,
                nowy += 1  # et on descend d'une ligne vers le bas.
            # Si la case courante est vide (valeur 0) ET
            # les coordonnées sont bien dans la grille (0 <= nowx < n et 0 <= nowy < n),
            # alors on a trouvé la bonne cellule où placer la prochaine valeur.
            if sq[nowy][nowx] == 0 and 0 <= nowx and nowx < n and 0 <= nowy and nowy < n:
                break  # On sort de la boucle 'while' car la cellule est valide et vide.

        sq[nowy][nowx] = i  # On place la valeur courante 'i' dans la position correcte de la grille.

    # On retourne uniquement la partie utile du carré (n lignes complètes), car la grille initiale fait toujours 16x16.
    return sq[:n]

# Boucle principale du programme qui lit les entrées, génère les carrés magiques et affiche les résultats.
while True:  # Une boucle sans condition explicite permettant de traiter une séquence d'entrées.
    n = int(input())  # On lit un nombre entier depuis l'entrée standard, qui représente la taille du carré magique désiré.
    if n == 0:  # Si la taille lue est zéro, cela signifie qu'on doit s'arrêter selon l'énoncé du problème.
        break  # On quitte la boucle principale.

    sq = magic_square(n)  # On appelle la fonction pour générer le carré magique de taille 'n' et on stocke le résultat dans 'sq'.

    # On parcourt chaque ligne du carré magique retourné.
    for row in sq:
        out = ""  # On initialise une chaîne vide qui contiendra la ligne formatée à afficher.
        for k in row[:n]:  # On parcourt uniquement les n premières valeurs de la ligne (au cas où la taille initiale dépasserait 'n').
            ks = str(k)  # On convertit la valeur entière en chaîne de caractères pour l'affichage.
            ks = ' ' * (4 - len(ks)) + ks  # On ajoute autant d'espaces blancs devant qu'il en faut pour aligner le nombre sur 4 caractères.
            out += ks  # On ajoute la valeur formatée à la chaîne de sortie 'out'.
        print(out)  # On affiche la ligne du carré magique avec tous les nombres correctement alignés.