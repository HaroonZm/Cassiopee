import sys  # Importation du module sys qui permet d'interagir avec le système, ici pour lire les entrées standard
import itertools  # Importation du module itertools qui propose des fonctions pour manipuler les itérateurs (non utilisé dans ce code mais importé)
readline = sys.stdin.readline  # Affectation de la méthode readline de sys.stdin à une variable pour faciliter la lecture des lignes d'entrée

while True:  # Boucle infinie qui sera interrompue avec un break lorsque la condition d'arrêt sera rencontrée
    N = int(readline())  # Lecture d'une ligne depuis l'entrée standard, conversion en entier; N représente le nombre de noeuds ou sommets
    M = int(readline())  # Lecture d'une autre ligne, conversion en entier; M représente le nombre de paires ou arêtes
    if N == 0 and M == 0:  # Condition d'arrêt: si les deux nombres lus sont zéro, on sort de la boucle car cela signifie la fin des cas à traiter
        break  # Sortie de la boucle while
    
    pairs = set()  # Création d'un ensemble vide qui va contenir les paires (arêtes) sous forme de tuples; set permet d'éviter les doublons
    
    # La boucle for itère M fois, correspondant au nombre d'arêtes à lire
    for _ in xrange(M):  # xrange est utilisée pour générer une séquence de nombres sans créer une liste entière (dans Python 3 il faut utiliser range)
        # Lecture d'une ligne, séparation de la chaîne en éléments par les espaces, conversion de chaque élément en entier
        a, b = tuple(int(x) for x in readline().split())  # On obtient deux entiers qui représentent une arête entre a et b
        
        pairs.add((a, b))  # Ajout du tuple (a,b) dans l'ensemble pairs; cela représente une arête allant de a vers b
        pairs.add((b, a))  # Ajout aussi du tuple (b,a) dans l'ensemble pairs; on considère donc les arêtes comme non orientées en ajoutant les deux sens

    cnt = 0  # Initialisation d'un compteur à zéro; ce compteur servira à compter certains résultats
    
    # On parcourt tous les sommets i allant de 2 à N inclus
    for i in xrange(2, N + 1):
        if (1, i) in pairs:  # On vérifie si une arête directe existe entre 1 et i
            cnt += 1  # Si oui, on incrémente le compteur car c'est un chemin direct accepté
        else:  # Sinon, on cherche un parcours alternatif passant par un sommet j différent de 1 et i
            for j in xrange(2, N + 1):  # On teste tous les sommets j de 2 à N pour voir s'il sert de pont
                if (1, j) in pairs and (j, i) in pairs:  # Si on peut aller de 1 à j et de j à i
                    cnt += 1  # On incrémente le compteur car on a trouvé un chemin de longueur 2 (via j)
                    break  # On arrête la recherche de j car on a trouvé une voie valable pour cet i

    print cnt  # Affichage du résultat final: nombre de sommets i accessibles depuis 1 directement ou via un autre sommet j en deux étapes maximum