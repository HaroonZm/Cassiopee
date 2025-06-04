# On commence par lire trois valeurs entières séparées par des espaces à partir de l'entrée standard (typiquement le clavier).
# La fonction input() permet de lire une ligne de texte à l'écran. La méthode split() sépare cette chaîne en morceaux selon les espaces.
# La fonction map(int, ...) convertit chaque morceau en entier.
# Enfin, l'affectation multiple w, h, n = ... range chaque valeur convertie dans l'une des trois variables : w, h, n.
w, h, n = map(int, input().split())

# On lit maintenant deux autres entiers qui correspondent aux coordonnées initiales (x, y).
# Le même principe de lecture, séparation, conversion et affectation s'applique ici.
x, y = map(int, input().split())

# On initialise une variable a à 0. Cette variable servira à accumuler un total (somme), dans ce cas la distance totale calculée.
a = 0

# On souhaite répéter un certain nombre de fois les opérations suivantes : il faut traiter n-1 points (parce qu'on a déjà lu le premier point).
# La fonction range(n-1) génère une séquence de valeurs allant de 0 à n-2 (soit n-1 valeurs), ce qui permet d'itérer n-1 fois.
for _ in range(n-1):
    # À chaque itération, on lit deux entiers représentant les coordonnées du point suivant : (px, py).
    px, py = map(int, input().split())
    
    # On calcule la différence horizontale dx entre le point actuel px et le point précédent x.
    dx = px - x
    # On calcule la différence verticale dy entre le point actuel py et le point précédent y.
    dy = py - y
    
    # Si dx et dy ont des signes opposés (l'un est positif, l'autre négatif, ou inversement),
    # alors leur produit sera négatif.
    # Par exemple, si dx=3 et dy=-2, alors dx*dy=-6<0, donc ils ont des signes opposés.
    if dx * dy < 0:
        # Si c'est le cas, on additionne la valeur absolue de dx et la valeur absolue de dy,
        # c'est-à-dire, on somme les déplacements en x et y, en ignorant le signe.
        # map(abs, [dx, dy]) applique la fonction abs (valeur absolue) à chaque élément de la liste [dx, dy].
        # sum(...) fait la somme des deux résultats.
        a += sum(map(abs, [dx, dy]))
    else:
        # Sinon, cela signifie que dx et dy ont le même signe (tous les deux positifs, tous les deux négatifs, ou l'un d'eux est nul),
        # donc ils sont dans le même quadrant ou en ligne droite.
        # On prend alors le maximum des valeurs absolues de dx et dy, c'est-à-dire le plus grand déplacement sur un des axes.
        a += max(map(abs, [dx, dy]))
    
    # On met ensuite à jour la position actuelle (x, y) pour la prochaine itération du boucle.
    x, y = px, py

# Enfin, après avoir parcouru tous les points, on affiche le résultat final stocké dans la variable a.
# La fonction print(a) affiche la valeur de a à l'écran.
print(a)