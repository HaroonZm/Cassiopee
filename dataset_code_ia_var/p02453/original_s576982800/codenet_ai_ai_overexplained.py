import bisect  # Importe le module bisect, qui fournit des fonctions pour travailler avec des listes triées de manière efficace.

# Demande à l'utilisateur d'entrer un nombre entier, qui sera converti explicitement depuis une chaîne de caractères en un entier avec la fonction int().
# 'n' représentera le nombre d'éléments dans la liste saisie par l'utilisateur.
n = int(input())

# Demande à l'utilisateur d'entrer une ligne de nombres séparés par des espaces.
# input() lit cette ligne comme une chaîne de caractères.
# .split() coupe la chaîne de caractères partout où il y a un espace, produisant une liste de chaînes.
# map(int, ...) applique la fonction int() à chaque chaîne (pour convertir chaque élément en entier).
# list(...) transforme le tout en une liste d'entiers.
num = list(map(int, input().split()))

# Demande à l'utilisateur combien de requêtes il souhaite effectuer, convertit la chaîne en entier, et stocke ce nombre dans la variable 'q'.
q = int(input())

# Démarre une boucle for.
# range(q) crée un itérable qui commence à 0 et s'arrête à q-1, fournissant exactement q itérations.
# On utilise '_' comme variable temporaire car la valeur n'est pas utilisée à l'intérieur de la boucle.
for _ in range(q):

    # Pour chaque itération, on lit un entier. C'est la valeur recherchée (ou la clé) dans la liste num.
    k = int(input())

    # On vérifie si la valeur recherchée 'k' est strictement supérieure au dernier élément de num.
    # num[-1] donne le dernier élément de la liste grâce à l'indexation négative.
    if k > num[-1]:
        # Si k est supérieur à tous les éléments de la liste :
        # Cela signifie qu'il n'est inférieur ou égal à aucun élément.
        # On imprime donc la valeur de n (la longueur de la liste), car c'est l'indice où il pourrait être inséré pour maintenir l'ordre.
        print(n)
        # La boucle passe directement à la prochaine itération sans exécuter le reste du bloc (mot clé 'continue').
        continue
    else:
        # Si la valeur recherchée 'k' est inférieure ou égale au dernier élément de la liste :
        # On utilise bisect_left pour trouver l'indice le plus bas où 'k' pourrait être inséré tout en maintenant l'ordre trié.
        # Si 'k' existe déjà dans la liste, bisect_left renverra l'indice de la première occurrence de 'k'.
        print(bisect.bisect_left(num, k))  # Affiche l'indice trouvé par bisect_left.