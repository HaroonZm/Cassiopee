# Définition de la fonction BFS (Breadth-First Search), qui effectue une recherche en largeur pour déterminer s'il est possible d'atteindre un objectif à partir d'un point de départ.
def bfs(start_y, start_x, goal_y, goal_x):
    # Création d'une matrice appelée bfs_map de dimensions h x w remplie de -1.
    # Cette matrice sert à enregistrer les positions déjà visitées pendant la recherche.
    bfs_map = [[-1 for x in range(w)] for y in range(h)]
    # Définition des mouvements possibles à partir d'une cellule (bas, haut, droite, gauche)
    move_y = [1, -1, 0, 0] # Liste indiquant le changement de coordonnée y pour chaque direction
    move_x = [0, 0, 1, -1] # Liste indiquant le changement de coordonnée x pour chaque direction
    # Listes servant à mémoriser les coordonnées y et x qui doivent encore être visitées.
    data_y = [start_y] # Ajout de la position de départ (ordonnée y)
    data_x = [start_x] # Ajout de la position de départ (abscisse x)
    # On marque la position de départ comme visitée en plaçant '1' dans la carte bfs_map
    bfs_map[start_y][start_x] = 1
    # La boucle suivante va fonctionner tant qu'il reste des positions à explorer
    while len(data_x) != 0:
        # Retire la première valeur dans la file pour le y des coordonnées à vérifier
        y = data_y.pop(0)
        # Retire la première valeur dans la file pour le x des coordonnées à vérifier
        x = data_x.pop(0)
        # Boucle sur chaque direction possible (bas, haut, droite, gauche)
        for i in range(4):
            # On ajoute le déplacement i à la position actuelle
            y += move_y[i] # Met à jour temporairement la coordonnée y
            x += move_x[i] # Met à jour temporairement la coordonnée x
            # Vérifie que la nouvelle position (y, x) reste dans les limites valides de la carte
            if y >= 0 and y < h and x >= 0 and x < w:
                # Vérifie si la position actuelle est le but à atteindre
                if y == goal_y and x == goal_x:
                    return "Yes" # Si le but est atteint, on retourne "Yes"
                # Vérifie si la position n'a pas encore été visitée et que c'est une case praticable (".")
                if bfs_map[y][x] == -1 and stage[y][x] == ".":
                    bfs_map[y][x] = 1 # On note la case comme visitée
                    data_y.append(y) # On ajoute la coordonnée y à la liste des prochains à visiter
                    data_x.append(x) # On ajoute la coordonnée x à la liste des prochains à visiter
            # On revient à la position initiale avant d'essayer le prochain déplacement
            y -= move_y[i]
            x -= move_x[i]
    # Si tous les chemins ont été explorés sans trouver l'objectif, on retourne "No"
    return "No"

# Lecture et conversion de la première ligne d'entrée utilisateur
# map(int, input().split()) coupe l'entrée selon les espaces et convertit chaque morceau en entier
h, w, d, n = map(int, input().split()) # h: hauteur, w: largeur, d et n: autres paramètres du problème

# On lit les lignes suivantes comme une carte (stage), chaque ligne représente une ligne de la carte
stage = [input() for i in range(h)]

# On lit une ligne qui contient des entiers et qui est affectée à la liste r
r = list(map(int, input().split()))

# On lit ensuite n lignes d'entrées composées chacune de 3 entiers, stockées dans la liste da
da = [list(map(int, input().split())) for i in range(n)]

# Création d'une matrice ma qui fait la même taille que stage, initialisée avec des 0 (utilisée pour compter un recouvrement)
ma = [[0 for x in range(w)] for y in range(h)]

# On parcourt chaque entrée dans la liste da, qui représente chacune certains objets ou événements sur la carte
for x, y, s in da:
    # Si la valeur s égal d, alors on ajoute 1 partout dans la matrice ma
    if s == d:
        for i in range(h):
            for j in range(w):
                ma[i][j] += 1
    # Si la valeur s est strictement inférieure à d, on ajoute 1 dans un carré centré sur (x, y) de rayon r[s]
    if s < d:
        for i in range(y - r[s], y + r[s] + 1):
            for j in range(x - r[s], x + r[s] + 1):
                # On ne modifie que les cases qui restent dans les limites de la carte
                if i >= 0 and i < h and j >= 0 and j < w:
                    ma[i][j] += 1
    # Si la valeur s vaut au moins 1, on retire 1 dans un carré centré sur (x, y) de rayon r[s-1]
    if s != 0:
        for i in range(y - r[s-1], y + r[s-1] + 1):
            for j in range(x - r[s-1], x + r[s-1] + 1):
                # On ne retire que pour les cases valides dans les limites de la carte
                if i >= 0 and i < h and j >= 0 and j < w:
                    ma[i][j] -= 1

# Création d'une liste vide qui servira à stocker des positions valides
ans = []

# On parcourt toute la carte (stage) pour identifier des positions spéciales et valides
for i in range(h): # i parcourt les lignes de la carte
    for j in range(w): # j parcourt les colonnes de la carte
        # Si la case actuelle est un point de départ (noté "D")
        if stage[i][j] == "D":
            o = i # On enregistre la position y du départ
            l = j # On enregistre la position x du départ
        # Si le nombre de recouvrements à cette position vaut n et que ce n'est pas un mur ("#")
        if ma[i][j] == n and stage[i][j] != "#":
            ans.append([i, j]) # On ajoute la position (i, j) à la liste des réponses potentielles

# Si on n'a trouvé aucune case valide, on affiche "Broken" et on arrête le programme immédiatement
if len(ans) == 0:
    print("Broken")
    quit()

# Création d'une liste key de même taille que ans, contenant initialement "Broken" pour chaque case
key = ["Broken" for i in range(len(ans))]

# Pour chaque position valide trouvée dans ans
for i in range(len(ans)):
    # On utilise la fonction bfs pour déterminer si le point de départ (o, l) atteint ans[i]
    key[i] = bfs(o, l, ans[i][0], ans[i][1])
    # Si le point de départ et la case de destination sont le même point, on force la réponse à "Yes"
    if o == ans[i][0] and l == ans[i][1]:
        key[i] = "Yes"

# On vérifie si les résultats pour toutes les positions valides trouvées sont cohérents
for i in range(1, len(key)):
    # Si un résultat diffère du précédent, on affiche "Unknown" et on arrête le programme
    if key[i] != key[i-1]:
        print("Unknown")
        quit()

# Si tous les résultats sont cohérents (soit tous "Yes", soit tous "No"), on affiche la réponse
print(key[0])