# Lire une ligne de l'entrée standard (habituellement le clavier), qui contient trois nombres séparés par des espaces
# La fonction input() lit la ligne sous forme de chaîne de caractères (string)
# La méthode split(), sans argument, coupe la chaîne en morceaux (tokens) là où il y a des espaces
# map(int, ...) applique l'objet int (fonction de conversion en entier) à chaque élément de la liste générée par split()
# Les trois valeurs converties sont ensuite affectées, dans l'ordre, aux variables h, a et b
h, a, b = map(int, input().split())

# Initialiser une variable nommée ans, qui servira à compter le nombre de cas satisfaisant la condition ci-dessous
# On commence donc avec la valeur 0 (zéro)
ans = 0

# Boucle for pour parcourir tous les entiers de a à b inclusivement
# range(a, b+1) génère une séquence de nombres entiers, partant de a et allant jusqu'à b (b inclus, car range s'arrête normalement avant la borne supérieure)
# La variable i prendra successivement chaque valeur de cette séquence
for i in range(a, b+1):
    # Pour chaque valeur de i, on vérifie si h est un multiple de i
    # L'opération % (modulo) donne le reste de la division entière de h par i
    # Si le reste est 0, cela signifie que h est exactement divisible par i, donc que i divise h sans reste
    if h % i == 0:
        # Si la condition ci-dessus est vraie, on ajoute 1 à la variable ans pour indiquer qu'un cas supplémentaire a été trouvé
        ans += 1

# Afficher (imprimer) la valeur finale de ans
# print() affiche à l'écran la valeur de ans, ce qui correspond au nombre total de diviseurs de h compris dans l'intervalle [a, b]
print(ans)