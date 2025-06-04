# La fonction print affiche une valeur à l'écran, c'est-à-dire qu'elle affiche une chaîne de caractères ou toute autre valeur passée en argument.
# Ici, nous utilisons la version print avec la syntaxe Python 2, sans parenthèses.
# La fonction raw_input() lit une ligne de texte saisie par l'utilisateur dans la console (entrée standard).
# Elle attend que l'utilisateur saisisse quelque chose au clavier puis appuie sur Entrée.
# Le texte saisi par l'utilisateur est renvoyé par raw_input() sous forme d'une chaîne de caractères (str).
# L'expression raw_input()[::-1] utilise le *slicing* (tranchage) sur la chaîne obtenue.
# Le *slicing* s'écrit sous la forme [début:fin:pas], ici:
#   - début n'est pas spécifié, donc commence au début de la chaîne
#   - fin n'est pas spécifié, donc va jusqu'à la fin de la chaîne
#   - pas est -1, donc on parcourt la chaîne de la fin vers le début, ce qui la renverse
# Ainsi raw_input()[::-1] renverse la chaîne saisie par l'utilisateur.
# Enfin, print affiche cette chaîne renversée à l'écran.

print raw_input()[::-1]