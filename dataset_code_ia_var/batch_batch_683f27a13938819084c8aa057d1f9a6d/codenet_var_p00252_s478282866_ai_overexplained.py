# Demande à l'utilisateur de saisir une ligne de texte, généralement des nombres séparés par des espaces
# La fonction input() attend que l'utilisateur entre des données au clavier et appuie sur Entrée
# split() coupe la chaîne de caractères entrée par l'utilisateur en morceaux séparés par des espaces
# map() applique la fonction int à chaque élément découpé afin de convertir chaque morceau en entier
# Les trois valeurs entières sont ensuite affectées respectivement aux variables a, b et c grâce à l'affectation multiple
a, b, c = map(int, input().split())

# On commence un bloc conditionnel pour exécuter des instructions selon les valeurs des variables

# Premier test : vérifie si la variable a est exactement égale à 1
# L'opérateur == teste l'égalité (à ne pas confondre avec = qui sert à l'affectation)
# On utilise "and" pour ne passer dans le bloc suivant que si les deux conditions sont VRAIES simultanément
# Cela veut dire : a doit être égal à 1 ET b doit aussi être égal à 1
if a == 1 and b == 1:
    # Si a et b sont tous les deux égaux à 1, on affiche le texte "Open" à l'écran avec la fonction print
    print("Open")

# Sinon, si la condition précédente (a == 1 and b == 1) n'est pas remplie,
# on vérifie une autre condition grâce à "elif", ce qui veut dire "else if"
# Ici, on vérifie si c est exactement égal à 1
elif c == 1:
    # Si c est égal à 1, alors on affiche le texte "Open"
    print("Open")

# Si aucune des conditions précédentes n'est vraie (c'est-à-dire que ni a == 1 and b == 1, ni c == 1),
# on exécute le bloc else, qui s'applique à tous les autres cas possibles
else:
    # Ce bloc affiche le texte "Close" à l'écran, indiquant un cas différent des deux précédents
    print("Close")