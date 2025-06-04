from sys import stdin  # Importe l'objet 'stdin' du module 'sys', permettant de lire des entrées depuis l'entrée standard (par défaut, le clavier)

# Initialisation de quatre variables entières à 0. 
# tri : compteur général de triangles valides rencontrés.
# rig : compteur des triangles rectangles.
# small : compteur des triangles acutangles (tous angles < 90°).
# large : compteur des triangles obtusangles (un angle > 90°).
tri = 0
rig = 0
small = 0
large = 0

# Boucle pour traiter chaque ligne d'entrée lue depuis l'entrée standard (par exemple via fichier ou clavier)
for line in stdin:
    # Sépare la ligne d'entrée en éléments par espace, convertit chaque élément en entier avec map(int, ...)
    # Puis transforme le map en liste, donc 'line' devient une liste de trois entiers.
    line = list(map(int, line.split()))
    
    # Trie la liste des trois côtés par ordre croissant (en place).
    # Après le tri, line[0] <= line[1] <= line[2] est garanti.
    line.sort()
    
    # Vérifie si la somme des deux côtés les plus courts (line[0] + line[1]) 
    # est inférieure ou égale au plus long côté (line[2]); dans ce cas, la condition du triangle n'est pas respectée.
    # On arrête alors la lecture et la boucle avec break.
    if line[0] + line[1] <= line[2]:
        break

    # Incrémente le compteur total de triangles valides rencontrés jusqu'ici.
    tri += 1

    # Calcule la différence entre la somme des carrés des deux plus petits côtés 
    # et le carré du plus grand côté, c'est-à-dire : a² + b² - c²
    tmp = line[0] ** 2 + line[1] ** 2 - line[2] ** 2

    # Si la valeur calculée (tmp) est exactement zéro, 
    # le triangle est rectangle (théorème de Pythagore).
    if tmp == 0:
        rig += 1  # Incrémente le compteur de triangles rectangles.
    # Si la valeur calculée (tmp) est négative, alors le triangle est obtusangle (un angle > 90°).
    elif tmp < 0:
        large += 1  # Incrémente le compteur de triangles obtusangles.
    # Sinon, c'est-à-dire si tmp > 0, le triangle est acutangle (tous les angles < 90°).
    else:
        small += 1  # Incrémente le compteur de triangles acutangles.

# Affiche les quatre compteurs sur une seule ligne, séparés par des espaces :
# - total de triangles (tri)
# - triangles rectangles (rig)
# - triangles acutangles (small)
# - triangles obtusangles (large)
print(tri, rig, small, large)