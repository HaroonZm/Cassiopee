# Affiche à l'écran la chaîne de caractères saisie par l'utilisateur, mais à l'envers
# Importante note : ce code est pour Python 2. En Python 3, utilisez 'input()' à la place de 'raw_input()'.

# Appelons la fonction 'raw_input()'.
# 'raw_input()' affiche une invite à l'utilisateur pour saisir une ligne de texte.
# Sans arguments, 'raw_input()' n'affiche pas de message avant la saisie.
# Elle attend que l'utilisateur tape une ligne de texte (jusqu'à appui sur Entrée).
# Le texte saisi est récupéré comme une chaîne de caractères (type 'str').
# On obtient donc la chaîne saisie par l'utilisateur.
# Exemple : si l'utilisateur saisit "bonjour", 'raw_input()' renvoie "bonjour".
# On applique ensuite un 'slice' sur cette valeur pour inverser la chaîne.
# Le slice '[: : -1]' signifie :
# - Le premier ':' indique qu'on utilise toute la chaîne, du début à la fin.
# - Le second ':' indique le pas (step), qui est ici -1 : cela signifie qu'on parcourt la chaîne à l'envers.
# Donc 'chaine[:: -1]' retourne la chaîne renversée caractère par caractère.
# Exemple : "abc"[:: -1] renvoie "cba".
# Enfin, on affiche cette chaîne inversée à l'aide de la fonction 'print'.
# 'print' en Python 2 affiche l'expression passée entre parenthèses (ou sans parenthèses).
# Ici, il affiche directement la chaîne inversée retournée par l'appel de 'raw_input()' puis slicing.

print raw_input()[::-1]