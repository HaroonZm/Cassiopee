# Demander à l'utilisateur de saisir un nombre entier, puis stocker cette valeur dans la variable 'n'
# 'input()' lit une ligne de texte au clavier, 'int()' convertit ce texte en entier
n = int(input())

# Demander à l'utilisateur de saisir une liste de nombres entiers séparés par des espaces
# 'input()' lit la ligne
# 'split()' divise la chaîne en une liste de sous-chaînes selon les espaces
# 'map(int, ...)' convertit chaque sous-chaîne en entier
# 'list(...)' convertit l'objet 'map' en liste Python
a = list(map(int, input().split()))

# Initialiser la variable qui contiendra le résultat final
# On utilise la valeur 0 comme point de départ car on va additionner ultérieurement à cette variable
result = 0

# Initialiser l'indice x, qui servira à parcourir le tableau 'a'
x = 0

# Initialiser une variable nommée 'i' à 0, qui sera utilisée comme un accumulateur pour former la somme courante des éléments de la sous-séquence
i = 0

# Démarrer une boucle for qui va de 0 jusqu'à n-1
# 'range(n)' crée un itérable de n valeurs commençant à 0 et finissant à n-1
# À chaque itération, 'j' vaudra l'indice actuel de la boucle
for j in range(n):
    # Boucle while permettant d'étendre la fenêtre vers la droite autant que possible
    # La condition 'x < n' garantit que l'indice x ne dépasse pas le dernier élément du tableau
    # 'i & a[x]' effectue un 'ET' binaire entre l'accumulateur courant 'i' et le prochain élément 'a[x]'
    # Si 'i & a[x] == 0', cela veut dire qu'aucun bit à 1 n'est commun entre 'i' et 'a[x]', donc ils peuvent être additionnés sans collision binaire
    while x < n and (i & a[x]) == 0:
        # Ajouter à 'i' la valeur de 'a[x]', ce qui agrandit la fenêtre courante
        i += a[x]
        # Incrémenter l'indice 'x' pour pointer vers le prochain élément de la liste pour l'itération suivante
        x += 1
    # Ajouter à 'result' le nombre de sous-séquences valides trouvées pour l'indice 'j'
    # 'x - j' est le nombre d'intervalles possibles commençant à l'indice 'j'
    result += x - j
    # Retirer de 'i' la valeur de 'a[j]' pour déplacer le début de la fenêtre vers la droite lors de l'itération suivante
    # Cela permet à la fenêtre glissante de ne plus considérer l'élément de début précédent
    i -= a[j]

# Afficher le résultat final, qui est le nombre total de sous-séquences satisfaisant la condition
print(result)