# Demande à l'utilisateur de saisir une valeur entière qui sera stockée dans la variable n
# La fonction int() convertit la chaîne de caractères obtenue avec input() en un entier
n = int(input())

# Demande à l'utilisateur de saisir deux entiers séparés par un espace
# Les deux valeurs saisies sont divisées à l'aide de input().split(), puis chacune est convertie en entier via map(int, ...)
# L'opération d'affectation multiple permet de stocker la première valeur dans a et la seconde dans b
a, b = map(int, input().split())

# Même principe que précédemment : demande de saisir deux autres entiers, stockés dans c et d
c, d = map(int, input().split())

# Les valeurs de a, b, c et d sont décrémentées de 1 pour passer à une base d'index allant de 0 à n-1 au lieu de 1 à n
# Cela est utile si l'on souhaite utiliser des indices dans des structures de données comme les listes en Python
a -= 1
b -= 1
c -= 1
d -= 1

# Définition d'une fonction nommée f, qui prend trois paramètres : x, y et z
def f(x, y, z):
    # Args :
    #   x (int): première valeur entière (peut être vue comme une position ou un indice)
    #   y (int): deuxième valeur entière
    #   z (int): valeur entière qui va influencer la division et le modulo
    # La fonction retourne la somme des valeurs absolues de deux différences :
    #   - La différence des résultats de la division entière de x et y par (z + 1)
    #   - La différence des restes de la division de x et y par (z + 1)
    # Cela calcule une sorte de "distance", dépendant de z
    return abs(x // (z + 1) - y // (z + 1)) + abs(x % (z + 1) - y % (z + 1))

# Création d'une liste par compréhension
# Pour chaque valeur i allant de 0 à n-1 (car range(n) génère [0, 1, ..., n-1]):
#   - On appelle la fonction f avec les arguments a, b, et i+1
#   - On appelle la fonction f avec les arguments c, d, et i+1
#   - On additionne les deux résultats pour obtenir une somme
# La liste complète contient toutes les sommes calculées pour chaque valeur de i
# On utilise la fonction min() pour obtenir la plus petite valeur parmi toutes celles calculées dans la liste
resultat_minimum = min([f(a, b, i + 1) + f(c, d, i + 1) for i in range(n)])

# Affiche la valeur minimale obtenue à l'utilisateur via la fonction print
print(resultat_minimum)