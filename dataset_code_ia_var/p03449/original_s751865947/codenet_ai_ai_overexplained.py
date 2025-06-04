# Lecture d'un entier à partir de l'entrée utilisateur et conversion en type int.
N = int(input())  # N représente le nombre d'éléments dans les listes A et B.

# Lecture d'une ligne de nombres séparés par des espaces depuis l'entrée utilisateur.
# input().split() retourne une liste de chaînes de caractères correspondant aux nombres tapés.
# map(int, ...) applique la fonction int à chaque élément de la liste pour les convertir en entiers.
# list(...) convertit l'itérateur retourné par map en une liste Python.
A = list(map(int, input().split()))  # La liste A contient N entiers lus de l'utilisateur.

# Même procédé pour lire la liste B de N entiers.
B = list(map(int, input().split()))  # La liste B contient N entiers lus de l'utilisateur.

# Initialisation d'une variable r à zéro.
# Cette variable va contenir la valeur maximale calculée dans la suite du programme.
r = 0

# Boucle for qui itère sur chaque valeur de i allant de 0 à N-1 inclus.
for i in range(N):
    # A chaque itération, on considère deux parties des listes :
    #   - A[:i+1] signifie : prendre les éléments de la liste A, depuis l'indice 0 jusqu'à l'indice i inclus.
    #     Par exemple, si i=2, A[:3] va de l'indice 0 à 2 (exclut l'indice 3).
    #   - B[i:] signifie : prendre les éléments de la liste B depuis l'indice i jusqu'à la fin de la liste.
    # sum(A[:i+1]) calcule la somme des (i+1) premiers éléments de A.
    # sum(B[i:]) calcule la somme des éléments de B du i-ème jusqu'au dernier.

    # On ajoute les deux sommes pour obtenir une valeur temporaire.
    # La fonction max(r, valeur_temporaire) retourne la plus grande des deux valeurs.
    # On utilise cette fonction pour que r garde toujours la plus grande valeur rencontrée jusqu'à présent.
    r = max(r, sum(A[:i+1]) + sum(B[i:]))

# Affichage final de la valeur maximale calculée.
print(r)  # Affiche la valeur calculée de r, qui est le résultat recherché.