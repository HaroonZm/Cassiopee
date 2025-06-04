# Création d'une liste vide nommée 'ps' qui va servir à stocker des paires de valeurs (tuples)
ps = []

# On lit une ligne à partir de l'entrée standard (typiquement le clavier),
# on convertit cette chaîne de caractères en entier, et on assigne la valeur à la variable 'n'.
# Cela va représenter le nombre d'éléments (ou de paires) à lire ensuite.
n = int(input())

# Boucle for classique pour parcourir une séquence d'entiers allant de 0 à n-1 inclus.
# Ici, 'range(n)' génère une séquence de n entiers consécutifs, de 0 à n-1.
for i in range(n):
    # Pour chaque itération, on lit une nouvelle ligne entrée par l'utilisateur.
    # La méthode split() décompose la chaîne de caractères sur les espaces, renvoyant une liste de chaînes.
    # Ensuite, map(int, ...) applique la fonction int à chaque élément de la liste, pour transformer chaque chaîne en entier.
    # Après cela, on assigne respectivement les deux entiers lus aux variables 'x' et 'y'.
    x, y = map(int, input().split())
    # On crée un tuple contenant les deux entiers (x, y).
    # Un tuple est un type de structure de donnée immuable dans Python, c'est-à-dire qu'il ne peut pas être modifié après création.
    # On utilise les parenthèses pour créer un tuple avec deux éléments.
    # Ensuite, on utilise la méthode append pour ajouter ce tuple (x, y) à la liste 'ps'.
    ps.append((x, y))

# On utilise la méthode sort() de la liste 'ps' pour trier les éléments de la liste.
# Comme 'ps' est une liste de tuples, la méthode sort() va trier principalement par le premier élément de chaque tuple (par défaut),
# et en cas d'égalité du premier, tri secondaire sur le deuxième élément (et ainsi de suite si plus d'éléments).
# La méthode sort() trie la liste sur place, c'est-à-dire qu'elle modifie la liste existante 'ps' au lieu de retourner une nouvelle liste triée.
ps.sort()

# On utilise une boucle for pour parcourir tous les éléments de la liste triée 'ps'.
# À chaque itération, la variable 'i' reçoit une valeur consécutive de la liste 'ps', c'est-à-dire un tuple contenant deux entiers.
for i in ps:
    # On appelle la fonction print pour afficher la valeur de chaque tuple.
    # L'opérateur '*' (étoile) utilisé ici s'appelle "unpacking d'arguments" (dépaquetage).
    # Il permet de passer les deux valeurs du tuple en tant qu'arguments séparés à la fonction print,
    # de sorte qu'elles soient affichées avec un espace entre elles.
    # Par exemple, si i = (3, 5), 'print(*i)' est équivalent à 'print(3, 5)'.
    print(*i)