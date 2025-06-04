# Demande à l'utilisateur d'entrer un entier, puis convertit son entrée en un entier
N = int(input())  # N représente le nombre d'éléments que nous allons traiter

# Demande à l'utilisateur d'entrer un autre entier, convertit aussi son entrée
K = int(input())  # K est une valeur de référence à utiliser dans le calcul

# Crée une liste vide appelée 'mylist' qui n'est cependant pas utilisée dans le reste du code,
# mais elle est déclarée ici (on aurait pu ne pas la déclarer, ça ne change rien au résultat)
mylist = []

# Initialise une variable appelée 'count' à 0. Cela servira à accumuler le résultat final lors du traitement de la liste.
count = 0

# Demande à l'utilisateur d'entrer une ligne d'entiers, les sépare grâce à split(), puis utilise map() pour convertir chaque chaîne en entier
# Ensuite, transforme le résultat map en liste.
x = list(map(int, input().split()))  # Cette liste 'x' contiendra les valeurs à traiter, supposées être de longueur N

# Démarre une boucle for qui itère à travers chaque indice compris entre 0 (inclus) et N (exclus)
for i in range(N):
    # À chaque itération, on va décider comment traiter l'élément x[i] en fonction de sa relation avec K

    # On vérifie si (K - x[i]) est supérieur ou égal à x[i]
    # Cela revient à vérifier si l'écart entre K et x[i] est au moins égal à x[i] lui-même
    if K - x[i] >= x[i]:
        # Si la condition est vraie, on ajoute à 'count' la valeur de x[i] multipliée par 2
        count = count + x[i] * 2
        # Cela signifie qu'on considère deux fois x[i] dans le total
    else:
        # Si la condition est fausse, on ajoute à 'count' le double de la différence (K - x[i])
        # Cela représente l'autre direction potentielle du calcul
        count = count + (K - x[i]) * 2

# Après avoir traité tous les éléments de la liste, on affiche la valeur finale de 'count' à l'aide de la fonction print()
print(count)  # C'est le résultat, la somme selon la logique appliquée à chaque élément de x