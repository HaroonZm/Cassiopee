# Prend une ligne d'entrée de l'utilisateur, qui est supposée contenir deux nombres séparés par un espace.
# La fonction input() lit cette ligne sous forme de chaîne de caractères.
# Par exemple, si l'utilisateur écrit "3 5", input() retournera la chaîne "3 5".
input_string = input()

# split() coupe la chaîne en une liste de sous-chaînes, séparées par des espaces par défaut.
# Ainsi, "3 5" devient ['3', '5'].
string_list = input_string.split()

# map(int, string_list) applique la fonction int() à chaque élément de string_list.
# int() convertit une chaîne représentant un nombre en un entier Python.
# Cela transforme ['3', '5'] en [3, 5] (une liste d'entiers).
mapped_list = map(int, string_list)

# list() convertit le map object en liste réelle, qu'on peut indexer.
# Au final, s contiendra les deux entiers entrés par l'utilisateur.
s = list(mapped_list)

# s[0] représente le premier nombre de la liste (indexation à partir de 0, la première position).
# s[1] représente le deuxième nombre de la liste.

# On veut calculer la moyenne arithmétique entière de ces deux nombres.
# Pour cela, on additionne les deux nombres : s[0] + s[1]
sum_of_numbers = s[0] + s[1]

# On divise cette somme par 2, pour obtenir la moyenne.
# Le signe / réalise une division flottante, donc le résultat pourrait être un nombre à virgule flottante (float).
average = sum_of_numbers / 2

# La fonction int() convertit la moyenne en un entier, en tronquant la partie décimale (partie après la virgule).
# Par exemple, int(4.7) va donner 4, car int() retire tout ce qui suit la virgule.
avr = int(average)

# print() affiche la valeur de avr dans la console, c'est-à-dire la moyenne entière des deux nombres.
print(avr)