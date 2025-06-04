# Demander à l'utilisateur de saisir un entier, qui sera converti à partir d'une chaîne de caractères grâce à la fonction int(), et assigner le résultat à la variable N.
N = int(input())

# Lire une ligne d'entrée depuis l'utilisateur, qui sera lue sous forme de chaîne de caractères, puis utiliser la méthode split() pour séparer la chaîne en liste de sous-chaînes sur chaque espace trouvé, et assigner cette liste à la variable Ss.
Ss = input().split()

# Initialiser la variable res à la valeur 1. Cette variable servira à stocker le résultat final qui sera calculé plus bas dans le programme.
res = 1

# Commencer une boucle for qui itérera sur les entiers t allant de 1 à N inclus (car la fonction range(a, b) génère les entiers de a à b-1, donc il faut écrire N+1 pour aller jusqu'à N)
for t in range(1, N+1):
    # Vérifier si N n'est pas divisible par t sans reste en utilisant l'opérateur modulo %. Si N % t n'est pas égal à 0, cela signifie que t n'est pas un diviseur de N.
    if (N % t != 0):
        # Si t n'est pas un diviseur de N, il est inutile de considérer cette valeur de t, donc on continue à la prochaine itération de la boucle avec l'instruction continue.
        continue

    # Initialiser la variable f (qui servira de "drapeau" ou flag) à la valeur False. Cette variable deviendra True si on détecte une différence entre des éléments correspondant à l'intervalle considéré plus bas.
    f = False

    # Démarrer une boucle interne qui va parcourir les indices i de 0 à N-t-1 inclus, c'est-à-dire de 0 jusqu'à N-t (car range(s, e) ne prend pas e lui-même).
    for i in range(N - t):
        # Comparer les éléments de la liste Ss situés aux indices i et i+t. Si les deux éléments sont égaux, c'est-à-dire Ss[i] == Ss[i + t], alors on continue avec la prochaine valeur de i.
        if (Ss[i] == Ss[i + t]):
            continue
        # Si les deux éléments comparés sont différents, alors on définit le drapeau f à True pour signaler que la condition d'égalité n'est pas respectée, puis on sort immédiatement de la boucle for interne avec break.
        f = True
        break

    # Après avoir parcouru la boucle interne, vérifier si le drapeau f a été activé, c'est-à-dire f == True, indiquant qu'il y avait au moins une incompatibilité trouvée pour cet intervalle t.
    if (f):
        # Si la différence a été trouvée, on ne modifie pas le résultat et on saute à la prochaine itération de t dans la boucle for externe.
        continue

    # Si le drapeau n'a pas été activé, cela signifie que pour tous les i, Ss[i] == Ss[i + t], ce qui correspond à la validation de la période d'intervalle t pour la liste Ss.
    # Dans ce cas, on calcule le résultat comme N divisé par t (division entière) et assigne ce résultat à la variable res.
    res = N // t

    # Comme on a trouvé le plus grand res possible avec cette condition, on peut arrêter la boucle principale immédiatement avec break.
    break

# Afficher la valeur finale calculée de res, en utilisant la fonction print() pour écrire sur la sortie standard.
print(res)