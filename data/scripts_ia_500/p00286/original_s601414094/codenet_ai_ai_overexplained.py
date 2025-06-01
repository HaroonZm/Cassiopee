from string import digits, ascii_uppercase

# Définition de la fonction principale de parsing appelé 'parse'
# Elle prend en paramètres :
# - S : une chaîne de caractères représentant une expression à parser
# - N : un entier (taille des permutations)
# - R : un dictionnaire associant des lettres à des permutations (listes d'entiers)
def parse(S, N, R):
    # On ajoute un caractère '$' en fin de chaîne, pour signaler la fin de l'expression
    S = S + "$"
    
    # Variable 'cur' qui mémorise la position actuelle dans la chaîne S
    cur = 0
    
    # Définition d'une fonction interne 'expr' qui va parser une expression complète
    def expr():
        # 'nonlocal cur' permet de modifier la variable 'cur' définie dans la fonction parente 'parse'
        nonlocal cur
        
        # Initialisation d'une liste 'r0' comme une permutation identitaire [0, 1, ..., N-1]
        # Utilisation de l'étoile dans *r0, = range(N) signifie que l'on crée la liste à partir de l'itérable range(N)
        *r0, = range(N)
        
        # Boucle infinie : on va continuer à parser des termes et agréger leurs résultats
        while 1:
            # On appelle la fonction 'term' qui retourne une permutation
            r = term()
            
            # On met à jour r0 par la composition de la permutation r0 suivie de la permutation r
            # r0[:] = [r0[e] for e in r] correspond à r0 = r0 ◦ r (composition de permutations)
            # On remplace le contenu de la liste r0 in-place uniquement
            r0[:] = [r0[e] for e in r]
            
            # On vérifie si le caractère actuel dans S est différent de '+' pour sortir de la boucle
            if S[cur] != '+':
                break
            
            # Si on a un '+', on avance le curseur 'cur' d'un caractère pour continuer le parsing
            cur += 1 # on ignore désormais le caractère '+'
        
        # Retour de la permutation finale après avoir appliqué tous les termes séparés par '+'
        return r0
    
    # Définition de la fonction interne 'term' qui parse un terme dans l'expression
    def term():
        nonlocal cur
        
        # Si le caractère courant S[cur] est un chiffre (donc présence d'un coefficient k)
        if S[cur] in digits:
            # On récupère le nombre entier k en lisant les chiffres à la suite (ex: 12)
            k = number()
            
            # Si le caractère suivant est une parenthèse ouvrante '('
            if S[cur] == '(':
                cur += 1 # avance d'un caractère pour passer la '('
                r = expr() # on parse récursivement une expression entre parenthèses
                cur += 1 # avance d'un caractère pour passer la ')'
            else:
                # Sinon il n'y a pas de parenthèse, on prend l'identité pour le terme
                r = identity()
            
            # On élève la permutation r à la puissance k en la composant k fois (exponentiation rapide)
            r = power(r, k)
        
        else:
            # Si pas de chiffre devant, on retourne directement une permutation issue d'un symbole (lettre)
            r = identity()
        
        # Retourne la permutation obtenue pour ce terme
        return r
    
    # Fonction interne pour calculer la puissance k-ième d'une permutation r
    def power(r, k):
        # Création d'une liste r0 initialisée à l'identité [0, 1, ..., N-1]
        *r0, = range(N)
        # 'r1' sera une copie de la permutation r, car on va l'élever récursivement par exponentiation binaire
        r1 = r[:]
        
        # Tant que k n'est pas nul on boucle
        while k:
            # Si le bit de poids faible de k vaut 1, on compose r0 avec r1
            if k & 1:
                r0[:] = [r0[e] for e in r1]
            
            # On élève r1 au carré : r1 = r1 ◦ r1 (composition de la permutation avec elle-même)
            r1[:] = [r1[e] for e in r1]
            
            # Décalage binaire à droite de k (division entière par 2)
            k >>= 1
        
        # On retourne la permutation r0 élevée à la puissance k
        return r0
    
    # Fonction interne pour parser un nombre entier dans la chaîne S à partir de la position cur
    def number():
        nonlocal cur
        v = 0 # initialisation du nombre
        # Tant que le caractère courant est un chiffre, on calcule le nombre entier en base 10
        while S[cur] in digits:
            v = 10*v + int(S[cur]) # conversion du caractère en entier et accumulation
            cur += 1 # passage au caractère suivant
        return v
    
    # Fonction interne pour retourner la permutation associée à un symbole (lettre majuscule)
    def identity():
        nonlocal cur
        r = R[S[cur]] # récupération de la permutation dans le dictionnaire R via le symbole S[cur]
        cur += 1 # avancée du curseur
        return r
    
    # Démarrage du parsing en appelant expr() sur toute la chaîne S
    return expr()

# Fonction principale main pour la gestion des entrées sorties
def main():
    # Lecture des deux entiers N, K
    N, K = map(int, input().split())
    
    # Initialisation d'un dictionnaire R qui mappe des lettres à des permutations
    R = {}
    
    # Lecture des K permutations nommées
    for i in range(K):
        # Lecture du symbole p (str) et de la hauteur h (int)
        p, h = input().split()
        h = int(h)
        
        # On initialise la permutation correspondant à p comme la permutation identité
        *r, = range(N)
        
        # Pour chaque hauteur -1 (on applique des opérations pour obtenir la permutation composée)
        for i in range(h-1):
            # Lecture d'une liste de N-1 entiers qui représentent des swaps à effectuer entre voisins
            *g, = map(int, input().split())
            # Pour chaque position j de 0 à N-2
            for j in range(N-1):
                # Si la valeur g[j] est 1, on échange les éléments d'indice j et j+1 dans la permutation
                if g[j]:
                    r[j], r[j+1] = r[j+1], r[j]
        
        # On associe cette permutation au symbole p dans le dictionnaire
        R[p] = r
    
    # Lecture du nombre d'expressions E
    E = int(input())
    
    # Pour chaque expression à traiter
    for i in range(E):
        S = input() # lecture de l'expression
        res = parse(S, N, R) # parsing de l'expression pour obtenir la permutation résultante
        
        # Impression des résultats en décalant les indices de permutations de 0-base à 1-base
        # print avec * pour décompresser la liste et map pour ajouter 1 à chaque élément
        print(*map(lambda x: x+1, res))

# Appel direct de la fonction main pour exécuter le programme
main()