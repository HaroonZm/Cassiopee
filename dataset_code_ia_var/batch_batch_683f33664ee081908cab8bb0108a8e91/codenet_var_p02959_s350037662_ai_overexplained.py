# Demande à l'utilisateur d'entrer une valeur entière qui sera assignée à la variable N.
# input() lit un texte sur la ligne de commande, et int() convertit ce texte en entier.
N = int(input())

# Lit une ligne de texte, la découpe en morceaux à chaque espace,
# puis convertit chaque morceau en entier avec map(int, ...), avant de les placer dans une liste.
A = list(map(int, input().split()))

# Fait la même chose pour une autre liste, appelée B.
B = list(map(int, input().split()))

# Crée une variable appelée 'sum' pour stocker l'accumulateur de la somme totale, initialisée à 0.
sum = 0

# Lance une boucle qui va de 0 (inclus) à N (exclu), donc il y aura N itérations correspondant aux indices des listes A et B.
for i in range(N):
    # Calcule la différence entre l'élément A[i] et B[i] et assigne le résultat à la variable x.
    x = A[i] - B[i]
    # Vérifie si x est supérieur ou égal à 0, c'est-à-dire si A[i] est plus grand ou égal à B[i].
    if x >= 0:
        # Si la condition ci-dessus est vraie : ajoute à sum la valeur B[i] (on ajoute B[i] au résultat total).
        sum = sum + B[i]
    else:
        # Sinon, c'est que B[i] est plus grand que A[i] :
        # Ajouter d'abord toute la valeur de A[i] à sum (puisqu'on ne peut donner que tout ce qu'on a dans A[i]).
        sum = sum + A[i]
        # Soustraire A[i] à B[i] (B[i] devient le besoin restant après avoir utilisé tout A[i]).
        B[i] = B[i] - A[i]
        # On va maintenant regarder le prochain élément de la liste A : A[i+1],
        # En recalculant x comme la différence entre A[i+1] et la nouvelle valeur de B[i].
        x = A[i+1] - B[i]
        # De nouveau, on vérifie si la nouvelle valeur de x est supérieure ou égale à 0.
        if x >= 0:
            # Si oui, cela signifie que A[i+1] contient suffisamment pour couvrir B[i]
            # Donc on ajoute B[i] à sum (on utilise juste ce dont on a besoin dans A[i+1]).
            sum = sum + B[i]
            # On met alors à jour A[i+1] en retirant la valeur de B[i] (on diminue le stock correspondant).
            A[i+1] = A[i+1] - B[i]
        else:
            # Si x<0, cela veut dire qu'A[i+1] ne suffit pas pour combler B[i].
            # On ajoute donc tout ce qu'il reste dans A[i+1] à sum.
            sum = sum + A[i+1]
            # On met A[i+1] à zéro, car tout a été utilisé.
            A[i+1] = 0

# À la fin de la boucle, on affiche la valeur totale stockée dans sum à l'aide de print().
print(sum)