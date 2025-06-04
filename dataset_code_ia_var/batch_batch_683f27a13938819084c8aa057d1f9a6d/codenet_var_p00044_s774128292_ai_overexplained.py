import sys  # Module qui permet d'accéder à des fonctionnalités système comme la gestion des entrées standard

# Création d'une liste de booléens pour déterminer si un nombre est premier
# La variable p est une liste de taille 55000 où chaque élément est initialisé à True
# Cela suppose que tous les nombres de 0 à 54999 sont premiers au départ
p = [True] * 55000

# Les indices 0 et 1 de la liste correspondent aux nombres 0 et 1
# Par définition, 0 et 1 ne sont pas des nombres premiers
# On les marque donc explicitement comme False
p[0] = False
p[1] = False

# Utilisation de la méthode du crible d'Ératosthène pour trouver tous les nombres premiers <= 54999
# On parcourt tous les entiers de 2 à 54999 inclus (le dernier indice est 54999 car range va jusqu'à 55000-1)
for i in range(2, 55000):
    # Si le nombre à l'indice i est encore considéré comme premier (True)
    if p[i]:
        # On va marquer comme non-premiers (False) tous les multiples de i à partir de 2*i
        # Cela élimine tous les multiples de i différents de i lui-même, puisqu'ils ne sont pas premiers
        # La fonction range(j, k, s) commence à j, s'arrête avant k, et fait des sauts de s
        for j in range(i * 2, 55000, i):
            # Ce multiple n'est donc pas un nombre premier
            p[j] = False

# On lit l'entrée utilisateur à partir de l'entrée standard (sys.stdin)
# sys.stdin.read() lit tout d'un coup jusqu'à la fin du flux d'entrée
# On retire les espaces ou les retours à la ligne en ligne de fin avec rstrip()
# On divise l'entrée en lignes avec split('\n')
for s in sys.stdin.read().rstrip().split('\n'):
    # Pour chaque chaîne s lue (chaque ligne), on la convertit en un entier n
    n = int(s)

    # Cherche le nombre premier immédiatement inférieur à n
    # On commence la recherche à n-1 et on descend jusqu'à 1 inclus
    for i in range(n - 1, 0, -1):
        # Si p[i] vaut True, i est premier
        if p[i]:
            # On stocke ce nombre premier dans la variable m1
            m1 = i
            # On a trouvé notre nombre, on peut sortir de la boucle avec break
            break

    # Cherche le nombre premier immédiatement supérieur à n
    # On commence la recherche à n+1 et on monte jusqu'à la fin de la liste p
    for i in range(n + 1, len(p)):
        # Si p[i] vaut True, i est premier
        if p[i]:
            # On stocke ce nombre premier dans la variable m2
            m2 = i
            # On a trouvé notre nombre, on peut sortir de la boucle avec break
            break

    # Affiche les deux nombres premiers trouvés, m1 et m2, séparés par un espace
    # L'instruction print sans parenthèses est valide en Python 2
    print m1, m2