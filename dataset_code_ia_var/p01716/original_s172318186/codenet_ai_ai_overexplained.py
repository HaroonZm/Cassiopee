# Définition de la fonction "dfs" (depth-first search)
def dfs(p, s, c, cmin, cmax):
    # Si la liste "p" ne contient plus d'éléments, c'est la condition d'arrêt de la récursion.
    # On effectue alors le calcul final en appelant la fonction "solve"
    if len(p) == 0:
        return solve(s, c, cmin, cmax)
    
    # On récupère le premier élément de la liste "p", qui est un tuple : (lower, u)
    lower, u = p[0]
    
    # On ajoute le caractère "lower" à la chaîne de caractères "c"
    c += lower
    
    # On vérifie si la valeur entière "u" est inférieure ou égale à 9
    if u <= 9:
        # Si oui, on met à jour le dictionnaire "cmin" (plancher) pour "lower" avec 0 comme valeur minimale
        cmin[lower] = 0
        # On met à jour le dictionnaire "cmax" (plafond) pour "lower" avec "u" comme valeur maximale
        cmax[lower] = u
        # On continue la recherche récursive sur le reste de la liste "p" avec la chaîne modifiée
        return dfs(p[1:], s, c, cmin, cmax)
    
    # Si "u" est supérieur à 9 :
    # On met à jour le plafond pour "lower" à 9
    cmin[lower] = 0
    cmax[lower] = 9
    # On effectue une recherche récursive sur le reste de "p" et on sauvegarde le résultat dans "ret"
    ret = dfs(p[1:], s, c, cmin, cmax)
    
    # On crée la majuscule du caractère "lower"
    upper = lower.upper()
    # On modifie la chaîne "s" en remplaçant chaque "lower" par "upper" suivi de "lower"
    s = s.translate(str.maketrans({lower: upper + lower}))
    
    # On ajoute le caractère majuscule "upper" à la chaîne "c"
    c += upper
    # Si le chiffre des unités de "u" est 9 (vérifie si le dernier chiffre est 9)
    if u % 10 == 9:
        # On met à jour les bornes pour "upper"
        cmin[upper] = 1
        cmax[upper] = u // 10
        # On additionne à "ret" le résultat de l'appel récursif, puis on retourne la somme
        return ret + dfs(p[1:], s, c, cmin, cmax)
    # Si "u" est supérieur ou égal à 20
    if 20 <= u:
        # On ajuste les bornes pour "upper"
        cmin[upper] = 1
        cmax[upper] = u // 10 - 1
        # On ajoute le résultat de l'appel récursif à "ret"
        ret += dfs(p[1:], s, c, cmin, cmax)
    # On ajuste les bornes pour "lower" avec le modulo 10 de "u" (le chiffre des unités)
    cmin[lower] = 0
    cmax[lower] = u % 10
    # On ajuste les bornes pour "upper" avec la division entière par 10 de "u"
    cmin[upper] = u // 10
    cmax[upper] = u // 10
    # Enfin, on retourne la somme de "ret" et de la dernière recherche récursive
    return ret + dfs(p[1:], s, c, cmin, cmax)

# Définition de la fonction "solve" qui effectue des opérations sur la chaîne de caractères et sur les bornes de chaque caractère
def solve(s, c, cmin, cmax):
    # On crée une liste "uf" (union-find) de taille 128 (pour chaque caractère ASCII), chaque valeur est initialisée à -1
    uf = [-1] * 128
    # On récupère la moitié gauche de la chaîne "s", et on convertit chaque caractère en son code ASCII
    s1 = map(ord, s[:len(s)//2])
    # On récupère la moitié droite de la chaîne "s", mais renversée, et on la convertit aussi en codes ASCII
    s2 = map(ord, s[::-1][:len(s)//2])
    # On parcourt en parallèle les deux moitiés
    for p, q in zip(s1, s2):
        # On trouve la racine de "p" et "q" dans la structure union-find
        p = root(uf, p)
        q = root(uf, q)
        # Si les racines sont différentes, on fusionne les ensembles correspondants
        if p != q:
            # On fusionne le plus petit ensemble dans le plus grand pour garder l'arbre plat
            if uf[p] >= uf[q]:
                uf[p] += uf[q]
                uf[q] = p
            else:
                uf[q] += uf[p]
                uf[p] = q
    
    # On prépare deux dictionnaires pour les bornes réelles après fusion
    nmin, nmax = {}, {}
    # Pour chaque caractère dans la chaîne "c"
    for ci in c:
        # On trouve la racine de ci (converti en code ASCII)
        p = root(uf, ord(ci))
        # On convertit le résultat racine en string pour s'en servir comme clé
        p = str(p)
        try:
            # Si la clé existe déjà, on prend le min/max approprié pour la borne fusionnée
            nmax[p] = min(nmax[p], cmax[ci])
            nmin[p] = max(nmin[p], cmin[ci])
        except KeyError:
            # Si la clé n'existe pas encore, on l'affecte directement
            nmax[p] = cmax[ci]
            nmin[p] = cmin[ci]
    
    # On initialise le résultat à 1 (neutre pour la multiplication)
    ret = 1
    # Pour chaque classe de racines
    for p in nmax.keys():
        # Si la borne min est strictement supérieure à la borne max, alors il n'y a pas de solution
        if nmax[p] < nmin[p]:
            return 0
        # Sinon, on multiplie le résultat par le nombre de valeurs possibles pour chaque classe (max-min+1)
        ret *= nmax[p] - nmin[p] + 1
    # On retourne le résultat final
    return ret

# Définition de la fonction "root", qui trouve la racine de l'ensemble (pour union-find)
def root(uf, p):
    # Si la valeur est négative, c'est un représentant racine
    if uf[p] < 0:
        return p
    # Sinon, on effectue la compression de chemin pour accélérer les appels suivants
    uf[p] = root(uf, uf[p])
    return uf[p]

# Import du module "sys" pour lire l'entrée standard
import sys
f = sys.stdin

# Lecture et conversion de la première ligne (non utilisée ici, on écrase les variables avec un "_", car le contenu n'est pas exploité)
_, _ = map(int, f.readline().split())

# Lecture de la deuxième ligne pour récupérer la chaîne "s" en supprimant le caractère de fin de ligne éventuel
s = f.readline().strip()

# Lecture de toutes les autres lignes du flux d'entrée, chaque ligne est séparée en une liste de chaînes avec split()
p = [line.split() for line in f]

# Pour chaque élément de p (qui sont des listes [caractère, nombre]), on convertit la seconde position en entier
for pi in p:
    pi[1] = int(pi[1])

# On prépare deux dictionnaires : cmin et cmax, pour chaque caractère chiffre de '0' à '9'
# cmin fixe la valeur minimale autorisée, cmax la valeur maximale autorisée, on commence par chaque chiffre peut être lui-même
cmin, cmax = {str(i): i for i in range(10)}, {str(i): i for i in range(10)}

# On prépare la chaîne "characters" qui contient tous les chiffres de 0 à 9 inclus
characters = '0123456789'

# On appelle la fonction dfs (départ de la récursion) et on affiche le résultat modulo 10^9 + 7 pour éviter les débordements
print(dfs(p, s, characters, cmin, cmax) % (10 ** 9 + 7))