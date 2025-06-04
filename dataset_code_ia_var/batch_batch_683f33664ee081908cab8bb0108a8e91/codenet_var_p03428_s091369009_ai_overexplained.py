from math import pi, atan2  # Importe les constantes et fonctions utiles du module math
# Plus précisément, 'pi' représente le nombre π ; 'atan2' permet d’obtenir l’argument d’un nombre complexe (angle du vecteur)

q = 2*pi  # 'q' sert à représenter un tour complet de cercle en radians (360 degrés)

def deg(a, b):
    # Cette fonction calcule l’angle orienté entre deux points complexes 'a' et 'b' dans le plan
    # 'a' et 'b' sont deux nombres complexes (x + yj chacun)
    d = b - a  # La soustraction de complexes donne le vecteur allant de 'a' vers 'b'
    t = atan2(d.real, d.imag)  # atan2(y, x) retourne l’angle dont la tangente vaut y/x
    # Ici, d.real est la partie réelle de 'd', d.imag la partie imaginaire
    if t < 0:  # atan2 retourne des valeurs entre -π et π ; on veut toujours des angles positifs
        t += q  # Donc on ajoute 2π si l’angle est négatif
    return t  # On renvoie toujours un angle dans [0, 2π[

n = int(input())  # Lit une ligne de l’entrée standard, convertit en entier : n points à traiter

cs = []  # Liste destinée à contenir les coordonnées complexes des points
for _ in range(n):  # Boucle qui sera exécutée 'n' fois, une fois pour chaque point
    a, b = map(int, input().split())  # Lit deux entiers séparés (coordonnées x, y)
    cs += [complex(a, b)]  # Crée un objet nombre complexe (a + bj) et l’ajoute à la liste

# À ce stade, 'cs' est une liste de nombres complexes représentant tous les points

for i in range(n):  # Pour chaque point (comme point de départ ou de référence)
    # Crée une liste nommée 'args' des arguments normalisés [0,1): angle de chaque autre point relatif au point i
    args = [deg(cs[i], cs[j]) / q for j in range(n) if j != i]
    # Ici, pour chaque autre point j != i :
    # - On appelle la fonction deg pour obtenir l’angle de (cs[j] - cs[i])
    # - On divise le résultat par 2π (q) pour normaliser l’angle en un nombre sur [0,1[
    args = sorted(args)  # Trie la liste des angles normalisés dans l’ordre croissant

    # Calcule les différences entre deux angles consécutifs dans la liste 'args'
    # Cela revient à déterminer la taille des intervalles angulaires formés entre les autres points autour du point 'i'
    # L’idée : Pour n-1 angles (car on ne considère pas le point lui-même), les intervalles sont formés entre args[0] -> args[1], ..., args[n-2] -> args[n-1], puis args[n-1] -> args[0] en tenant compte du cercle
    dif = [args[i] - args[i-1] for i in range(n-1)]
    # Remarque : args[i-1] pour i=0 donne args[-1] (le dernier élément)
    # En Python, args[-1] est bien le dernier élément, donc la première différence calcule args[0] - args[n-2]
    # Mais ici la suite est modifiée à la main :
    dif[0] += 1  # On ajoute 1 uniquement à la première différence pour bien fermer le cercle (on considère le passage de 1 à 0)
    # Après cette opération, le total des valeurs de 'dif' est bien 1, couvrant tout le cercle

    # On cherche le plus grand des intervalles (le plus grand trou angulaire vu du point i), qu’on ajuste
    res = max(dif) - 1/2  # On retire 1/2 (correspondant à un demi-cercle) au plus grand écart angulaire
    # S’il n’y a aucun intervalle de taille supérieure à 1/2, alors le résultat sera négatif (on ramène ça à 0)
    print(max(res, 0))  # Affiche le résultat, mais ne retourne jamais de nombre négatif (max avec 0)
    # Ainsi, on affiche pour chaque point la taille du plus grand arc supérieur à un demi-cercle (s’il y en a), ou 0 sinon