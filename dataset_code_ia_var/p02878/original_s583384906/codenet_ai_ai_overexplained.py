# Lire trois entiers N, A et B à partir de l'entrée standard (saisie utilisateur).
# La fonction input() lit une ligne saisie sur le terminal.
# La méthode split() découpe la chaîne en utilisant l'espace comme séparateur, créant une liste de chaînes.
# La fonction map() applique int à chaque élément de la liste pour les convertir de chaînes en entiers.
N, A, B = map(int, input().split())

# Définir une constante M égale à 998244353.
# Ici, M est un nombre premier qui est souvent utilisé comme mod pour les calculs modulo dans la programmation compétitive.
M = 998244353

# P représente N+1. Cela sert pour dimensionner les tableaux plus loin.
P = N + 1

# Initialiser une variable f à 1.
# Elle servira à stocker les valeurs intermédiaires lors du calcul des factorielles.
f = 1

# Créer une liste F de taille P, avec chaque élément initialisé à 1.
# F sera utilisée pour stocker les valeurs des factorielles modulo M, tel que F[n] == n! % M.
F = [1] * P

# Créer une liste I de taille P, initialisée à 1.
# I sera utilisée pour stocker les inverses multiplicatifs des factorielles modulo M.
I = [1] * P

# Initialiser une variable z à 0.
# Cette variable accumulera le résultat final du calcul de la somme.
z = 0

# Définir R comme un alias local pour la fonction range().
# Cela permet d'écrire R(...) au lieu de range(...), ce qui aide à raccourcir le code.
R = range

# Vérifier si B est égal à 0.
if B == 0:
    # Si B == 0, alors on affiche 1 directement et on quitte le programme.
    # (Cela correspond à un cas particulier de l'énoncé.)
    print(1)
    exit()

# Boucle pour calculer les factorielles de 1 à N.
# Pour chaque entier n de 1 à N inclus (range(1, P) va de 1 à N inclus car P = N+1),
# nous actualisons f = f * n modulo M, et nous stockons la valeur courante dans F[n].
for n in R(1, P):
    # Calcul de la factorielle n! modulo M.
    f = f * n % M
    # Stockage du résultat dans la liste F à la position n.
    F[n] = f

# Calcul de l'inverse modulaire de N! modulo M à l'aide de la fonction pow().
# pow(f, M-2, M) utilise le petit théorème de Fermat pour obtenir l'inverse modulo d'un nombre premier.
I[N] = i = pow(f, M - 2, M)

# Boucle pour calculer l'inverse modulaire de toutes les autres factorielles, de N-1 à 0.
# Commencer de N à 1 exclus (donc on couvre N à 1 inclusivement).
for n in R(N, 1, -1):
    # i est multiplié par n puis réduit modulo M.
    i = i * n % M
    # On stocke la valeur d'inverse dans I[n-1].
    I[n - 1] = i

# Cette boucle principale calcule la somme désirée selon la formule donnée.
# Le nombre d'itérations dépend d'une condition basée sur les valeurs de N, B, et A.
if N - B - A:
    # Si N - B - A est non nul, alors range s'arrête à min(A+1, N-B).
    loop_range = min(A + 1, N - B)
else:
    # Sinon, la boucle va jusqu'à A + 1 (exclu).
    loop_range = A + 1

# Boucle sur l'ensemble des valeurs de k allant de 0 à loop_range-1 inclus.
for k in R(loop_range):
    # Q est défini comme N - B - k - 1.
    Q = N - B - k - 1
    # Calcul du terme de la somme qui sera ajouté à z, appliqué modulo M.
    # La formule comporte plusieurs arrangements de combinaisons binomiales,
    # réalisés à l'aide des factorielles et des inverses calculés précédemment.
    # Pour chaque valeur de k dans la plage définie :
    # - (B-k) est multiplié par la combinaison d'autres termes (voir la formule originale).
    # - Toutes les multiplications et divisions sont effectuées sous modulo M.
    # - Les divisions sont remplacées par des multiplications par des inverses modulo M.
    term = (B - k) * F[B + k - 1] * I[B] * I[k] * F[Q + A - k] * I[Q] * I[A - k]
    # Ajouter le terme à z et le réduire modulo M pour éviter le dépassement.
    z = (z + term) % M

# Afficher le résultat final de la somme calculée.
print(z)