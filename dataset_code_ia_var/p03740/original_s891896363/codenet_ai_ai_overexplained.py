# Demande à l'utilisateur de saisir une ligne de texte
# La fonction input() affiche une invite et attend la saisie de l'utilisateur
# Après la saisie, input() retourne la chaîne de caractères tapée par l'utilisateur
# La méthode split() coupe cette chaîne de caractères en plusieurs sous-chaînes (mots) en utilisant l'espace par défaut comme séparateur
# La fonction map() applique la fonction int à chaque sous-chaîne, c'est-à-dire convertit chaque chaîne en un entier
# Le résultat de map() est un itérable de ces entiers
# Enfin, affecte le premier entier à la variable x et le second à la variable y en utilisant l'affectation multiple
x, y = map(int, input().split())

# Calcule la différence entre x et y en valeur absolue
# La fonction abs() retourne la valeur absolue, c'est-à-dire la valeur sans le signe négatif
# On compare cette valeur à 1 pour vérifier si elle est strictement supérieure à 1
# Si c'est le cas, exécute le code qui suit dans le bloc if
if abs(x - y) > 1:
    # Affiche la chaîne de caractères 'Alice' suivie d'un saut de ligne
    # print() affiche du texte à l'écran
    print('Alice')

# Calcule encore la différence absolue entre x et y
# Cette fois, on vérifie si elle est inférieure ou égale à 1
# <= est l'opérateur de comparaison "inférieur ou égal"
# Si la condition est vraie, exécute le code suivant
if abs(x - y) <= 1:
    # Affiche la chaîne de caractères 'Brown' suivie d'un saut à la ligne
    print('Brown')