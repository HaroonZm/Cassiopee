# Demande à l'utilisateur d'entrer trois entiers séparés par des espaces.
# raw_input() lit une ligne de texte saisie par l'utilisateur depuis l'entrée standard (généralement le clavier).
# split() divise cette ligne en fonction des espaces et renvoie une liste de chaînes.
# map(int, ...) convertit chaque élément de la liste (qui sont des chaînes) en entiers.
# w : largeur, h : hauteur, n : nombre d'itérations ou points.
w, h, n = map(int, raw_input().split())

# Demande à l'utilisateur d'entrer deux entiers pour a et b.
# a et b peuvent représenter par exemple des coordonnées initiales ou un premier point.
a, b = map(int, raw_input().split())

# Initialise une variable ans à zéro.
# Cette variable va accumuler le résultat final à afficher.
ans = 0

# Début d'une boucle for pour itérer sur un certain nombre de points/étapes.
# xrange(n-1) crée un générateur qui donne les entiers de 0 à n-2 (inclus).
# Cela permet d'effectuer (n-1) itérations, probablement pour traiter tous les points sauf le premier déjà lu.
for i in xrange(n-1):

    # Pour chaque itération, lit deux entiers x et y de l'utilisateur.
    # Ces valeurs représentent probablement des coordonnées ou des étapes successives dans le problème.
    x, y = map(int, raw_input().split())

    # Calcul du coût ou d'une mesure d'une certaine opération en relation avec les points (a, b) et (x, y).
    # Décomposons le calcul :
    # 1. abs(y-x + a-b) : différence absolue entre y-x et a-b (addition).
    # 2. min(abs(y-b), abs(x-a)) : minimum entre le déplacement du y actuel vers b ou x actuel vers a.
    # On ajoute les deux, puis on prend le minimum avec le cas où l'on se déplace directement
    # de (a, b) à (x, y) ou l'inverse via abs(x-a) + abs(y-b).
    # Ce calcul prend en compte deux manières d'aller d'un point à l'autre, pour choisir la plus courte ou la moins coûteuse.
    ans += min(
        abs(y - x + a - b) + min(abs(y - b), abs(x - a)),
        abs(x - a) + abs(y - b)
    )

    # On met à jour les variables a et b pour le prochain tour de boucle à partir des x et y lus.
    # Cela permet à la prochaine itération de calculer le déplacement à partir du point actuel.
    a, b = x, y

# Après la boucle, on affiche le résultat final accumulé dans ans.
# print permet d'afficher la valeur de ans à l'écran.
print ans