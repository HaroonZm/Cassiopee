# Demander à l'utilisateur de rentrer un nombre entier qui sera affecté à la variable N
# Cette ligne lira une ligne de l'entrée standard (par exemple, le clavier), 
# la convertira en entier avec int(), puis stockera la valeur obtenue dans N.
N = int(input())

# Demander à l'utilisateur de rentrer une séquence d'entiers séparés par des espaces (par exemple : "1 2 3")
# input() lit une ligne de texte, .split() découpe la chaîne de caractères sur les espaces pour créer une liste de chaînes
# map(int, ...) applique la fonction int() à chaque élément de cette liste pour les convertir tous en entiers
# list(...) convertit le résultat du map en une liste, stockée dans la variable h
h = list(map(int, input().split()))

# Initialiser une variable de compteur appelée ans à 0
# Cette variable comptera le nombre total d'opérations effectuées
ans = 0

# Créer une boucle infinie avec 'while True', ce qui signifie que la boucle continuera pour toujours,
# à moins qu'elle ne soit interrompue par une instruction 'break'
while True:
    # Utiliser la fonction max() pour trouver la valeur maximale actuelle dans la liste h
    # Si la valeur maximale est 0, cela signifie que tous les éléments de h sont maintenant à 0
    # Dans ce cas, on sort de la boucle avec 'break'
    if max(h) == 0:
        break

    # Initialiser la variable d'index i à 0
    # On utilisera i pour parcourir les indices de la liste h, du début à la fin
    i = 0

    # Démarrer une boucle interne qui continue tant que i est strictement inférieur à N
    # N représente la longueur de h
    while i < N:
        # Si l'élément actuel h[i] est égal à 0,
        # cela signifie qu'on ne peut pas effectuer d'opération dessus (car il est déjà à 0)
        # Donc on incrémente simplement i pour passer à l'élément suivant
        if h[i] == 0:
            i += 1   # On augmente i de 1 pour passer à l'indice suivant de la liste
            continue # 'continue' indique de sauter le reste du bloc courant et de recommencer la boucle avec le nouvel i
        else:
            # Si l'élément courant h[i] est supérieur à 0, 
            # cela marque le début d'une séquence de "hauteurs" positives
            # On augmente le compteur d'opérations ans de 1,
            # car on va effectuer une opération sur cette séquence de valeurs positives consécutives
            ans += 1

            # Maintenant, démarrer une seconde boucle interne imbriquée qui va décrémenter de 1 tous les h[i]
            # pour tous les i consécutifs tels que h[i] > 0, à partir de l'indice courant i
            while (i < N and h[i] > 0):
                # On décrémente la hauteur courante h[i] de 1
                h[i] -= 1
                # Puis on passe à l'indice suivant
                i += 1

# Après la fin de la boucle principale (qui se termine lorsque tous les éléments de h sont à 0), 
# afficher la valeur finale de ans, qui représente le nombre total d'opérations effectuées
print(ans)