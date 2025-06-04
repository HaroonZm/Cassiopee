# Lecture des trois premiers entiers depuis l'entrée standard (utilisateur)
# La fonction input() lit une ligne de texte fournie par l'utilisateur.
# split() divise cette ligne en différentes parties selon les espaces.
# map(int, ...) transforme chaque morceau de texte en un entier.
# Les trois entiers sont affectés dans les variables n, h et w.
n, h, w = map(int, input().split())

# Initialisation d'une liste vide qui contiendra des sous-listes.
ab = []  # Cette liste va contenir n sous-listes, chacune de deux entiers.

# Boucle pour répéter n fois, de i=0 à i=n-1.
for i in range(n):
    # Lecture d'une ligne d'entrée utilisateur, qui est supposée contenir deux entiers séparés par un espace.
    line = input()
    # split() divise la ligne donnée en une liste de chaînes sur les espaces.
    # map(int, ...) convertit chaque élément de cette liste de chaînes en entier.
    # list(...) transforme le map en une liste d'entiers.
    l = list(map(int, line.split()))
    # Append ajoute la liste l à la liste principale ab.
    ab.append(l)

# Initialisation de la variable ans à zéro.
# Cette variable va compter combien de paires satisfont une certaine condition.
ans = 0

# Pour chaque élément de la liste ab, qui est une sous-liste de deux éléments [a, b] :
for a, b in ab:
    # On vérifie si a est supérieur ou égal à h, c'est-à-dire si le premier élément dépasse ou égale la valeur h.
    # On vérifie aussi si b est supérieur ou égal à w; c'est la même logique pour le second élément.
    if a >= h and b >= w:
        # Si les deux conditions précédentes sont vraies, alors on incrémente ans de 1.
        # Cela veut dire qu'on a trouvé une paire (a, b) qui respecte les deux contraintes.
        ans += 1

# Affichage du résultat final avec la fonction print.
# Le nombre total de paires qui satisfont les conditions imposées sera affiché à l'écran.
print(ans)