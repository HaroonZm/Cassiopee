# Définition d'une variable pour stocker le modulo utilisé dans tous les calculs pour éviter les dépassements d’entier
mod = 10**9 + 7  # 10 puissance 9 plus 7, un grand nombre premier classique en algorithmique

# Initialisation de deux listes vides pour stocker les factorielles et leurs inverses modulo 'mod'
fac = []  # Cette liste contiendra fac[i] = (i!) % mod
pw = []   # Cette liste contiendra pw[i] = inverse modulo de fac[i] par rapport à 'mod'

# Calcul de la factorielle de 0 modulo 'mod' et ajout à la liste des factorielles
fac.append(1 % mod)  # 0! est 1. On ajoute 1 % mod pour être cohérent dans l'écriture.

# Calcul de l'inverse modulo de 0! (qui est 1) et ajout à la liste des inverses de factorielles
pw.append(1 % mod)   # l'inverse de 1 modulo mod est 1

# Boucle pour pré-calculer toutes les factorielles de 1 à 1000 en appliquant le modulo à chaque étape
for i in range(1, 1001):  # On boucle de 1 inclus à 1000 inclus
    # Calcul de la factorielle de i en multipliant la factorielle précédente par i, avec un modulo pour rester dans les bornes
    fac.append(fac[i-1]*i % mod)  # fac[i] = (fac[i-1] * i) % mod

# Boucle pour pré-calculer l'inverse modulo de chaque factorielle de 1 à 1000
for i in range(1, 1001):  # On commence à 1 car 0 a déjà été traité
    # Pour inverser une factorielle modulo 'mod', on utilise la fonction pow avec l'exposant mod-2
    # pow(fac[i], mod-2, mod) calcule l'inverse de fac[i] modulo mod grâce au théorème de Fermat (mod doit être premier)
    pw.append(pow(fac[i], mod-2, mod))

# Lecture de deux entiers n et k sur une seule ligne, séparés par un espace, puis conversion en int
n, k = [int(s) for s in input().split()]  # Par exemple, si l'utilisateur tape "3 5", n sera 3 et k sera 5

# Test pour vérifier si n est strictement plus grand que k
if n > k:   # Si on demande plus d'éléments qu'il n'y en a, impossible de choisir
    print(0)  # Dans ce cas, il n'y a aucune solution, donc on affiche 0
else:
    # Sinon, on calcule le coefficient k! / (k-n)! modulo mod, qui correspond au nombre d'arrangements de k éléments pris n à n
    # fac[k] est k! modulo mod, pw[k-n] est l'inverse modulaire de (k-n)! modulo mod, donc le produit donne (k! / (k-n)!) % mod
    print(fac[k] * pw[k-n] % mod)  # On affiche le résultat final modulo mod