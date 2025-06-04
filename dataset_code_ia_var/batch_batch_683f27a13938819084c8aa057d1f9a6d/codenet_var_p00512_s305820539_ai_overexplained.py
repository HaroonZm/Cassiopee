# Création d'un dictionnaire vide nommé 'o'
# Ce dictionnaire servira à stocker, pour chaque clé 'p', une valeur entière qui sera la somme de plusieurs valeurs associées à cette clé
o = {}

# Demande à l'utilisateur d'entrer un nombre entier via la fonction input()
# Ce nombre représente le nombre total de lignes de données que nous allons traiter dans la boucle
# La fonction int() convertit la chaîne de caractères retournée par input() en un entier utilisable pour range()
for _ in range(int(input())):
    # Pour chaque itération de la boucle :
    # input() demande une ligne à l'utilisateur, que l'on suppose de la forme "p m", séparées par un espace
    # .split() sépare cette ligne en deux chaînes distinctes sur l'espace : la première devient 'p', la seconde devient 'm'
    p, m = input().split()
    # Pour la clé 'p' dans le dictionnaire 'o', on récupère la valeur courante associée à 'p' avec o.get(p,0)
    # o.get(p,0) signifie : si 'p' existe déjà dans le dictionnaire, récupère sa valeur ; sinon, utilise 0 comme valeur par défaut
    # On ajoute à cette valeur la valeur entière obtenue en convertissant la chaîne 'm' en entier avec int(m)
    # Ensuite, on assigne la somme à la clé 'p' dans le dictionnaire 'o' (soit on met à jour, soit on crée une nouvelle entrée)
    o[p] = o.get(p, 0) + int(m)

# Création d'une liste 'k' à partir des clés du dictionnaire 'o'
# Pour chaque clé 'x' dans o.keys(), on crée un tuple composé de (longueur_de_x, x)
# len(x) calcule le nombre de caractères de la clé 'x'
# On utilise une compréhension de liste pour générer cette liste de tuples
k = sorted([(len(x), x) for x in o.keys()])

# On trie ensuite la liste 'k' avec la fonction sorted()
# 'sorted' utilise le premier élément du tuple (la longueur) comme critère principal de tri,
# donc les clés seront triées d'abord par leur longueur croissante, puis par ordre alphabétique en cas d'égalité de longueur

# On parcourt la liste triée des tuples (longueur, clé)
for _, i in k:
    # Pour chaque tuple, on ignore la longueur (nommée par un simple '_') et on utilise 'i' qui contient la clé
    # print() affiche la clé 'i', suivie d'un espace, puis la valeur correspondant à cette clé dans le dictionnaire 'o'
    print(i, o[i])