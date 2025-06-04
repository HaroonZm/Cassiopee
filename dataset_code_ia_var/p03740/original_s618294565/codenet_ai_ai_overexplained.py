# Demander à l'utilisateur de saisir deux valeurs séparées par un espace sur une seule ligne.
# La fonction input() lit cette ligne de texte saisie par l'utilisateur sous forme de chaîne de caractères (string).
# La méthode split() découpe cette chaîne aux espaces, renvoyant une liste de chaînes correspondant aux éléments saisis.
# La fonction map(int, ...) applique la conversion en entier (int) à chaque élément de la liste, pour obtenir deux entiers au lieu de deux chaînes.
# L'affectation multiple (x, y = ...) attribue le premier entier à la variable x et le second à la variable y.
x, y = map(int, input().split())

# On souhaite comparer les valeurs absolues de la différence entre x et y.
# La fonction abs() retourne la valeur absolue (toujours positive ou nulle) de l'argument fourni.
# L'expression abs(x - y) évalue la différence entre x et y puis convertit cette différence en valeur absolue.
# On vérifie si cette différence (toujours positive ou nulle) est strictement supérieure à 1.
# L'opérateur > compare si la valeur gauche est supérieure à la valeur droite.
# Si c'est vrai, alors l'expression conditionnelle retourne "Alice", sinon elle retourne "Brown".
# Cette expression conditionnelle est une forme raccourcie d'instruction if-else en une ligne.
# La fonction print() affiche le texte final à l'écran, qui sera soit "Alice", soit "Brown" selon la condition précédente.
print("Alice" if abs(x - y) > 1 else "Brown")