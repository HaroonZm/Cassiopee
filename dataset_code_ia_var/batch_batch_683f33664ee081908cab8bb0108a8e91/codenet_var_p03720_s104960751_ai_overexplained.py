# Demande à l'utilisateur de saisir deux entiers sur la même ligne, séparés par un espace.
# Ces entiers sont stockés dans N (nombre de noeuds) et M (nombre de paires, ou d'arêtes).
N, M = map(int, input().split())

# Crée une liste vide nommée A.
# Cette liste va contenir tous les entiers 'a' et 'b' issus des paires qui seront saisies ensuite.
A = []

# Commence une boucle qui va répéter l'opération M fois,
# car il y a M paires à lire.
for i in range(M):
    # Demande à l'utilisateur de saisir deux entiers sur une ligne séparés par un espace.
    # map(int, ...) convertit les deux éléments lus (sous forme de chaînes) en entiers.
    a, b = map(int, input().split())

    # Ajoute l'entier 'a' à la liste A.
    A.append(a)  # Cela ajoute la valeur de 'a' à la fin de la liste.

    # Ajoute l'entier 'b' à la liste A.
    A.append(b)  # Cela ajoute la valeur de 'b' à la fin de la liste.

# Démarre une boucle pour traiter chaque entier de 1 à N inclus.
# range(1, N+1) génère une séquence contenant les entiers de 1 à N.
for i in range(1, N + 1):
    # La méthode count() d'une liste retourne le nombre de fois
    # que la valeur 'i' apparaît dans la liste A.
    # En d'autres termes, cela compte combien de paires contiennent le noeud 'i'.
    print(A.count(i))  # Affiche le résultat sur une nouvelle ligne pour chaque noeud.