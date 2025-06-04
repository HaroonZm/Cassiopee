# Importation de tous les objets du module networkx
from networkx import*

# Ouverture de l'entrée standard (input) et lecture des lignes.
# La première ligne (H) contient des valeurs de dimensions, 
# les lignes suivantes (S) correspondent à la grille.
H, *S = open(0)

# Découpage de la première ligne pour obtenir les dimensions (H et W).
# map applique la fonction int à chaque élément de la liste obtenue par split().
# H : nombre de lignes. W : nombre de colonnes.
H, W = map(int, H.split())

# Création d'un objet Graphe non orienté (Graph) à l'aide de networkx.
g = Graph()

# L'attribut add_edges_from permet d'ajouter des arêtes en lot au graphe,
# a est donc une référence abrégée à cette méthode de l'objet g.
a = g.add_edges_from

# La boucle parcourt chaque case (cellule) de la grille.
# i : indice linéaire de la cellule, 
# va de 0 à (m - 1) où m est le nombre total de cellules.
for i in range(m := H * W):

    # h correspond au numéro de la ligne de la cellule courante (indice de la case sur l'axe vertical).
    # // est la division entière, W : nombre de colonnes.
    h = i // W

    # w correspond au numéro de la colonne de la cellule courante (indice de la case sur l'axe horizontal).
    # % est le modulo, permet de rester dans l'intervalle des colonnes.
    w = i % W + m

    # c extrait le caractère situé à la ligne h et à la colonne (w-m) de la grille S.
    # w-m donne l'indice de colonne réel, car w = i % W + m donc w-m = i % W.
    c = S[h][w - m]

    # La variable I est définie plus bas mais utilisée dans la construction des arêtes au cas où la case correspond à 'T'.
    # Pour 'S' ou 'T', création d'arêtes spéciales, sinon création d'arêtes standard de capacité 1.

    # Ajout d'arêtes au graphe g selon le type de caractère rencontré dans la case.
    # Si c == 'S' : ajoute une arête du super source (m*2) à h (entrée cellule) et du super source à w (sortie cellule).
    # Si c == 'T' : ajoute une arête de h (entrée cellule) au super puits (I=m*3) et de w (sortie cellule) au super puits.
    # Pour d'autres caractères (> 'T'), ajoute une arête entre entrée et sortie, capacité 1, et l'inverse.
    a(
        # Liste d'arêtes pour 'S'
        [[m*2, h], [m*2, w]] * (c == 'S')  # Si la case courante contient 'S', ajoute ces deux arêtes depuis le super source
        
        # Liste d'arêtes pour 'T'
        + [[h, I := m*3], [w, I]] * (c == 'T')  # Si la case courante contient 'T', ajoute ces deux arêtes vers le super puits
        
        # Liste d'arêtes pour les autres caractères (c > 'T')
        + [[h, w], [w, h]] * (c > 'T'),  # Si la valeur caractère ASCII de c > 'T', ajoute des arêtes entre entrée et sortie dans les deux sens
        
        capacity=I if c == 'T' else 1  # Capacité de l'arête : m*3 pour 'T', sinon 1 par défaut
    )

# Calcul d'un minimum_cut (coupe de flot minimum) entre le super source (m * 2) et le super puits (I) du graphe g.
# minimum_cut retourne un tuple dont le premier élément est la valeur de la coupe,
# et le deuxième est un ensemble de nœuds (partition du graphe selon la coupe).
f = minimum_cut(g, m * 2, I)[0]

# Si la valeur de flot f est inférieure à I (i.e., la capacité max possible), alors la coupe a réussi.
# On affiche 1 (car f < I)\
# Sinon, on affiche -1 (impossible d'atteindre le super puits).
print([-1, f][f < I])