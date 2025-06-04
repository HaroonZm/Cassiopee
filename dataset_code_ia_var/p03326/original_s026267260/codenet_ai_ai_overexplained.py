import numpy as np  # Importe le module numpy, qui fournit des structures et fonctions avancées pour des opérations numériques (par exemple, tableaux multidimensionnels)

# Lecture depuis l'entrée standard : input() lit une ligne saisie par l'utilisateur
# La variable contient une chaîne comme "3 2" qu'on découpe en une liste avec split(' ')
N, M = input().split(' ')

# Conversion des nombres lus, de chaîne de caractères en entiers avec int()
N = int(N)  # Nombre d'éléments à lire pour x, y, z
M = int(M)  # Nombre d'éléments à garder pour le calcul ultérieur

# Création de trois listes vides. On utilisera ces listes pour stocker les valeurs de x, y, et z
x_arr = []  # Liste pour stocker les composantes x de chaque point lu
y_arr = []  # Liste pour les valeurs y
z_arr = []  # Liste pour les valeurs z

# Boucle for pour traiter N fois, i.e. pour chaque triplet de coordonnées
for i in range(N):
    # On lit sur l'entrée standard une ligne, qui contient trois valeurs séparées par des espaces
    x, y, z = input().split(' ')  # On sépare cette ligne en trois chaînes x, y et z

    # Conversion de chaque valeur chaîne en entier
    x = int(x)
    y = int(y)
    z = int(z)

    # On ajoute la valeur x à la fin de la liste x_arr
    x_arr.append(x)
    # Pareil pour y et z
    y_arr.append(y)
    z_arr.append(z)

# À ce stade, x_arr, y_arr et z_arr sont des listes Python classiques contenant chacun N entiers

# On transforme ces listes en tableaux numpy pour profiter des opérations vectorielles efficaces de numpy
x_arr = np.array(x_arr)  # Convertit la liste x_arr en tableau numpy
y_arr = np.array(y_arr)
z_arr = np.array(z_arr)

# Pour chaque combinaisons de signe (au nombre de 8), on calcule une nouvelle combinaison linéaire des vecteurs x/y/z

# Première combinaison : on additionne tous les termes pour chaque index i (x_i + y_i + z_i)
xyz1 = x_arr + y_arr + z_arr

# On trie les valeurs obtenues par ordre croissant avec np.sort (du plus petit au plus grand)
xyz1 = np.sort(xyz1)[::-1]  # Le [::-1] inverse le tableau, donnant ainsi un tri décroissant

# Somme des M plus grandes valeurs : on sélectionne les M premiers éléments du tableau trié ([:M:])
xyz1_sum = np.sum(xyz1[:M:])

# Deuxième combinaison : x+y-z
xyz2 = x_arr + y_arr - z_arr
xyz2 = np.sort(xyz2)[::-1]
xyz2_sum = np.sum(xyz2[:M:])

# Troisième : x-y-z
xyz3 = x_arr - y_arr - z_arr
xyz3 = np.sort(xyz3)[::-1]
xyz3_sum = np.sum(xyz3[:M:])

# Quatrième : x-y+z
xyz4 = x_arr - y_arr + z_arr
xyz4 = np.sort(xyz4)[::-1]
xyz4_sum = np.sum(xyz4[:M:])

# Cinquième : -x-y+z
xyz5 = -x_arr - y_arr + z_arr
xyz5 = np.sort(xyz5)[::-1]
xyz5_sum = np.sum(xyz5[:M:])

# Sixième : -x+y+z
xyz6 = -x_arr + y_arr + z_arr
xyz6 = np.sort(xyz6)[::-1]
xyz6_sum = np.sum(xyz6[:M:])

# Septième : -x+y-z
xyz7 = -x_arr + y_arr - z_arr
xyz7 = np.sort(xyz7)[::-1]
xyz7_sum = np.sum(xyz7[:M:])

# Huitième : -x-y-z
xyz8 = -x_arr - y_arr - z_arr
xyz8 = np.sort(xyz8)[::-1]
xyz8_sum = np.sum(xyz8[:M:])

# On rassemble toutes les sommes calculées dans une liste, a
a = [xyz1_sum, xyz2_sum, xyz3_sum, xyz4_sum, xyz5_sum, xyz6_sum, xyz7_sum, xyz8_sum]

# On affiche le maximum de cette liste.
# La fonction max retourne la plus grande valeur de la liste, qui correspond à la solution finale recherchée
print(max(a))