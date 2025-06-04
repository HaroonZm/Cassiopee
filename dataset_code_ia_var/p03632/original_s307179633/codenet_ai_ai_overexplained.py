# Prendre quatre entiers a, b, c et d depuis l'entrée utilisateur
# La fonction input() lit une ligne depuis l'entrée standard (habituellement le clavier)
# split() divise la chaîne d'entrée autour des espaces, produisant une liste de chaînes
# map(int, ...) convertit chaque chaîne de la liste en entier
# Les quatre entiers sont affectés respectivement aux variables a, b, c, d par décomposition
a, b, c, d = map(int, input().split())

# Initialiser une liste de 100 éléments tous égaux à zéro
# [0]*100 crée une liste où chaque élément est le nombre entier zéro
li = [0] * 100

# Boucler sur tous les entiers de a (inclus) jusqu'à b (exclus)
# range(a, b) génère une séquence d'entiers débutant à a jusqu'à b-1
for i in range(a, b):
    # Pour chaque entier i dans ce range, augmenter la valeur li[i] de 1
    # Cela marque que l'index i a été traversé lors de ce premier intervalle
    li[i] += 1

# Boucler sur tous les entiers de c (inclus) jusqu'à d (exclus)
# range(c, d) fonctionne de la même façon mais pour l'autre segment
for i in range(c, d):
    # Pour chaque entier i de ce second intervalle, augmenter li[i] de 1
    # Cela ajoute un passage supplémentaire à l'indice i du tableau
    li[i] += 1

# Compter combien d'éléments de la liste li sont exactement égaux à 2
# li.count(2) compte combien de fois la valeur 2 apparaît dans la liste li
# Cela correspond aux indices qui ont été visités par les deux intervalles
print(li.count(2))
# Affiche le résultat à l'utilisateur : le nombre d'entiers inclus dans les deux intervalles [a, b) et [c, d)