# Demande à l'utilisateur de saisir une ligne de texte via le clavier.
# La fonction raw_input() lit cette ligne de texte et la retourne comme une chaîne de caractères.
# split() divise cette chaîne en une liste de sous-chaînes, séparées par des espaces.
# map(int, ...) applique la fonction int à chaque sous-chaîne, les convertissant en nombres entiers.
# Les deux entiers obtenus sont affectés respectivement aux variables A et B.
A, B = map(int, raw_input().split())

# Effectue la division entière de A par B.
# L'opérateur '/' en Python 2 effectue une division entière si les deux opérandes sont des entiers.
# Le résultat de cette division est stocké dans la variable ans.
ans = A / B

# Vérifie si le résultat de la division entière est négatif ET s'il existe un reste non nul dans la division A / B.
# A % B calcule le reste de la division entière de A par B.
# On s'assure que ce code fonctionne comme un arrondi vers zéro pour certaines divisions négatives.
if ans < 0 and A % B != 0:
    # Si la condition précédente est vraie (résultat négatif avec un reste non nul),
    # on ajoute 1 à ans pour corriger l'arrondi vers le bas,
    # ce qui permet de se rapprocher de l'arrondi plafond (arrondi vers le haut pour négatif).
    ans += 1

# Affiche la valeur de ans à l'écran.
# La fonction print en Python 2 s'utilise sans parenthèse.
print ans