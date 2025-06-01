# Demander à l'utilisateur d'entrer deux nombres entiers séparés par un espace, puis les stocker dans les variables x et y
# input() récupère une chaîne de caractères entrée par l'utilisateur
# split() découpe cette chaîne en une liste de sous-chaînes selon les espaces
# La compréhension de liste [int(i) for i in input().split()] transforme chaque sous-chaîne en entier
x, y = [int(i) for i in input().split()]

# Définir une constante fiboMax qui sera la taille maximale de la liste pour stocker les nombres de Fibonacci
fiboMax = 100

# Créer une liste fibo de longueur fiboMax initialisée à 0
# Cette liste contiendra les nombres de Fibonacci
# La syntaxe [0 for i in range(fiboMax)] crée une liste comprenant fiboMax éléments, chacun étant 0
fibo = [0 for i in range(fiboMax)]

# Initialiser les deux premiers nombres de Fibonacci pour correspondre à la séquence classique
# fibo[1] et fibo[2] sont les 1ers et 2èmes termes (en ignorant l'indice 0)
fibo[1] = 1
fibo[2] = 1

# Remplir ensuite la liste fibo avec les autres nombres de Fibonacci jusqu'à fiboMax - 1
# La boucle commence à 3 car les deux premiers termes sont déjà définis
# La formule est fibo[i] = fibo[i-1] + fibo[i-2]
for i in range(3, fiboMax):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

# Initialiser les variables définissant les limites d'un rectangle dans le plan cartésien
# xMax et yMax représentent les coordonnées supérieures droite
# xMin et yMin représentent les coordonnées inférieures gauche
# Tous commencent à 0
xMax = 0
yMax = 0
xMin = 0
yMin = 0

# Initialiser la variable ans à -1, indiquant qu'il n'y a pas encore de réponse trouvée
ans = -1

# Vérifier si le point (x, y) est dans le rectangle défini par (xMin, yMin) et (xMax, yMax)
# Si oui, on peut fixer la réponse ans à 1
# Les conditions x <= xMax et y <= yMax vérifient que le point est à l'intérieur par le haut/droite
# Les conditions x >= xMin et y >= yMin vérifient qu'il est à l'intérieur par le bas/gauche
if x <= xMax and y <= yMax and x >= xMin and y >= yMin:
    ans = 1
else:
    # Sinon, on démarre une boucle infinie pour étendre cette zone rectangulaire de manière spécifique
    i = 2  # Cette variable contrôle l'indice dans la liste des nombres de Fibonacci
    while True:
        # Étendre la borne max en x vers la droite en ajoutant fibo[i]
        xMax += fibo[i]
        # Vérifier si le point est maintenant dans la nouvelle zone
        if x <= xMax and y <= yMax and x >= xMin and y >= yMin:
            ans = i
            break
        else:
            i += 1  # Passer au nombre de Fibonacci suivant
        
        # Étendre la borne max en y vers le haut en ajoutant fibo[i]
        yMax += fibo[i]
        # Refaire la vérification d'appartenance du point
        if x <= xMax and y <= yMax and x >= xMin and y >= yMin:
            ans = i
            break
        else:
            i += 1
        
        # Étendre la borne min en x vers la gauche en soustrayant fibo[i] (car on va vers la gauche)
        xMin -= fibo[i]
        # Vérifier de nouveau l'appartenance
        if x <= xMax and y <= yMax and x >= xMin and y >= yMin:
            ans = i
            break
        else:
            i += 1
        
        # Étendre la borne min en y vers le bas en soustrayant fibo[i]
        yMin -= fibo[i]
        # Dernière vérification
        if x <= xMax and y <= yMax and x >= xMin and y >= yMin:
            ans = i
            break
        else:
            i += 1

# À la sortie de la boucle, on calcule ans modulo 3
# Cela adapte la réponse dans un cycle de 3
ans %= 3

# Si le résultat modulo 3 est 0, on ajuste ans à 3 afin d'éviter un résultat nul
if ans == 0:
    ans = 3

# Afficher la réponse finale
print(ans)