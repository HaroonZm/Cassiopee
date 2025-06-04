# Demander à l'utilisateur de saisir un entier, puis convertir la saisie (qui est une chaîne de caractères) en entier avec int()
n = int(input())

# Pour raccourcir les appels ultérieurs, on nomme print par 'p', et range par 'r'
p, r = print, range

# Vérifier si n est une puissance de deux.
# n & -n isole le bit de poids le plus faible à 1 dans n.
# Si n est une puissance de deux, n & -n == n.
if n & -n == n:
    # Si n est une puissance de deux, il faut afficher "No", puis arrêter immédiatement le programme.
    p("No")
    exit(0)  # Quitte le programme avec le code de sortie 0 (succès)

# Si on arrive ici, alors n n'est pas une puissance de deux
p("Yes")  # Afficher "Yes" car la condition est satisfaite.

# Cas particuliers : si n vaut exactement 3
if n == 3:
    # On affiche des paires de nombres.
    # Chaque appel p(a, b) affiche les deux entiers sur une ligne séparés par un espace.
    p(1, 2)
    p(2, 3)
    p(3, 4)
    p(4, 5)
    p(5, 6)
    exit(0)  # On termine le programme car ce cas est traité à part.

# Initialiser k à 1.
k = 1
# Doubler k tant que k*2 < n, pour obtenir la plus grande puissance de deux STRICTEMENT inférieure à n.
while k * 2 < n:
    k *= 2  # Multiplie k par 2 à chaque itération.

# Première boucle : pour i allant de 0 à k-3 inclus (donc k-2 éléments au total).
for i in r(k - 2):
    # Afficher deux entiers consécutifs i+1 et i+2 (parce que range commence à 0, donc on ajoute 1)
    p(i + 1, i + 2)

# Connecter le sommet k-1 (c'est-à-dire le (k-1)-ième sommet, vu qu'on part de 1) au sommet n+1
# Cela fait un lien spécial entre une puissance de deux et un nombre décalé
p(k - 1, n + 1)

# Deuxième boucle : pour i de 0 à k-3 inclus (toujours k-2 éléments)
for i in r(k - 2):
    # On ajoute n au numéro de sommet pour obtenir une nouvelle série de sommets.
    # On connecte chaque (n+i+1) à (n+i+2)
    p(n + i + 1, n + i + 2)

# On connecte le sommet n+k à n+1
p(n + k, n + 1)
# On connecte le sommet n+k+1 à k
p(n + k + 1, k)

# Dernière boucle : pour i de 0 à n-k-1 inclus (donc n-k éléments au total)
for i in r(n - k):
    # On relie (n+i+1) à (n+k+i+1)
    p(n + i + 1, n + k + i + 1)
    # On relie (n+k+i) à (k+i+1)
    p(n + k + i, k + i + 1)