# Importation du module 'copy' qui permet de faire des copies superficielles ou profondes d'objets
import copy

# Lecture d'une valeur entière depuis l'entrée standard (au clavier)
# Cette valeur correspond au nombre total d'éléments qui seront saisis ensuite
n = int(input())

# Lecture d'une ligne de nombres séparés par des espaces, conversion de chaque fragment en entier,
# puis construction d'une liste contenant tous ces entiers
data = list(map(int, input().split()))

# Tri de la liste 'data' dans l'ordre croissant
data.sort()

# Création d'une copie superficielle de la liste 'data' afin de travailler dessus
# sans altérer la liste d'origine - cela permet de manipuler la nouvelle liste indépendamment
data1 = copy.copy(data)

# Suppression et récupération du dernier élément de 'data1' (le plus grand, car la liste est triée)
A = data1.pop()
# Suppression et récupération du nouvellement dernier élément de 'data1' (le deuxième plus grand)
B = data1.pop()
# Détermination de la nouvelle taille de la liste restante après les deux suppressions
n_1 = n - 2

# Initialisation d'une variable 'min' à une très grande valeur,
# qui servira à stocker la plus petite différence trouvée entre deux éléments consécutifs
min = 100000000

# Parcours de la liste 'data1' (qui contient maintenant n-2 éléments) pour trouver
# la paire de nombres consécutifs ayant la différence la plus petite
for i in range(n_1 - 1):
    # Vérification de la différence entre l'élément à l'indice i+1 et celui à l'indice i
    if data1[i+1] - data1[i] < min:
        # Si la différence courante est inférieure à 'min', mise à jour de 'min'
        min = data1[i+1] - data1[i]
        # Stockage des deux valeurs consécutives correspondantes dans C et D
        C = data1[i+1]
        D = data1[i]

# Calcul du résultat intermédiaire 'ans_1' en réalisant une opération arithmétique
# : somme de A et B (les deux plus grands) divisée par la différence entre C et D (la plus petite des différences)
ans_1 = (A + B) / (C - D)

# Création d'une nouvelle copie superficielle de la liste d'origine 'data'
data2 = copy.copy(data)

# Réinitialisation de 'min' à une très grande valeur pour la nouvelle recherche
min = 100000000

# Recherche à nouveau, mais cette fois sur tous les éléments de la liste,
# la paire de valeur consécutive ayant la différence la plus faible
for i in range(n - 1):
    if data2[i+1] - data2[i] < min:
        min = data2[i+1] - data2[i]
        C = data2[i+1]
        D = data2[i]

# Suppression du premier élément de la paire trouvée (C)
data2.remove(C)
# Suppression du deuxième élément de la paire (D)
data2.remove(D)
# Suppression et récupération des deux derniers éléments restants de la liste (qui seront les plus grands après suppressions)
A = data2.pop()
B = data2.pop()

# Calcul d'un second résultat selon la même formule que précédemment, mais avec cette disposition différente des valeurs
ans_2 = (A + B) / (C - D)

# Affichage du plus grand des deux résultats calculés, en utilisant la fonction max
print(max(ans_1, ans_2))