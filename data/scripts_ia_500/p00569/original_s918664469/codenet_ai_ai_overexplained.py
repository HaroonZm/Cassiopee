N, K, L, *A = map(int, open(0).read().split())
# Ici, nous lisons l'entrée standard complète, puis nous utilisons map pour convertir chaque élément lu (sous forme de chaîne de caractères)
# en un entier. La fonction open(0) ouvre le flux d'entrée standard (stdin).
# Ensuite, nous utilisons un unpacking multiple:
# - N reçoit le premier entier, représentant typiquement la taille d'une liste ou d'un ensemble de données.
# - K reçoit le second entier, un paramètre du problème.
# - L reçoit le troisième entier, un autre paramètre du problème.
# - *A recueille tous les entiers restants dans une liste appelée A.
# Cela signifie que la première ligne de l'entrée est attendue sous la forme: N K L suivie de N entiers pour A.

def solve(X):
    # Définition d'une fonction solve qui prend un paramètre X (un entier).
    # Cette fonction teste une condition qui sera utilisée dans une recherche binaire.
    # Elle retourne un booléen indiquant si une certaine propriété est satisfaite pour la valeur X.

    s = -1
    # Variable s initialisée à -1; elle n'est jamais modifiée par la suite
    # Probablement un vestige de code ou préparée pour un usage ultérieur. Peut-être laissée sans utilité ici.

    su = 0
    # Variable su initialisée à 0; elle n'est pas utilisée par la suite dans la fonction.
    # Pourrait être un reste de code ancien ou préparé pour un calcul de somme.

    R = []
    # Liste R qui sera utilisée pour stocker les indices t des éléments dans A qui répondent à une certaine condition.
    # Dans ce cas, ceux dont la valeur A[t] est inférieure ou égale à X.

    res = 0
    # Variable res pour accumuler le résultat partiel sous forme d'entier.

    for t, a in enumerate(A):
        # Boucle for qui itère sur la liste A avec l'index t (commençant à 0) et la valeur a correspondant à A[t].
        # enumerate() est une fonction Python qui retourne chaque index et la valeur correspondante.

        if A[t] <= X:
            # Condition qui vérifie si l'élément courant A[t] est inférieur ou égal à X.
            # Si c'est le cas, cet indice sera ajouté à la liste R.

            R.append(t)
            # On ajoute l'indice t à la liste R.

        if len(R) >= K:
            # Si la longueur de la liste R est au moins égale à K, 
            # cela signifie qu'on a assez d'indices qui remplissent la condition A[t] <= X.
            # Alors on effectue une opération sur res.

            res += R[-K] + 1
            # On ajoute à res la valeur de l'élément à la position -K dans R, c'est-à-dire l'indice qui est le K-ième depuis la fin.
            # Puisque R stocke des indices t, R[-K] est un indice de A.
            # On ajoute 1 ici (probablement pour convertir de l'indexation 0-based à 1-based).
            # Cette opération est répétée pour chaque élément parcouru dans A,
            # accumulant ainsi un total dans res.

    return res >= L
    # La fonction retourne True si res est supérieur ou égal à L, sinon False.
    # Cette condition sera utilisée pour décider si la valeur X est suffisante dans la recherche binaire.

left = 0
# Variable left initialisée à 0, représentant la borne inférieure dans la recherche binaire.

right = N
# Variable right initialisée à N, représentant la borne supérieure dans la recherche binaire.
# N est probablement aussi la valeur maximale possible pour X, 
# ou la taille de la liste, utilisée comme borne.

while left + 1 < right:
    # Boucle while qui continue tant que la distance entre left et right est strictement supérieure à 1.
    # Ceci est une condition classique pour une recherche binaire afin d'éviter une boucle infinie.
    # L'idée est de réduire progressivement l'intervalle [left, right].

    mid = (left + right) >> 1
    # Calcul du milieu de l'intervalle [left, right].
    # L'opérateur >> 1 représente un décalage binaire à droite de 1 bit,
    # ce qui équivaut à une division entière par 2.
    # Donc mid est la valeur moyenne entière entre left et right.

    if solve(mid):
        # On teste si la fonction solve retourne True pour mid.
        # Cela signifie que mid satisfait la condition recherchée.

        right = mid
        # Si la condition est vraie, on peut réduire la borne supérieure à mid,
        # car on cherche généralement le plus petit X qui satisfait la condition.
    else:
        # Sinon, si solve(mid) retourne False,
        # cela signifie que mid est trop faible pour satisfaire la condition.

        left = mid
        # On augmente la borne inférieure à mid, car solution doit être plus grande.

print(right)
# Enfin, on affiche la valeur de right, 
# qui correspond à la plus petite valeur X pour laquelle solve(X) est True,
# c'est-à-dire la réponse au problème posé.