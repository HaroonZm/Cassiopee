# Demande à l'utilisateur de saisir un entier (par exemple, la longueur d'une séquence)
# La fonction input() lit la saisie au clavier sous forme de chaîne de caractères
# La fonction int() convertit cette chaîne de caractères en un entier
# Cela affecte le nombre entier lu à la variable n
n = int(input())

# Initialise la variable de résultat à 1.
# Cette variable servira à stocker le résultat final du calcul qui sera modifié plus tard
res = 1

# Crée une liste vide nommée 'a'
# Une liste en Python est une structure de données ordonnée et modifiable
a = []

# Boucle for pour une séquence de longueur n (allant de 0 à n-1)
for i in range(n):
    # Pour chaque itération, lit un entier à partir de l'entrée standard
    # Ensuite, crée un tuple contenant cet entier et la valeur 1
    # Le tuple (valeur lue, 1) est ajouté à la liste 'a'
    a.append((int(input()), 1))

# Boucle for similaire pour une séquence de longueur n
for i in range(n):
    # Pour chaque itération, lit un entier à partir de l'entrée standard
    # Ensuite, crée un tuple contenant cet entier et la valeur -1
    # Ces tuples (valeur lue, -1) sont ajoutés à la liste 'a'
    a.append((int(input()), -1))

# Trie la liste 'a' sur place
# La liste consiste maintenant en 2n tuples où le premier élément est un entier et
# le deuxième élément est 1 ou -1
# La méthode sort() trie les tuples selon leur premier élément par défaut
a.sort()

# Initialise une nouvelle variable entière t à 0.
# Cette variable servira probablement à compter/suivre un solde ou une somme.
t = 0

# Parcourt chaque élément (each tuple) dans la liste triée 'a'
for i in a:
    # Pour chaque tuple i, vérifie une condition impliquant la valeur actuelle de t et i[1].
    # i[1] est le deuxième élément du tuple courant dans la liste (1 ou -1)
    # t est le compteur courant mis à jour à chaque étape
    # La condition utilise la fonction abs(), qui retourne la valeur absolue de son argument.
    # La condition teste si abs(i[1] + t) n'est pas égal à abs(i[1]) + abs(t).
    # Ceci vérifie si i[1] et t ont des signes opposés et se compensent en valeur absolue.
    if abs(i[1] + t) != abs(i[1]) + abs(t):
        # Si la condition est vraie, multiplie res par abs(t)
        # Utilise l'opérateur modulo (%) pour garder la valeur dans la limite de 1_000_000_007
        # Met à jour res avec cette nouvelle valeur
        res = (res * abs(t)) % 1000000007
    # Met à jour le compteur t en lui ajoutant i[1] (va augmenter ou diminuer selon i[1])
    t += i[1]

# Affiche le résultat final stocké dans la variable res
print(res)