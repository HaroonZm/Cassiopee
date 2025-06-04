# Lire deux entiers N et C depuis l'entrée standard.
# input() lit une ligne de texte de l'utilisateur, split() découpe la ligne en morceaux (ici deux entiers), 
# map(int, ...) convertit chaque morceau en entier, puis les deux sont assignés à N et C.
N, C = map(int, input().split())

# Créer une liste de N éléments, où chaque élément est une liste de 2 entiers (x et v).
# Nous utilisons une compréhension de liste pour cette opération.
# Pour chaque itération dans la plage N, nous lisons une ligne, la découpons, la convertissons en entiers,
# et la stockons comme [x, v] pour représenter la position et la valeur.
xv = [list(map(int, input().split())) for _ in range(N)]

# Extraire la liste des positions (x) de chaque élément dans xv.
# Pour chaque indice i de 0 à N-1, prenons le premier élément de xv[i], qui correspond à x_i.
x = [xv[i][0] for i in range(N)]

# Extraire la liste des valeurs (v) de chaque élément dans xv.
# Pour chaque indice i de 0 à N-1, prenons le deuxième élément de xv[i], qui correspond à v_i.
v = [xv[i][1] for i in range(N)]

# Initialiser deux listes C1 et C2 qui serviront à stocker des valeurs maximisées vers la droite (aller)
# Ces deux listes auront toutes deux une taille de N et seront initialisées à 0.
C1 = [0] * N  # C1[i] correspondra à la valeur maximale en parcourant les i+1 premiers éléments, pénalisée par la distance parcourue (x)
C2 = [0] * N  # C2[i] correspondra à la même chose sauf que la pénalité par la distance est doublée

# Boucle pour construire les cumuls des valeurs v du début jusqu'à l'élément i compris
for i in range(N):
    # Si i == 0, C1[-1] ou C2[-1] renvoie le dernier élément de la liste, mais ici on les veut à 0 quand i == 0, donc les listes initialisées à 0 conviennent
    # Pour tous les i, on ajoute la valeur v[i] à la somme cumulative précédente (ou 0 si i == 0)
    C1[i] = C1[i - 1] + v[i]
    C2[i] = C2[i - 1] + v[i]
    # Après cette boucle, C1[i] et C2[i] contiennent la somme des v[0] à v[i]

# Parcourir tous les indices pour appliquer la pénalité de distance dans C1 et C2 :
for i in range(N):
    # Retirer la distance parcourue x[i] de la somme cumulée dans C1 (aller simple)
    C1[i] -= x[i]
    # Retirer le double de la distance dans C2 (aller-retour)
    C2[i] -= 2 * x[i]

# Cette boucle ajuste chaque C1[i] et C2[i] pour être le maximum de leur valeur actuelle et du maximum précédent
for i in range(1, N):
    # Pour chaque position i, on garde la meilleure valeur rencontrée jusque-là (max entre C1[i] actuel et maximum précédent)
    C1[i] = max(C1[i], C1[i - 1])
    C2[i] = max(C2[i], C2[i - 1])

# Initialiser deux listes D1 et D2 qui serviront à stocker les valeurs maximisées vers la gauche (retour)
# La logique est identique au cas aller, mais on commence à la fin (on inverse le parcours)
D1 = [0] * N  # D1[i] contiendra la valeur maximale pour les i+1 derniers éléments, pénalisée par la distance
D2 = [0] * N  # D2[i] contiendra la même logique mais la distance est doublée

# Construire les cumuls des valeurs v depuis la droite (fin) vers la gauche (début)
for i in range(N):
    # Le parcours s'effectue à l'envers : v[N-1], v[N-2], ..., v[0]
    D1[i] = D1[i - 1] + v[N - 1 - i]
    D2[i] = D2[i - 1] + v[N - 1 - i]

# Appliquer la pénalité de la distance sur les parcours retour
for i in range(N):
    # On prend la distance depuis la droite : C - x[N-1-i] (distance du point d'arrivée au point 0)
    D1[i] -= C - x[N - 1 - i]
    # Dans D2, la distance est doublée (aller-retour)
    D2[i] -= 2 * (C - x[N - 1 - i])

# Ajuster chaque D1[i] et D2[i] pour garantir que l'on conserve toujours la meilleure valeur cumulative jusqu'à i
for i in range(1, N):
    D1[i] = max(D1[i], D1[i - 1])
    D2[i] = max(D2[i], D2[i - 1])

# Initialiser la variable qui contiendra le maximum final à 0
ans = 0

# Parcourir tous les points pour comparer la meilleure valeur en allant depuis la gauche ou depuis la droite
for i in range(N):
    # À chaque point, ans prend la plus grande valeur entre ans, C1[i] (aller gauche), et D1[i] (aller droite)
    ans = max(ans, C1[i], D1[i])

# Combiner les résultats aller et retour pour des scénarios combinés
# Parcourir tous les points sauf le dernier (pour éviter duplication), considérer des allers-retours optimaux pris à un point de coupure
for i in range(N - 1):
    # Le joueur va à x[i] puis revient, puis va vers la droite, ou inversement, on prend le maximum de toutes ces combinaisons
    # Additionner les meilleurs résultats cumulés de chaque côté, en prenant soin d'éviter le double comptage
    ans = max(ans, C2[i] + D1[N - i - 2], D2[i] + C1[N - i - 2])

# Afficher la réponse maximale obtenue
print(ans)