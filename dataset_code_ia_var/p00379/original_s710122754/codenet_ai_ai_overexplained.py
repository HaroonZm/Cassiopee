# Création d'une liste vide nommée 'list' pour stocker les puissances de nombres entiers
list = []

# Lecture de trois entiers séparés par des espaces depuis l'entrée standard
# La fonction input() lit une ligne de texte, split() la divise en éléments selon les espaces
# map applique la fonction int() à chaque élément pour les convertir en entiers
# Les trois valeurs sont ensuite affectées respectivement à 'a', 'n' et 's'
a, n, s = map(int, input().split())

# Création d'une liste vide nommée 'ans' qui servira à stocker les résultats finaux
ans = []

# Boucle for qui va itérer de 1 jusqu'à 10000 inclus (mais range s'arrête avant 10001)
for i in range(1, 10001):
    # Calcul de i élevé à la puissance n à l'aide de l'opérateur **
    # Vérification si cette puissance est inférieure ou égale à s
    if i ** n <= s:
        # Ajout de la valeur de i puissance n à la liste 'list'
        list.append(i ** n)

# Boucle pour parcourir chaque élément (puissance) de la liste 'list'
for i in list:
    # Conversion de l'entier 'i' en une chaîne de caractères pour itérer sur chaque chiffre
    k = str(i)
    # Copie la valeur de 'a' dans une nouvelle variable 'd' pour la modifier localement
    d = a
    # Boucle sur chaque caractère (chiffre écrit en lettre) de la chaîne 'k'
    for j in k:
        # Conversion du caractère 'j' en entier, puis ajout à la variable 'd'
        d += int(j)
    # Après la boucle sur chaque chiffre de 'i', on élève 'd' à la puissance 'n' et compare avec 'i'
    if d ** n == i:
        # Si l'égalité est vraie, on ajoute 'i' à la liste des réponses 'ans'
        ans.append(i)

# Affichage final du nombre d'éléments dans la liste 'ans', c'est-à-dire la longueur de la liste
print(len(ans))