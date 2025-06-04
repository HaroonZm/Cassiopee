# Demande à l'utilisateur de saisir une ligne de texte via le clavier.
# La fonction input() lit tout ce que l'utilisateur écrit jusqu'à l'appui sur Entrée,
# et retourne cette saisie sous la forme d'une chaîne de caractères (string).
# Par exemple, si l'utilisateur tape "3 4", alors input() retournera la string "3 4".
user_input = input()

# La méthode split() est appelée sur la chaîne saisie afin de la découper en une liste de sous-chaînes (strings),
# en utilisant l'espace comme séparateur par défaut. Ainsi, "3 4" devient ['3', '4'].
split_input = user_input.split()

# La fonction map() applique la fonction spécifiée en premier argument (ici int, pour convertir en entier)
# à chaque élément de l'itérable fourni en second argument (ici split_input, la liste des strings issus du split).
# Cela retourne un itérable où chaque string de split_input est convertie en entier.
mapped_integers = map(int, split_input)

# On utilise l'affectation multiple (décomposition ou unpacking), ce qui permet d'attribuer en une seule instruction
# la première valeur de mapped_integers à 'a' et la seconde à 'b'.
# mapped_integers est converti en une séquence (comme une liste ou un tuple) pour permettre le déballage.
a, b = mapped_integers

# À ce stade, 'a' et 'b' sont deux variables de type entier (int) contenant les nombres saisis par l'utilisateur.

# On calcule ensuite le produit de 'a' et 'b' en utilisant l'opérateur *.
# Cette opération arithmétique multiplie la valeur de 'a' par celle de 'b' et produit un nouvel entier.
result = a * b

# Enfin, la fonction print() est appelée pour afficher le résultat de la multiplication à l'écran.
# print() convertit automatiquement l'entier result en une chaîne de caractères pour l'affichage
# et l'écrit sur la sortie standard (habituellement la console, là où on a lancé le script).
print(result)