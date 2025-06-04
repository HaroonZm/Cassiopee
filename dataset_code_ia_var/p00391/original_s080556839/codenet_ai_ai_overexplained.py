# Demande à l'utilisateur d'entrer deux entiers séparés par un espace qui seront stockés dans les variables W et H
# La fonction input() lit la ligne d'entrée standard sous forme de chaîne de caractères
# La méthode split() découpe la chaîne en une liste de sous-chaînes (par défaut séparées par des espaces)
# La fonction map(int, ...) convertit chaque sous-chaîne en entier
# Les deux valeurs sont affectées simultanément grâce à l'affectation multiple (décomposition)
W, H = map(int, input().split())

# Lis une ligne d'entrée utilisateur, la découpe en une liste de sous-chaînes, puis convertit chaque sous-chaîne en entier
# Le * avant A permet de stocker la liste résultante dans la variable A (opérateur d'étoile pour dépaqueter une séquence dans une liste)
# Par exemple, si l'entrée utilisateur est "3 2 1", A prendra la valeur [3, 2, 1]
*A, = map(int, input().split())

# Même opération pour B: lecture, découpage et conversion afin d'obtenir une liste d'entiers B
*B, = map(int, input().split())

# Trie la liste A en place, c'est-à-dire que l'ordre des éléments est modifié dans la variable sans créer de nouvelle liste
# reverse=1 (équivalent de reverse=True) indique de trier dans l'ordre décroissant (du plus grand au plus petit)
A.sort(reverse=1)

# Calcule la somme des éléments de la liste A et de la liste B, puis teste l'égalité entre les deux sommes
# Si elles sont égales, l'expression sum(A)==sum(B) renverra True (équivalent à 1 en Python), sinon False (équivalent à 0)
# L'opérateur =+ est probablement une faute de frappe pour +=, mais ici il est utilisé pour initialiser 'ok' à (sum(A)==sum(B))
# Cela associe à 'ok' la valeur 1 si les sommes sont égales, sinon 0
ok =+ (sum(A) == sum(B))

# Boucle extérieure sur chaque élément 'a' de la liste A
for a in A:
    # Trie la liste B à chaque itération par ordre décroissant afin que les plus grands éléments soient traités en premier
    B.sort(reverse=1)
    # Boucle intérieure allant de 0 à a-1 (exclusif: range(a)), c'est-à-dire a fois
    for i in range(a):
        # Si i dépasse ou atteint la longueur de B, cela signifie que nous essayons d'accéder à un élément inexistant
        # ou si B[i] vaut 0, alors la tâche n'est plus réalisable selon les contraintes, donc on met ok à 0
        if i >= len(B) or B[i] == 0:
            ok = 0
            # On quitte la boucle interne immédiatement car il n'est plus possible de continuer
            break
        # Sinon, on décrémente la valeur de la case B[i] de 1 pour signifier qu'une unité a été affectée/consommée
        B[i] -= 1

# Affiche la valeur de la variable ok ; 1 signifie succès de la condition voulue, 0 échec
print(ok)