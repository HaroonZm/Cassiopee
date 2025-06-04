# Définition de la fonction gcd pour trouver le plus grand commun diviseur (GCD) de deux nombres entiers
def gcd(a, b):
    # Utilisation de l'algorithme d'Euclide
    # Tant que b n'est pas égal à zéro
    while b:
        # Remplacement de a par b, et de b par le reste de la division de a par b
        # Ceci fait progresser l'algorithme vers la condition d'arrêt où b devient 0
        a, b = b, a % b
    # Une fois que b vaut 0, a est le GCD que l'on retourne
    return a

# Définition de la fonction f qui calcule l'ordre multiplicatif de 10 modulo m
def f(n, m):
    # Si m vaut 1 alors, par convention, on retourne 0 (aucune puissance ne convient)
    if m == 1:
        return 0
    # On initialise une variable x à 1 (qui représentera n^i modulo m)
    x = 1
    # On parcourt tous les entiers i de 0 jusqu'à m-1 inclus
    for i in range(m):
        # On multiplie x par n puis on applique le modulo m (pour rester dans Z/mZ)
        x = (x * n) % m
        # Si x est redevenu égal à 1 pour la première fois (autre que i=0)
        if x == 1:
            # Cela signifie que l'ordre est trouvé, on retourne i+1 (car on démarre à i=0)
            return i + 1

# Boucle principale du programme, s'exécutera indéfiniment sauf interruption volontaire à l'intérieur
while 1:
    # Lit une ligne de l'entrée standard, sépare les deux entiers saisis et les convertit en entiers avec map
    a, b = map(int, input().split())
    # Si a est égal à 0, on arrête le programme avec break (condition de sortie volontaire)
    if a == 0:
        break
    # Calcule du plus grand commun diviseur de a et b, que l'on stocke dans c
    c = gcd(a, b)
    # Division entière de a par c afin de rendre a et b premiers entre eux (simplification de la fraction)
    a //= c
    # Idem, division entière de b par c
    b //= c
    # Initialisation d'un compteur cnt à 0, il servira à compter les facteurs 2 et 5 supprimés de b
    cnt = 0
    # Calcul du GCD de b et 10, pour voir si b est divisible par 2 ou 5
    d = gcd(b, 10)
    # Tant qu'il existe un facteur commun entre b et 10 (c'est-à-dire tant qu'on détecte des 2 ou 5 dans b)
    while d != 1:
        # On divise b par d (c'est-à-dire qu'on enlève ce facteur commun, qui sera soit 2 soit 5)
        b //= d
        # On incrémente le compteur cnt, car on vient de retirer un facteur 2 ou 5
        cnt += 1
        # On recalcule d pour voir s'il reste encore des facteurs 2 ou 5
        d = gcd(b, 10)
    # Enfin, on affiche le résultat sous la forme de deux valeurs :
    # Le nombre de facteurs 2 et 5 retirés de b (cnt)
    # L'ordre multiplicatif de 10 modulo b (nombre de chiffres de la période dans la décimale de 1/b)
    print(cnt, f(10, b))