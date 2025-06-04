# Demande à l'utilisateur de saisir trois entiers séparés par des espaces (comme "1 2 3")
# La fonction input() attend une chaîne de caractères saisie par l'utilisateur.
# split() découpe cette chaîne en morceaux séparés (tokens) en utilisant l'espace comme séparateur par défaut.
# map(int, ...) convertit chaque token (qui est une chaîne de caractères) en entier.
# Enfin, les trois entiers sont affectés aux variables a, b et c respectivement.
a, b, c = map(int, input().split())

# Demande à l'utilisateur de saisir un autre entier qui sera la valeur de k.
# Ce nombre sera utilisé ultérieurement pour déterminer combien de fois multiplier un nombre par 2.
k = int(input())

# Utilise la fonction max() pour déterminer le plus grand parmi les trois entiers a, b et c.
# Stocke cette valeur maximale dans la variable num.
num = max(a, b, c)

# Utilise une boucle for pour exécuter un bloc de code plusieurs fois.
# range(1, k + 1) génère une séquence de nombres entiers allant de 1 jusqu'à k inclus.
# Pour chaque valeur de i dans cette séquence, exécute le corps de la boucle.
for i in range(1, k + 1):
    # À chaque itération de la boucle, double la valeur de num en la multipliant par 2.
    # Cela équivaut à multiplier num par 2, puis par 2 encore, et ainsi de suite, k fois.
    num = num * 2

# Calcule la somme totale de a, b et c.
# Ensuite, soustrait à cette somme le maximum des trois (puisque num contient déjà ce maximum transformé).
# Ajoute à ce résultat la nouvelle valeur de num (qui était le maximum original, multiplié par 2 k fois).
# Affiche finalement le résultat à l'écran.
print(num + (a + b + c) - max(a, b, c))