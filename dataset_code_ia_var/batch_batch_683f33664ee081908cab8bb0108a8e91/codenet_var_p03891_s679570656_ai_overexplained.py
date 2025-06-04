# Définition de la variable 'i' qui référence la fonction input intégrée, permettant de lire une entrée utilisateur sous forme de chaîne de caractères.
i = input

# Lecture de la première entrée utilisateur via la fonction 'i()', qui stocke la valeur dans la variable 'a'.
a = i()
# Lecture de la deuxième entrée utilisateur, stockée dans la variable 'b'.
b = i()
# Lecture de la troisième entrée utilisateur, stockée dans la variable 'c'.
c = i()

# Calcul d'une nouvelle valeur 'd' en effectuant une opération arithmétique :
# D'abord, '2*c' multiplie la variable 'c' par 2 (c'est la multiplication d'un nombre par 2).
# Ensuite, '2*c - a' soustrait la variable 'a' du résultat précédent.
# Puisqu'i() retourne par défaut des chaînes, il faut convertir a et c en entiers pour effectuer cette opération mathématique.
d = 2 * int(c) - int(a)

# Calcul d'une nouvelle valeur 'e' :
# Soustrait la valeur de la variable 'b' à la valeur de la variable 'c'.
# Encore une fois, conversion de 'b' et 'c' en entiers afin de pouvoir soustraire des nombres.
e = int(c) - int(b)

# Premier affichage :
# On affiche trois valeurs séparées par des espaces.
# print prend en charge l'affichage d'arguments multiples en les séparant par des espaces, même s'il s'agit de différents types (chaînes, entiers).
# 'a' et 'b' sont encore des chaînes de caractères; 'e+d' est le résultat d'une addition de deux entiers.
# Pour effectuer 'e+d', on additionne les valeurs entières de 'e' et 'd'.
# Cependant, pour afficher correctement et éviter une erreur de concaténation, on doit convertir a et b en chaînes si on veut les mélanger avec des entiers dans print.
print(a, b, e + d)

# Deuxième affichage :
# Affiche trois valeurs: 
# '2*d-b' réalise la multiplication 2*d (doubler la valeur de d), puis enlève la valeur de b.
# 'c' est la valeur de la variable c.
# 'a+b-d' commence par additionner les valeurs de a et b, puis soustrait d au total.
# Il faut convertir correctement les variables en entiers pour les opérations arithmétiques.
print(2 * d - int(b), c, int(a) + int(b) - d)

# Troisième affichage :
# Imprime la valeur de 'a', puis 'c+e', puis 'd'.
# Pour 'c+e', additionne la valeur entière de c à e.
print(a, int(c) + e, d)