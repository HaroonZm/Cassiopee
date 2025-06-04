# Demander à l'utilisateur d'entrer deux entiers sur la même ligne séparés par un espace
# map(int, input().split()) convertit chaque valeur saisie (séparée par un espace) en entier
# n et m reçoivent respectivement la première et la deuxième valeur saisie
n, m = map(int, input().split())

# Demander à l'utilisateur d'entrer une liste de nombres séparés par des espaces
# map(int, input().split()) convertit chaque valeur saisie en entier
# list(...) transforme l'itérable produit par map en une vraie liste Python
x = list(map(int, input().split()))

# Trier la liste x dans l'ordre croissant
# Cela modifie la liste x elle-même
x.sort()

# Initialise une liste vide ans qui contiendra les différences entre éléments consécutifs
ans = []

# Boucle for pour itérer i de 0 jusqu'à m-2 inclus (car range(m-1) exclut m-1)
for i in range(m - 1):
    # Calculer la différence entre l'élément suivant et l'élément courant dans la liste triée x
    # Cela représente la distance entre chaque paire d'éléments consécutifs
    diff = x[i + 1] - x[i]
    # Ajouter la différence à la liste ans
    ans.append(diff)

# Trier la liste des différences ans par ordre croissant
ans.sort()

# Vérifier si le nombre n est strictement inférieur à m
if n < m:
    # Si n est inférieur à m, on doit effectuer certains calculs :
    # Prendre la somme des (m-n) plus petites différences dans la liste ans
    # ans[:m-n] prend une "slice" de ans allant du début jusqu'à l'indice (m-n) exclu,
    # c'est-à-dire les (m-n) premiers éléments de la liste triée ans
    # sum(...) calcule la somme totale de ces éléments
    result = sum(ans[:m-n])
    # Afficher le résultat à l'utilisateur
    print(result)
else:
    # Si n n'est pas inférieur à m (c'est-à-dire n >= m),
    # alors le résultat doit toujours être 0
    print(0)