# Lecture de trois entiers séparés par des espaces à partir de l'entrée standard (input). 
# La fonction input() lit la ligne saisie par l'utilisateur, 
# puis split() la divise en une liste de chaînes numériques, 
# map(int, ...) convertit chaque chaîne en entier
# Enfin, l'affectation multiple permet de stocker les trois valeurs dans N, A et B respectivement.
N, A, B = map(int, input().split())

# Définition du module utilisé dans les calculs pour éviter les débordements arithmétiques sur les grands entiers
M = 998244353

# Calcul de P qui représente N+1 ; utilisé dans la taille des tableaux pour la factorielle
P = N + 1

# Initialisation de la variable f à 1. Elle stockera les valeurs intermédiaires de la factorielle lors du calcul
f = 1

# Création de la liste F pour stocker les factorielles de 0 à N, initialisée avec des 1.
F = [1] * P

# Création de la liste I qui servira à stocker les inverses modulo M des factorielles,
# également initialisée avec des 1
I = [1] * P

# z sera la variable qui stockera le résultat final calculé dans la boucle principale
z = 0

# Préparation d'un objet range pour désigner les plages de boucles (pour la lisibilité ensuite)
R = range

# Première boucle : calcul des factorielles modulo M pour tous les entiers de 1 à N inclus
for n in R(1, P):  # Commence à 1 et va jusqu'à N inclus (car range s'arrête avant P)
    # f prend la valeur de la factorielle de n, mais en utilisant les valeurs précédentes
    # Multiplication de la valeur précédente par n, puis réduction modulo M
    f = f * n % M
    # On stocke la factorielle de n dans F[n]
    F[n] = f

# Calcul de l'inverse modulo M de la factorielle de N
# pow(f, M-2, M) utilise le petit théorème de Fermat pour obtenir l'inverse de f modulo M
I[N] = i = pow(f, M - 2, M)

# Deuxième boucle : calcul des inverses modulo M de toutes les factorielles (de N à 1)
for n in R(N, 1, -1):  # Commence à N, finit à 2 inclus (car range s'arrête avant le deuxième argument)
    # Mise à jour de i : multiplication par n, puis modulo M, donne l'inverse de la factorielle de n-1  
    i = i * n % M
    # Stockage du résultat dans I[n-1]
    I[n - 1] = i

# Troisième boucle principale pour le calcul de la somme finale
# min(A+1, N-B) calcule la borne supérieure de la boucle selon la logique de l'algorithme,
# mais si N-B-A == 0 (équivalent à N-B-A étant faux), alors la plage sera simplement A+1
for k in R(min(A + 1, N - B) if N - B - A else A + 1):
    # Q est une variable intermédiaire qui dépend de N, B et k, utilisée dans les calculs de combinaisons
    Q = N - B - k - 1

    # Calcul du terme qui sera ajouté à z pour chaque valeur de k
    # On démontre les opérations individuellement :
    # (B-k) : facteur linéaire dépendant de k
    # F[B+k-1] : factorielle de (B+k-1)
    # I[B] : inverse de la factorielle de B
    # I[k] : inverse de la factorielle de k
    # F[Q+A-k] : factorielle de (Q+A-k)
    # I[Q] : inverse de la factorielle de Q
    # I[A-k] : inverse de la factorielle de (A-k)
    term = (
        (B - k)                      # facteur linéaire
        * F[B + k - 1]               # factorielle de (B+k-1)
        * I[B]                       # inverse factorielle de B
        * I[k]                       # inverse factorielle de k
        * F[Q + A - k]               # factorielle de (Q+A-k)
        * I[Q]                       # inverse factorielle de Q
        * I[A - k]                   # inverse factorielle de (A-k)
    )
    # Ajout du terme au résultat z, en gardant z modulo M
    z = (z + term) % M

# Condition particulière : si B vaut 0, alors le résultat est 1 quelle que soit la valeur de z
# sinon on affiche la valeur calculée dans z
print(z if B else 1)