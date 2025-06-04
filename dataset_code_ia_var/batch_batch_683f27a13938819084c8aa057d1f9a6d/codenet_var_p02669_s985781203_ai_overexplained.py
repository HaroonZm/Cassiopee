import sys  # Le module sys permet d'interagir avec l'interpréteur Python

# Par défaut, la limite de récursion en Python est assez basse (~1000). Ici, on l'augmente pour permettre plus d'appels récursifs
sys.setrecursionlimit(10 ** 6)  # 10 ** 6 = 1000000. Ceci autorise un million de récursions

# Déclaration d'une variable 'inf' pour représenter une valeur infinie
inf = float('Inf')  # float('Inf') renvoie une valeur flottante qui représente l'infini positif

# Création d'une liste 'f' contenant les facteurs 2, 3 et 5 qui serviront à diviser les nombres par la suite
f = [2, 3, 5]

# Création d'une liste 'cost' de taille 4 initialisée à zéro : ceci stockera les coûts d'opérations pour chaque facteur et l'opération de base
cost = [0] * 4  # Cette notation crée une liste de quatre zéros : [0, 0, 0, 0]

# Création d'un dictionnaire vide nommé 'd', qui sera utilisé pour la mémoïsation afin d'optimiser la récursion
d = dict()  # C'est un dictionnaire Python classique, utilisé pour stocker les solutions déjà trouvées

# Définition d'une fonction récursive 'dfs' (depth-first search) prenant deux paramètres :
#  - x : l'entier dont on cherche le coût minimal de réduction à 0
#  - d : le dictionnaire pour la mémoïsation
def dfs(x, d):
    # Vérifier si le résultat pour x a déjà été calculé. Cela réduit énormément la complexité en évitant les calculs redondants
    if x in d:
        return d[x]  # Si oui, retourne le coût mémorisé

    # Initialement, on suppose que la seule opération réalisable est de soustraire 1 de x autant de fois qu'il le faut.
    # Le coût total sera donc cost[-1] (coût de l'opération de base : -1) multiplié par x (nombre de fois à l'appliquer)
    ret = cost[-1] * x  # cost[-1] désigne le dernier élément de la liste cost

    # On va ensuite essayer chaque facteur parmi 2, 3 et 5 pour voir s'il est plus optimal de diviser x par ce facteur
    for i in range(3):  # Boucle sur les indices 0, 1, 2, pour f = 2, 3, 5
        if x < f[i]:
            continue  # Si x est plus petit que le facteur, on ne peut pas diviser, on passe au suivant

        if x % f[i] == 0:
            # x est exactement divisible par f[i], donc pas de reste
            # On peut appliquer le coût de la division puis résoudre récursivement pour x // f[i]
            ret = min(
                ret,  # Le choix est entre le coût actuel et l'alternative qui suit
                dfs(x // f[i], d) + cost[i]  # Coût de résoudre pour x divisé par f[i] + coût d'utiliser ce facteur
            )
        else:
            # x n'est pas divisible par f[i], il y a un reste
            k = x // f[i]  # k est le quotient entier de x divisé par f[i]
            # Première option : on réduit x à k*f[i] en soustrayant (x % f[i]) fois l'opération 'soustraire 1'
            ret = min(
                ret,
                cost[i] + dfs(k, d) + (x % f[i]) * cost[-1]
                # cost[i] : coût de division par f[i]
                # dfs(k, d) : coût pour atteindre 0 à partir de k
                # (x % f[i]) * cost[-1] : coût pour soustraire le reste pour atteindre un multiple de f[i]
            )
            # Deuxième option : on augmente x à (k+1)*f[i] en ajoutant ((k+1)*f[i] - x) fois l'opération 'ajouter 1'
            ret = min(
                ret,
                cost[i] + dfs(k + 1, d) + ((k + 1) * f[i] - x) * cost[-1]
                # Pareil que ci-dessus, mais au lieu de soustraire, on "ajoute" (en fait ici c'est traité pareil)
            )

    # Après avoir essayé toutes les options, on enregistre le coût minimal trouvé pour x dans le dictionnaire de mémoïsation
    d[x] = ret  # Cela permet d'accélérer les prochains appels à dfs(x, d)
    return ret  # On retourne le coût minimal obtenu pour réduire x à 0

# Définition de la fonction principale du programme
def main():
    # Lecture du nombre de tests à effectuer, depuis l'entrée standard
    T = int(input())  # input() lit une ligne au clavier, int() convertit cette ligne en entier

    # Boucle principale : on répète la résolution pour chaque jeu de données d'entrée
    for _ in range(T):  # Le souligné (_) est une variable anonyme quand la valeur importée n'est pas utilisée
        N, *c = map(int, input().split())
        # input().split() lit la ligne contenant les N et les 4 coûts (séparés par des espaces) et les sépare en chaîne
        # map(int, ...) convertit chaque chaîne en entier
        # N récupère le premier entier, *c récupère le reste dans une liste [c0, c1, c2, c3]

        # On copie les coûts d'opérations dans la liste cost pour ce test
        for i in range(4):
            cost[i] = c[i]  # cost[i] correspond à c[i], pour chaque opération possible

        # Appel de dfs en passant N et un nouveau dictionnaire vide pour la mémoïsation.
        # On affiche le coût minimal obtenu à la sortie
        print(dfs(N, dict()))

# Instruction pour appeler la fonction principale lorsqu'on exécute le fichier
main()  # Cela lance tout le traitement défini ci-dessus