n = int(input())
h = [int(input()) for _ in range(n)]
h.sort(reverse=True)

# On calcule la somme des diamètres des "zones" de mouvement de chaque soldat.
# Chaque soldat peut couvrir toutes les cases dans un rayon égal à sa force (h_i).
# La zone couverte par un soldat avec h_i d'énergie est un diamant de rayon h_i,
# la taille du diamant étant 2*h_i + 1 sur un axe.
# L'ensemble des zones est la somme des diamètres moins les chevauchements,
# mais on ne peut pas chevaucher plus que la distance entre 2 chemins.
# Dans ce cas, la zone maximale peut être calculée en sommant 2*h_i+1 puis en soustrayant
# les chevauchements. En pratique, cela revient à:
# L'étendue maximale est reach = somme des h_i.
# Donc la taille maximale est 2*reach +1 (car en partant du centre on peut aller reach cases de chaque côté).

total_h = sum(h)
# la zone maximale est la taille du plus grand diamant couvrant tous les déplacements
# Cette zone correspond au nombre de cases dans un diamant de rayon total_h:
# Nombre de cases dans un diamant de rayon r = 2*r*r + 2*r +1
# Mais nous devons vérifier si c'est correct.

# En réalité, la zone accessible par un soldat est le nombre de cases dans un diamant de rayon h_i:
# nombre_cases = 2*h_i*(h_i+1) +1
# L'union des positions atteignables par tous les soldats en partant d'un même point
# est un diamant de rayon sum(h_i).
# Le nombre de cases dans un diamant de rayon R est 2*R*(R+1)+1

R = total_h
result = 2*R*(R+1)+1

print(result)