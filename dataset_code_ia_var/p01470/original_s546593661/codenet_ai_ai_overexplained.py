# Définition d'une constante entière nommée 'M' qui stocke la valeur du modulo premier utilisé à travers le programme.
# Cette valeur est utilisée pour assurer que les résultats des calculs restent dans l'intervalle des entiers 64 bits signés.
M = 4294967311

# Définition d'une fonction nommée 'pmod' qui calcule le modulo sécurisé d'un entier 'v' par rapport à 'M'.
# Cette fonction gère aussi bien les valeurs positives que négatives de 'v' afin de toujours retourner un résultat positif compris entre 0 et M-1.
def pmod(v):
    # On calcule (v % M) qui donne le reste de la division entière de v par M.
    # Si 'v' est négatif, le résultat de v % M peut être aussi négatif. Donc on ajoute M pour être sûr d'obtenir une valeur positive.
    # Enfin, on reprend le modulo 'M' une deuxième fois pour ramener d'éventuelles valeurs > M à l'intervalle [0, M-1].
    return (v % M + M) % M

# Définition d'une fonction 'mpow' qui calcule la puissance modulaire.
# Elle élève l'entier 'x' à la puissance entière 'N', le tout sous modulo 'M'.
def mpow(x, N):
    # Initialisation d'une variable 'res' à 1 qui va contenir le résultat de la puissance modulaire.
    res = 1
    # On utilise une boucle 'while' pour répéter tant que l'exposant 'N' est strictement supérieur à 0.
    while N > 0:
        # Si l'exposant 'N' est impair (c'est-à-dire que N modulo 2 vaut 1),
        # cela signifie qu'il reste une puissance de 'x' à multiplier au résultat.
        if (N % 2):
            # On multiplie 'res' par 'x' et on applique pmod pour garder le résultat dans le bon intervalle modulo.
            res = pmod(res * x)
        # On élève 'x' au carré et l'on prend le reste modulo 'M' pour ne pas dépasser la taille des entiers autorisée.
        x = pmod(x * x)
        # On divise 'N' par 2 (division entière grâce à l'opérateur //), ce qui revient à faire un décalage de bit à droite.
        # Ainsi la boucle traite chaque bit de N pour le calcul binaire exponentiel rapide.
        N = N // 2
    # Après la boucle, on retourne la valeur calculée.
    return res

# Définition d'une fonction 'minv' qui calcule l'inverse modulaire d'un nombre entier 'a' modulo 'M'.
# Cela correspond à un nombre x tel que (a * x) % M == 1.
def minv(a):
    # On utilise la propriété de l'arithmétique modulaire (petit théorème de Fermat) pour un nombre premier M :
    # l'inverse de 'a' modulo 'M' est égal à a^(M-2) modulo M.
    return mpow(a, M - 2)

# Lecture d'un entier N depuis l'entrée standard qui indique combien d'opérations seront à traiter.
N = input()
# Initialisation de la variable 'v' à 0 ; cette variable va accumuler la valeur à modifier.
v = 0
# On utilise une boucle 'for' pour itérer 'i' de 0 jusqu'à N-1 inclus.
for i in range(N):
    # Lecture d'une ligne depuis l'entrée standard, découpage en deux entiers par la fonction 'map' et 'raw_input'.
    c, y = map(int, raw_input().split())
    # Si 'c' vaut 1, on effectue une addition modulaire entre 'v' et 'y'.
    if c == 1:
        v = pmod(v + y)
    # Si 'c' vaut 2, on effectue une soustraction modulaire entre 'v' et 'y'.
    if c == 2:
        v = pmod(v - y)
    # Si 'c' vaut 3, on effectue une multiplication modulaire entre 'v' et 'y'.
    if c == 3:
        v = pmod(v * y)
    # Si 'c' vaut 4, on effectue une division modulaire entre 'v' et 'y', c'est-à-dire multiplication par l'inverse modulo.
    if c == 4:
        v = pmod(v * minv(y))

# Après traitement de toutes les opérations, on veut afficher la valeur naturelle signée de 'v'.
# Si 'v' est inférieur à (1<<31), c'est-à-dire la limite supérieure d'un entier 32 bits signé, on garde 'v' inchangé.
if v < (1 << 31):
    v = v
# Sinon, on soustrait 'M' à 'v' pour obtenir la valeur négative correcte sur 32 bits.
else:
    v = v - M

# Affichage final de la valeur entière 'v' formatée en décimal.
print "%d" % v