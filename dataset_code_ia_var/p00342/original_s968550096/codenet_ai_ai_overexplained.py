# Demander à l'utilisateur de saisir une valeur entière à partir du clavier pour représenter le nombre d'éléments dans la liste
n = int(input())  # Par exemple, si l'utilisateur saisit '5', alors n vaudra 5

# Demander à l'utilisateur de saisir une ligne composée de nombres séparés par des espaces
# Cette ligne est ensuite transformée en liste de chaînes de caractères grâce à la méthode split()
# Ensuite, chaque chaîne représentant un nombre est convertie en entier grâce à int()
# Enfin, la liste de tous ces int est stockée dans la variable 'a'
a = [int(num) for num in input().split()]

# Initialiser la variable 'ans' à la valeur flottante 0.0
# Cette variable servira à conserver la plus grande valeur calculée plus loin dans le programme
ans = 0.0

# Trier la liste 'a' dans l'ordre croissant afin que les plus petits éléments soient placés au début,
# et les plus grands à la fin ; cela est utile pour les calculs de maximum et minimum ultérieurs
a.sort()

# Démarrer une boucle for qui va itérer depuis 0 jusqu'à n-3 inclus (soit n-2 exclusions)
# Cela signifie que la variable d'itération 'i' prendra les valeurs 0, 1, ..., n-3
for i in range(n - 2):
    # À chaque itération, calculer (a[n - 1] + a[n - 2]) / (a[i + 1] - a[i] + 0.0)
    # a[n-1] correspond au plus grand élément de la liste (puisqu'elle est triée)
    # a[n-2] correspond au second plus grand élément de la liste
    # a[i] est l'élément à la position courante dans la boucle
    # a[i+1] est l'élément suivant dans la liste
    # Le '+ 0.0' force la division à se faire en virgule flottante, même si tous les arguments sont des entiers
    val = (a[n - 1] + a[n - 2]) / (a[i + 1] - a[i] + 0.0)
    # Comparer la valeur actuelle de 'ans' à 'val' et assigner à 'ans' la plus grande des deux valeurs grâce à max()
    ans = max(ans, val)

# Calculer une première valeur supplémentaire en dehors de la boucle
# (a[n - 1] + a[n - 4]) : somme du plus grand élément et du 4ème plus grand
# (a[n - 2] - a[n - 3] + 0.0) : différence entre le 2ème et le 3ème plus grand que l'on force en flottant
val1 = (a[n - 1] + a[n - 4]) / (a[n - 2] - a[n - 3] + 0.0)

# Mettre à jour 'ans' si cette nouvelle valeur est effectivement plus grande
ans = max(ans, val1)

# Calculer une seconde valeur supplémentaire, avec une combinaison différente des indices extrêmes
# (a[n - 3] + a[n - 4]) : somme du 3ème plus grand et du 4ème plus grand
# (a[n - 1] - a[n - 2] + 0.0) : différence entre le plus grand et le second plus grand (forcée en flottant)
val2 = (a[n - 3] + a[n - 4]) / (a[n - 1] - a[n - 2] + 0.0)

# On met à jour 'ans' si cette nouvelle valeur est la plus grande trouvée jusqu'ici
ans = max(ans, val2)

# Afficher le résultat avec 8 chiffres après la virgule, en utilisant le formatage de chaîne de caractères
# '%.8f' : cela signifie que l'on affiche le nombre sous forme flottante (f), avec 8 chiffres après la virgule
print('%.8f' % (ans))