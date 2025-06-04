# Demander à l'utilisateur d'entrer un entier, stocké dans la variable n.
# input() lit une ligne de l'entrée standard (typiquement le clavier).
# int(...) convertit la chaîne de caractères reçue en un entier.
n = int(input())

# Demander à l'utilisateur d'entrer une séquence d'entiers sur une ligne.
# input() lit la ligne sous forme de chaîne de caractères.
# .split() divise la chaîne en différents éléments, séparés par des espaces par défaut, et crée une liste de chaînes (une par nombre).
# map(int, ...) applique la fonction int à chaque élément de la liste résultante, convertissant chaque chaîne de caractères en entier.
# list(...) convertit l'objet map en une véritable liste Python d'entiers, qui est stockée dans la variable alst.
alst = list(map(int, input().split()))

# Créer une liste de trois éléments, initialisés à zéro : [0, 0, 0].
# Cette liste contiendra le compte des entiers selon leur reste modulo 3.
# mod_cnt[0] comptera combien de nombres dans alst donnent un reste de 0 lorsqu'ils sont divisés par 3.
# mod_cnt[1] comptera ceux donnant un reste de 1.
# mod_cnt[2] comptera ceux donnant un reste de 2.
mod_cnt = [0, 0, 0]

# Boucler à travers chaque entier 'a' de la liste alst.
for a in alst:
    # Calculer le reste de la division entière de 'a' par 3 (c'est l'opérateur modulo '%').
    # Ce reste sera soit 0, 1, ou 2.
    # En utilisant le résultat comme indice de la liste mod_cnt, on incrémente le bon compteur.
    # Exemple : si a % 3 == 1, alors mod_cnt[1] est augmenté de 1.
    mod_cnt[a % 3] += 1

# À ce stade, mod_cnt[0] est le nombre d'entiers divisibles par 3,
# mod_cnt[1] est le nombre avec un reste de 1,
# et mod_cnt[2] est le nombre avec un reste de 2.

# La suite établit une série de conditions pour déterminer quel nombre afficher selon la configuration des comptes.
# Première condition :
# Si mod_cnt[1] == 0 et mod_cnt[2] == 0, cela signifie que tous les nombres dans alst sont divisibles par 3 (aucun nombre ne laisse de reste 1 ou 2).
if mod_cnt[1] == 0 and mod_cnt[2] == 0:
    # Dans ce cas précis, on affiche 1 (c’est la sortie demandée pour cette configuration particulière).
    print(1)

# Deuxième condition :
# Si mod_cnt[1] == mod_cnt[2], cela signifie que le nombre d'entiers laissant un reste 1 est égal au nombre laissant un reste 2.
elif mod_cnt[1] == mod_cnt[2]:
    # Dans ce cas, on affiche la somme totale de tous les éléments (tous les restes), soit le nombre d'entiers initialement reçus.
    print(mod_cnt[0] + mod_cnt[1] + mod_cnt[2])

# Troisième condition :
# Si le nombre de restes 1 est strictement inférieur au nombre de restes 2.
elif mod_cnt[1] < mod_cnt[2]:
    # On additionne le nombre d'éléments divisibles par 3 (mod_cnt[0]), puis mod_cnt[1] (tous les restes 1),
    # puis on ajoute le minimum entre (mod_cnt[1]+3) et mod_cnt[2].
    # min(mod_cnt[1]+3, mod_cnt[2]) s'assure que l'on ne prend pas plus de restes 2 que disponible,
    # ou éventuellement trois de plus que le nombre de restes 1.
    print(mod_cnt[0] + mod_cnt[1] + min(mod_cnt[1] + 3, mod_cnt[2]))

# Dernière condition :
# Si le nombre de restes 1 est strictement supérieur au nombre de restes 2.
elif mod_cnt[1] > mod_cnt[2]:
    # Ici, on additionne mod_cnt[0] (divisibles par 3),
    # puis min(mod_cnt[1], mod_cnt[2]+3) (le nombre minimum entre les restes 1 disponibles et les restes 2 plus trois),
    # puis mod_cnt[2] (tous les restes 2).
    print(mod_cnt[0] + min(mod_cnt[1], mod_cnt[2] + 3) + mod_cnt[2])

# Remarques :
# - L'ensemble du script réalise des opérations basées sur le comptage des restes modulo 3 d'une séquence d'entiers.
# - Les conditions finales permettent de choisir la sortie en fonction des différentes répartitions de ces restes.
# - Les commentaires ici expliquent chaque construction Python de base, y compris les opérations fondamentales comme print,
#   les boucles for, les listes, les conversions de types et les conditions.