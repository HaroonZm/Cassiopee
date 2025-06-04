# Demander à l'utilisateur de saisir un entier et convertir la saisie en un nombre entier (int)
# input() lit une chaîne depuis la console, int() convertit la chaîne en entier
x = int(input())

# Initialiser une variable 'n' avec la valeur 2
n = 2

# Utiliser une boucle for pour répéter des instructions 'x' fois
# range(x) produit une séquence de 'x' nombres, de 0 à x-1
for i in range(x):
    # À chaque itération de la boucle, mettre à jour 'n'
    # n = n + n + 1 + 1 signifie :
    #  - n + n double la valeur actuelle de 'n'
    #  - puis on ajoute 1, puis encore 1 (donc on ajoute 2 en tout)
    n = n + n + 1 + 1

# Afficher la valeur finale de 'n' après la boucle
# print() affiche l'argument passé à la console
print(n)