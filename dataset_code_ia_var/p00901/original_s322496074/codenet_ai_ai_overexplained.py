# Définition de la constante MOD qui servira de base pour les opérations de modulo dans le programme.
MOD = 2011

# Boucle infinie qui ne sera interrompue que par l'exécution explicite d'une instruction break.
while 1:
    # Lecture d'une entrée utilisateur, conversion en entier pour obtenir le nombre de lignes n.
    n = int(input())
    
    # Si n vaut 0, cela signifie qu'on souhaite arrêter, donc on quitte la boucle avec break.
    if n == 0:
        break
    
    # Création d'une liste S de n chaînes de caractères, chaque chaîne étant lue à partir de l'entrée standard.
    # Ici, S représentera la "grille" contenant l'expression écrite en format infixé sur plusieurs lignes éventuellement.
    S = [input() for i in range(n)]
    
    # Détermination de la largeur (nombre de colonnes) de la grille en prenant la longueur de la première chaîne de S.
    w = len(S[0])

    # Définition d'une fonction imbriquée parse servant à analyser et évaluer récursivement une sous-expression délimitée par des bornes.
    def parse(bcur, bright, top, bottom):
        # bcur : position de début de la colonne de la sous-expression à analyser
        # bright : position de fin (exclue)
        # top : ligne supérieure de la sous-expression
        # bottom : ligne inférieure de la sous-expression

        # Initialisation de la variable base à -1. Cette variable va trouver la première ligne contenant autre chose qu'un point ('.').
        base = -1

        # Parcours toutes les colonnes de bcur à bright (exclusive)
        for i in range(bcur, bright):
            # Pour chaque colonne, on cherche la première ligne de haut en bas, de top à bottom (inclus)
            for j in range(top, bottom+1):
                # Si à la position (ligne j, colonne i) on trouve autre chose qu'un point, on a trouvé la base (le “niveau” principal ou le séparateur fractionnel)
                if S[j][i] != '.':
                    base = j
                    break  # On arrête de chercher dès qu'on a trouvé une base
            if base != -1:
                break  # On arrête de chercher dès qu'on a trouvé sur une colonne

        # cur sera la variable de position courante dans la plage de colonnes ; initialisée à bcur
        cur = bcur

        # Définition de la fonction imbriquée read permettant de regarder le caractère courant (différent de '.') sur la ligne base et d'avancer cur jusqu'à ce caractère.
        def read():
            nonlocal cur  # Permet de modifier cur défini dans le parent parse
            c = None  # Initialisation de la variable c à None
            while 0 <= base < n and cur < bright:  # Vérifie que base est valide et cur dans la plage
                # Récupère le caractère à la position (base, cur)
                c = S[base][cur]
                if c != '.':
                    break  # On retourne dès qu'on a trouvé un caractère autre que '.'
                cur += 1  # Sinon on avance cur
            return c

        # Définition de la fonction fraction pour gérer les expressions de type fraction.
        def fraction():
            nonlocal cur
            # left stocke la position actuelle de cur avant de commencer à lire la barre de fraction
            left = cur
            # Déplace cur sur toutes les positions où il y a un tiret '-' à la ligne base, ce qui correspond à la barre de fraction.
            while cur < w and S[base][cur] == '-':
                cur += 1
            # right représente une colonne après la fin de la barre de fraction, pour délimiter le sous-domaine de la fraction.
            right = cur + 1 if cur < w else cur

            # Appel récursif de parse pour la partie supérieure (le numérateur), c'est la zone au-dessus de la barre
            dividend = parse(left, right, top, base - 1)

            # Appel récursif de parse pour la partie inférieure (le dénominateur), c'est la zone en-dessous de la barre
            divisor = parse(left, right, base + 1, bottom)

            # Calcule la valeur de la fraction : division en arithmétique modulaire
            # pow(divisor, MOD-2, MOD) calcule l'inverse modulo MOD du dénominateur divisor
            return (dividend * pow(divisor, MOD - 2, MOD)) % MOD

        # Définition de la fonction primary, qui analyse un nombre ou une expression parenthésée
        def primary():
            nonlocal cur
            # Lecture du caractère courant, qui pourrait être une parenthèse ouvrante ou un chiffre
            c = read()
            # Si le caractère courant est une parenthèse ouvrante (\( )
            if c == '(':
                cur += 1  # On avance après la parenthèse ouvrante
                v = expr()  # On analyse récursivement l'expression à l'intérieur des parenthèses
                cur += 1  # On avance après la parenthèse fermante
                return v  # On retourne la valeur de l'expression parenthésée
            else:
                # Sinon, c'est un chiffre, on avance cur et on retourne la valeur entière du chiffre
                cur += 1
                return int(c)

        # Définition de powexpr qui gère les puissances, par exemple x^n, où la puissance peut être écrite au-dessus d'un chiffre
        def powexpr():
            nonlocal cur
            # On commence par parser la base de la puissance avec primary (un nombre ou parenthèse)
            v = primary()
            # Maintenant, on vérifie s'il y a un exposant écrit une ligne au-dessus et à la même position cur
            if 0 < base and cur < bright and S[base - 1][cur] in "0123456789":
                # Si c'est le cas, on élève v à la puissance indiquée (en modulo MOD, bien sûr)
                return pow(v, int(S[base - 1][cur]), MOD)
            return v  # Sinon, on retourne juste v

        # Définition de factor, pour gérer les facteurs d'un produit ou une fraction ou éventuellement un signe -
        def factor():
            nonlocal cur
            # Lit le prochain caractère significatif
            c = read()
            if c == '-':
                # Si le caractère suivant après '-' est un point, il s'agit d'un signe négatif, pas une barre de fraction
                if S[base][cur + 1] == '.':
                    cur += 1  # On avance après le signe '-' pour traiter le facteur négatif
                    return -factor()  # Retourne l'opposé du facteur qui suit
                else:
                    # Sinon, il s'agit d'une fraction (barre horizontale)
                    return fraction()
            # Sinon, c'est une expression puissance ou un nombre simple
            return powexpr()

        # Définition de term, qui correspond à une série de multiplications
        def term():
            nonlocal cur
            # Initialisation de result à 1 car il servira de produit pour les facteurs successifs
            result = 1
            # Boucle "à la main" qui traite successivement chaque facteur du produit
            while 1:
                v = factor()  # Lecture d'un facteur (un nombre, une parenthèse, une puissance, une fraction, etc.)
                result *= v  # Multiplication du résultat courant par la valeur trouvée
                result %= MOD  # On prend le modulo pour maintenir le résultat dans les bornes requises
                c = read()  # Lit le caractère suivant pour voir si c'est un multiplié '*'
                if c != '*':  # Si ce n'est pas un '*' on s'arrête
                    break
                cur += 1  # Sinon, avance cur pour zapper le caractère '*'
            return result  # Retourne le résultat de la multiplication

        # Définition de expr, qui correspond à une succession de terms reliés par des + ou des -
        def expr():
            nonlocal cur
            op = '+'  # Initialisation du prochain opérateur à '+'
            result = 0  # Initialisation du résultat cumulatif à 0
            while 1:
                v = term()  # Lit un terme (un produit de facteurs)
                # Selon l'opérateur précédent ('+' ou '-'), ajoute ou soustrait v au résultat.
                # Pour la soustraction, (MOD - v) permet de gérer le modulo correctement car on travaille en valeurs non-signées.
                result += v if op == '+' else MOD - v
                result %= MOD  # On prend le modulo à chaque étape
                c = read()  # Lecture du prochain caractère pour déterminer si c'est un + ou un -
                if not c or c not in '+-':
                    break  # Si c n'est ni + ni -, on sort de la boucle
                cur += 1  # Avance cur si on va traiter un nouvel opérateur
                op = c  # Enregistre le nouvel opérateur
            return result  # Retourne la valeur de l'expression

        # Appel initial de expr sur la plage demandée
        v = expr()
        # Retourne la valeur calculée de l'expression
        return v

    # Affichage du résultat du parsing de l'expression (en appelant parse sur toute la largeur et hauteur de la grille)
    print(parse(0, w, 0, n-1))