# Lecture d'un entier depuis l'entrée standard (clavier).
# La fonction input() permet de récupérer une ligne saisie par l'utilisateur, 
# mais elle renvoie une chaîne de caractères. La fonction int() convertit cette 
# chaîne en un entier.
s = int(input())

# Définition d'une fonction pour calculer les combinaisons modulo un entier donné.
# Les combinaisons (nCr) indiquent le nombre de façons de choisir r objets parmi n
# sans tenir compte de l'ordre. La formule générale est : n! / (r! * (n-r)!)
def cmb(n, r, mod):
    # Si r est hors des bornes logiques (plus petit que 0 ou plus grand que n), 
    # il n'y a aucune combinaison possible donc on retourne 0.
    if ( r<0 or r>n ):
        return 0
    # À cause de la propriété de symétrie des combinaisons (nCr == nC(n-r)), 
    # on choisit le plus petit entre r et n-r pour optimiser le calcul.
    r = min(r, n-r)
    # Le calcul des combinaisons est effectué en multipliant le pré-calcul du
    # factoriel de n (g1[n]) avec l'inverse modulaire des factoriels de r et n-r 
    # (g2[r] et g2[n-r]). Le tout est pris modulo 'mod' pour éviter les débordements.
    return g1[n] * g2[r] * g2[n-r] % mod

# Déclaration de la constante 'mod' qui représente le modulo à appliquer.
# 10**9 + 7 est un grand nombre premier fréquemment utilisé pour éviter 
# les débordements et pour les propriétés algébriques dans la programmation compétitive.
mod = 10**9+7

# Déclaration de N qui représente la borne supérieure utilisée pour les pré-calculs.
# On va pré-calculer les factoriels et leurs inverses jusqu'à N inclus.
N = 3000

# Initialisation de la liste des factoriels.
# g1[k] représentera le factoriel de k modulo mod, c'est-à-dire (k!) % mod.
# On commence avec 0! = 1 et 1! = 1.
g1 = [1, 1]

# Initialisation de la liste des inverses modulaire des factoriels.
# g2[k] représentera l'inverse modulaire de (k!) modulo mod.
# On commence avec 0!^-1 = 1 et 1!^-1 = 1.
g2 = [1, 1]

# Initialisation de la liste des inverses modulaires de chaque nombre jusqu'à N.
# inverse[k] donnera l'inverse modulaire de k modulo mod.
# On commence par inverse[0] (inutile ici) et inverse[1] = 1.
inverse = [0, 1]

# Boucle pour pré-calculer toutes les valeurs jusqu'à N inclus.
for i in range( 2, N + 1 ):
    # Calcul du factoriel de i modulo mod. On multiplie le factoriel précédent g1[-1]
    # par i puis on prend le résultat modulo mod pour le stocker dans g1.
    g1.append( ( g1[-1] * i ) % mod )
    # Calcul de l'inverse modulaire de i modulo mod en utilisant la formule
    # basée sur le petit théorème de Fermat et les propriétés des inverses.
    # Cette méthode dynamique évite de recalculer les inverses à chaque fois.
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    # Calcul de l'inverse modulaire du factoriel courant. On multiplie 
    # l'inverse précédent du factoriel par l'inverse modulaire de i, 
    # puis on prend le tout modulo mod.
    g2.append( (g2[-1] * inverse[-1]) % mod )

# Initialisation de la variable qui contiendra la réponse finale.
ans = 0

# Boucle pour déterminer le nombre total de solutions.
# i commence à 1 et s'arrête avant 2000 (i.e., pour i=1 jusqu'à i=1999 inclus).
for i in range(1, 2000):
    # Vérification si s - 3*i est négatif.
    # Si c'est le cas, il n'est plus possible d'avoir une partition donc
    # on quitte la boucle car les valeurs suivantes n'auront pas de sens non plus.
    if s-3*i < 0:
        break

    # Calcul du nombre de façons de répartir s-3*i objets dans i groupes,
    # en ajoutant i-1 séparateurs (c'est le principe des combinaisons avec répétition).
    # Plus précisément, cela calcule la combinaison ((s-3*i)+(i-1), i-1).
    # On utilise la fonction cmb définie plus tôt, avec les pré-calculs pour 
    # obtenir le résultat rapidement modulo mod.
    ans += cmb(s-3*i+i-1, i-1, mod)
    # On prend le résultat modulo mod à chaque itération pour éviter les débordements
    # et rester dans la limite attendue.
    ans %= mod

# Affichage du résultat final.
# La fonction print() affiche la valeur de ans calculée ci-dessus.
print(ans)