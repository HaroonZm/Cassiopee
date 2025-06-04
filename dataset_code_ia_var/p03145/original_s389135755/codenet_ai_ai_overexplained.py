# Demande à l'utilisateur de saisir une ligne de texte, en général via le clavier.
# La fonction input() attend que l'utilisateur tape quelque chose et appuie sur Entrée.
# Le texte saisi sera retourné sous la forme d'une chaîne de caractères (type str).
user_input = input()

# Le texte saisi est séparé en plusieurs sous-chaînes à chaque espace.
# La méthode split() coupe la chaîne partout où elle trouve un espace et retourne une liste de chaînes.
# Par exemple, si l'utilisateur tape "3 4 5", split() donnera ["3", "4", "5"].
split_input = user_input.split()

# La fonction map() applique une fonction (ici int, pour convertir en entier) à chaque élément de la liste split_input.
# Cela transforme la liste de chaînes en une liste de nombres entiers.
# map(int, split_input) retourne un objet map, qui peut être utilisé comme un itérateur sur les entiers.
mapped_values = map(int, split_input)

# Les trois valeurs produites par map(int, split_input) sont extraites et stockées dans les variables a, b et c.
# On utilise l'affectation multiple (a, b, c =) pour cela. Cette syntaxe assigne successivement la première valeur à a, 
# la deuxième à b et la troisième à c.
a, b, c = mapped_values

# On multiplie la valeur de 'a' par celle de 'b'. L'opérateur * effectue la multiplication.
# Ensuite, on effectue une division entière de ce résultat par 2. L'opérateur // fait une division entière, 
# c'est-à-dire qu'il donne le quotient sans la partie décimale (par exemple, 7 // 2 donne 3).
# Finalement, le résultat calculé est envoyé à la fonction print(), qui affiche cette valeur à l'écran.
print(a * b // 2)