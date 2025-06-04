# Demande à l'utilisateur de saisir une valeur, lit l'entrée sous forme de chaîne de caractères,
# puis convertit cette chaîne en entier à l'aide de la fonction int().
# Le résultat est stocké dans la variable A.
A = int(input())

# Répète le même processus pour la variable B.
B = int(input())

# Lit une troisième entrée de l'utilisateur, la convertit en entier
# et la stocke dans la variable C.
C = int(input())

# Fait de même pour la variable D.
D = int(input())

# Utilise la fonction min() pour trouver la plus petite valeur entre A et B.
# La fonction min() prend deux arguments et renvoie celui qui est le plus petit.
# La valeur minimale est stockée dans la variable min1.
min1 = min(A, B)

# Répète l'opération précédente, cette fois-ci entre les variables C et D.
# Stocke le minimum des deux dans min2.
min2 = min(C, D)

# Additionne les deux plus petites valeurs trouvées précédemment (min1 et min2).
# Utilise la fonction print() pour afficher le résultat de cette addition à l'écran.
print(min1 + min2)