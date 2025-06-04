import math  # On importe le module math, qui fournit des fonctions mathématiques, notamment pour la racine carrée.

# Définition d'une fonction appelée isprime qui prend un argument n
def isprime(n):
    # Si n vaut exactement 1, alors la fonction retourne 0 (1 n'est pas un nombre premier)
    if n == 1:
        return 0
    
    # On itère sur les valeurs entières k allant de 2 inclus jusqu'à la racine carrée de n incluse
    # math.sqrt(n) renvoie la racine carrée de n
    # math.floor arrondit vers le bas
    # int convertit le résultat en entier (utile si racine carrée n'est pas entière)
    for k in range(2, int(math.floor(math.sqrt(n))) + 1):
        # Pour chaque valeur de k dans la boucle, on regarde si n est divisible par k
        # L'opérateur % donne le reste de la division
        # Si le reste est nul, alors k divise n et n n'est donc pas premier
        if n % k == 0:
            # Si on trouve un diviseur, on retourne 0 immédiatement
            return 0
    
    # Si aucune division n'a abouti à un reste nul, n est un nombre premier
    # On retourne 1 pour indiquer que n est premier
    return 1

# Début d'une boucle infinie (True est toujours vrai, donc la boucle ne s'arrêtera jamais sauf si un break intervient)
while True:
    # On lit une ligne de l'entrée standard (typiquement le clavier)
    # input() lit la ligne
    # split() découpe la chaîne de caractères en morceaux selon les espaces
    # map(int, ...) convertit chaque morceau en un entier
    # a, d, n reçoivent respectivement les trois entiers lus en entrée
    a, d, n = map(int, input().split())
    
    # On teste si les trois valeurs sont toutes égales à zéro
    # Si c'est le cas, on quitte la boucle avec l'instruction break
    if a == d == n == 0:
        break

    # On initialise une variable num à 0 : elle comptera combien de nombres premiers on a trouvés
    # On initialise kazu à 0 : elle représentera le nombre candidat courant de la suite arithmétique
    kazu = 0
    num = 0

    # On commence une boucle allant de i = 0 jusqu'à i = 999 999 inclus (10**6 donne un million)
    # On utilisera la variable i pour calculer chaque terme de la suite arithmétique
    for i in range(10**6):
        # kazu reçoit le i-ème terme de la suite arithmétique commencant à a et de raison d
        # Chaque terme s'obtient en ajoutant i fois d à a
        kazu = a + i * d
        
        # On vérifie si le nombre kazu est un nombre premier en appelant isprime(kazu)
        # Si oui, isprime renvoie 1 et on entre dans le if
        if isprime(kazu) == 1:
            # On augmente num de 1, car on a trouvé un nombre premier supplémentaire
            num += 1
        
        # On vérifie si le nombre de nombres premiers trouvés est exactement n
        if num == n:
            # On affiche le dernier nombre premier trouvé qui correspond au n-ième nombre premier de la suite
            print(kazu)
            # On sort de la boucle for car on a obtenu la réponse voulue
            break