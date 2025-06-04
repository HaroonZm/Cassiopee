# Demande à l'utilisateur de saisir un nombre entier. La fonction input() lit la saisie utilisateur comme une chaîne de caractères.
# La fonction int() convertit cette chaîne en un nombre entier en base 10.
N = int(input())

# Définit la fonction gcd qui calcule le plus grand commun diviseur (PGCD) de deux entiers m et n.
def gcd(m, n):
    # Boucle qui continue tant que n n'est pas zéro. La condition n est vraie tant que n != 0.
    while n:
        # Effectue l'algorithme d'Euclide : à chaque itération,
        # m prend la valeur de n, et n prend la valeur du reste de la division entière de m par n.
        m, n = n, m % n
    # Lorsque n atteint 0, m est le PGCD recherché.
    return m

# Définit la fonction lcm qui calcule le plus petit commun multiple (PPCM) de deux entiers m et n.
def lcm(m, n):
    # Le PPCM de m et n est égal à m fois n divisé par leur PGCD. 
    # Ici, on effectue d'abord la division entière m // gcd(m, n) puis on multiplie par n.
    return m // gcd(m, n) * n

# Définit la fonction carmichael qui calcule la fonction de Carmichael pour un entier x.
# La fonction de Carmichael lambda(n) est le plus petit entier t tel que a^t ≡ 1 (mod n) pour tout a coprime avec n.
def carmichael(x):
    # Initialise la variable r à 1 ; elle stockera la valeur finale de la fonction de Carmichael.
    r = 1

    # Compte le nombre de facteurs 2 dans x et stocke ce nombre dans b.
    b = 0
    # La condition x & 1 == 0 teste si x est pair : un nombre pair a le dernier bit à 0.
    while x & 1 == 0:
        # Incrémente b de 1 à chaque fois que x est divisible par 2.
        b += 1
        # Fait un décalage de bits à droite sur x, c'est-à-dire divise x par 2 (x >>= 1).
        x >>= 1
    # Gère le cas où x était divisible par plusieurs 2 au départ.
    if b > 1:
        # Si b == 2, alors le facteur pour la partie 2 de la décomposition est 2.
        # Sinon, c'est 2^(b-2), conformément à la définition de la fonction de Carmichael pour les puissances de 2.
        r = 2 if b == 2 else 2**(b-2)

    # Commence à vérifier les facteurs premiers impairs de x à partir de y = 3.
    y = 3
    # Tant que y*y <= x, c'est-à-dire que y est inférieur ou égal à la racine carrée de x.
    while y*y <= x:
        # Si y divise x sans reste, alors y est un facteur premier de x.
        if x % y == 0:
            # Initialise le compteur c à 0, il va compter la puissance de y dans x.
            c = 0
            # Tant que x est divisible par y, divise x par y et incrémente c.
            while x % y == 0:
                x //= y
                c += 1
            # Met à jour r avec le PPCM de r et (y-1) * y^(c-1) qui est la valeur de Lambda pour un facteur premier impair.
            r = lcm(r, (y-1) * y**(c-1))
        # Passe au nombre impair suivant.
        y += 1
    # À la fin, s'il reste un facteur premier supérieur à la racine carrée de x (x > 1), le prendre en compte aussi.
    if x > 1:
        r = lcm(r, x-1)
    # Retourne la valeur calculée de lambda.
    return r

# Définit la fonction solve qui cherche l'ordre multiplicatif de x modulo c (le plus petit k > 0 tel que x^k ≡ 1 mod c).
def solve(x, c):
    # Si c vaut 1, alors pour tout x on a x^k ≡ 0 mod 1 pour tout k, donc on retourne 1 comme cas particulier.
    if c == 1:
        return 1
    # On réduit x modulo c pour éviter les grands nombres.
    x = x % c
    # On définit sq comme la partie entière de la racine carrée de c plus 1. 
    # Cela sert pour la méthode de "baby-step giant-step" pour trouver l'ordre.
    sq = int(c ** .5) + 1

    # Déclare un dictionnaire vide pour mémoriser les puissances déjà calculées.
    mp = {}
    # Initialise y à 1, c'est x^0 modulo c.
    y = 1
    # Premier parcours pour remplir le dictionnaire avec les puissances les plus basses ("baby-step").
    for i in range(sq):
        # Associe à chaque valeur (y) l'exposant correspondant (i).
        mp[y] = i
        # Calcule la prochaine puissance de x: y = y * x modulo c.
        y = (y * x) % c
        # Si on tombe sur 1, cela signifie que l'ordre est i+1.
        if y == 1:
            return i+1
        # Si cette puissance a déjà été rencontrée, alors il y a une collision non triviale (boucle), donc pas de solution.
        if y in mp:
            return -1
    # Si on n'a pas encore trouvé l'ordre, on procède au "giant-step".
    z = 1
    # On itère sur sq termes pour essayer de retrouver une puissance vue précédemment (collision).
    for i in range(sq):
        # Multiplie z par la dernière puissance (qui était y à la fin de la boucle précédente), modulo c.
        z = (z * y) % c
        # Si cette puissance a été vue précédemment dans mp, alors on peut calculer l'ordre par la formule suivante :
        if z in mp:
            # On utilise les indices renvoyés pour déterminer l'ordre minimal.
            return sq*(i+1) - mp[z]
    # Si aucune collision n'a été trouvée, cela signifie que l'ordre n'existe pas, on retourne -1.
    return -1

# Calcule la fonction de Carmichael pour N, qui sera le module servant à chercher l'ordre.
c = carmichael(N)
# Cherche l'ordre multiplicatif de N modulo c.
k = solve(N, c)
# Vérifie que l'ordre est valide : si pas trouvé ou si la condition x^k ≡ 1 mod c n'est pas satisfaite,
# alors on affiche -1. On utilise pow(N, k, c) pour calculer N^k modulo c efficacement.
if k == -1 or pow(N, k, c) != 1 % c:
    print(-1)
else:
    print(k)