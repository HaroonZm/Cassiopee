# Demande à l'utilisateur de saisir une valeur entière qui sera le nombre de requêtes.
# La fonction input() lit une entrée utilisateur sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne de caractères en un entier.
n = int(input())

# Création d'une liste 'queries' qui va contenir toutes les requêtes saisies par l'utilisateur.
# L'opérateur [] est utilisé pour définir une liste vide qui sera remplie grâce à une compréhension de liste.
# La compréhension de liste itère 'n' fois, parce qu'il y a 'n' requêtes à lire.
# Pour chaque itération avec l'indice 'i' (de 0 jusqu'à n-1), on fait ce qui suit :
# 1. input().split() lit une nouvelle ligne depuis l'entrée utilisateur, la découpe en morceaux (chaque morceau séparé par un espace devient un élément de liste)
# 2. map(int, ...) applique la fonction int() à chaque élément de cette liste de chaînes, transformant chaque valeur en entier
# 3. list(...) convertit l'objet map en une vraie liste d'entiers
queries = [list(map(int, input().split())) for i in range(n)]

# Initialisation des variables s et t. Ces deux variables sont utilisées pour stocker des valeurs entières.
# s reçoit la valeur 1. Cela signifie que les opérations sur s agiront comme sur une base multiplicative (car on multipliera s à chaque étape). 
# t reçoit la valeur 0. Cela signifie que les opérations ultérieures sur t imiteront le comportement d'une somme (addition, soustraction, multiplication).
s = 1
t = 0

# Traite chaque requête contenue dans la liste 'queries'.
# Une boucle for standard est utilisée pour parcourir la liste.
# À chaque itération, q est une référence à la requête courante, c'est-à-dire une liste d'entiers correspondant à une commande.
for q in queries:
    # Teste la première valeur (indice 0) de la requête 'q'.
    # Si cette valeur vaut 1, alors la requête demande une multiplication.
    if q[0] == 1:
        # Multiplie la variable 's' par la seconde valeur (indice 1) de la requête 'q'.
        # Cela permet d'accumuler la valeur de 's' en multipliant à chaque fois la nouvelle valeur.
        s *= q[1]
        # Multiplie également la variable 't' par la même valeur.
        # Cela met à jour 't' de façon multiplicative de la même manière que 's'.
        t *= q[1]
    # Si la première valeur de la requête est 2, cela signifie que nous devons ajouter la seconde valeur à 't'.
    elif q[0] == 2:
        # Ajoute la seconde valeur de la requête à la variable 't'.
        t += q[1]
    # Si la première valeur de la requête n'est ni 1 ni 2 (donc ici, cela signifie que c'est 3), nous faisons une soustraction.
    else:
        # Soustrait la seconde valeur de la requête à la variable 't'.
        t -= q[1]

# Affiche les résultats finaux.
# La fonction print() affiche une ou plusieurs valeurs à l'écran, séparées par des espaces par défaut.
# Ici, on affiche la valeur opposée de 't' (c'est-à-dire -t, l'opposé de 't') puis la valeur actuelle de 's'.
print(-t, s)