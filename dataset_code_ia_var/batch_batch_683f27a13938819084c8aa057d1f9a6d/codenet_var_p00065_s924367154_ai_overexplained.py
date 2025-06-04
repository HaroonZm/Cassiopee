# Initialisation d'un dictionnaire vide nommé 'A' qui sera utilisé pour stocker des clés (x) et pour compter combien de fois chaque x apparaît
A = {}

# On entre dans une boucle infinie qui ne s'arrêtera que si elle est explicitement interrompue
while True:
    # Utilisation de la fonction input() pour lire une ligne entrée par l'utilisateur sur le clavier
    S = input()
    # Vérification si la ligne lue est une chaîne vide ''
    if S == '':
        # Si la chaîne est vide, on sort de la boucle avec 'break'
        break
    # La chaîne d'entrée S est supposée contenir deux entiers séparés par une virgule, par exemple "4,5"
    # La méthode split(',') sépare la chaîne S en une liste selon la virgule, 
    # puis map(int, ...) convertit chaque élément de la liste en entier grâce à la fonction int
    x, y = map(int, S.split(','))
    # Vérifie si la valeur x existe déjà comme une clé dans le dictionnaire A
    if x in A:
        # Si x existe, on incrémente la valeur correspondante dans le dictionnaire de 1
        A[x] += 1
    else:
        # Si x n'existe pas encore dans le dictionnaire, on crée une nouvelle clé x dans le dictionnaire avec la valeur associée 1
        A[x] = 1

# Création d'un deuxième dictionnaire vide nommé 'B', qui servira de compteur similaire mais pour une seconde série d'entrées
B = {}

# Démarrage d'une autre boucle infinie, qui cette fois-ci sera arrêtée de façon différente
while True:
    try:
        # Tentative de lire une ligne de texte à l'aide de input()
        # La ligne lue est supposée contenir deux nombres séparés par une virgule, par exemple "3,8"
        # On sépare la chaîne selon la virgule puis on convertit les deux morceaux en int
        x, y = map(int, input().split(','))
    except EOFError:
        # Si la fonction input() échoue parce que la fin de l'entrée (EOF) est atteinte, une exception EOFError est levée
        # Dans ce cas, on quitte la boucle en utilisant break
        break
    # Vérifie si la valeur x existe déjà comme clé dans le dictionnaire B
    if x in B:
        # Si x existe déjà comme clé, on augmente la valeur associée de 1 : cela compte le nombre d'occurrences de x
        B[x] += 1
    else:
        # Si x n'est pas encore présent dans le dictionnaire, on l'ajoute avec la valeur initiale 1
        B[x] = 1

# Parcours de toutes les clés (i) présentes dans le dictionnaire A
for i in A.keys():
    # Vérifie pour chaque clé i de A si elle existe aussi dans le dictionnaire B
    if i in B:
        # Si la clé i est également présente dans B, on affiche cette clé i,
        # suivie de la somme de la valeur de i dans A et dans B (addition des deux compteurs)
        print(i, A[i] + B[i])