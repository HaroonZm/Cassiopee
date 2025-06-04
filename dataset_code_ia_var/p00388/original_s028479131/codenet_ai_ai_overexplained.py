# Demande à l'utilisateur d'entrer trois nombres séparés par des espaces.
# La fonction input() lit la saisie de l'utilisateur sous forme de chaîne de caractères (string).
# La méthode split() découpe cette chaîne au niveau des espaces, ce qui retourne une liste de sous-chaînes.
# La fonction map() applique la fonction int à chaque élément de cette liste 
# afin de convertir chaque sous-chaîne (qui représente un nombre) en un entier (integer).
# Enfin, les trois entiers sont affectés respectivement aux variables h, a, et b.
h, a, b = map(int, input().split())

# On initialise une variable nommée 'ans' à 0.
# Cette variable va servir de compteur pour compter combien de nombres dans l'intervalle [a, b]
# divisent exactement (c'est-à-dire sans laisser de reste) la valeur de h.
ans = 0

# On crée une boucle for afin d'examiner chaque entier, noté i,
# allant de la valeur de 'a' jusqu'à la valeur égale à 'b' incluse.
# La fonction range(a, b + 1) génère une séquence d'entiers débutant à a et s'arrêtant à b (car la borne supérieure est exclusive).
for i in range(a, b + 1):
    # À l'intérieur de la boucle, on utilise l'opérateur modulo '%' pour vérifier si h est divisible par i.
    # L'expression 'h % i' calcule le reste de la division entière de h par i.
    # Si ce reste est nul (c'est-à-dire égal à 0), alors cela signifie que i est un diviseur de h.
    if h % i == 0:
        # Si la condition ci-dessus est vraie, cela veut dire que i divise h exactement.
        # On incrémente alors la variable 'ans' de 1, c'est-à-dire qu'on ajoute 1 à son ancienne valeur.
        ans += 1

# Après que la boucle for a examiné tous les nombres de a à b inclus,
# on utilise la fonction print() pour afficher la valeur finale de 'ans'.
# Cette valeur représente le nombre total d'entiers dans l'intervalle [a, b] qui divisent h sans reste.
print(ans)