from numpy import *  # Importe toutes les fonctions et classes du module numpy

# On lit deux entiers depuis l'entrée standard, séparés par un espace, et on les assigne respectivement à A et B.
# 'input()' attend une ligne entrée par l'utilisateur.
# 'split()' divise cette ligne en morceaux (chaque morceau séparé par un espace)
# 'map(int, ...)' applique la conversion en entier à chaque morceau.
A, B = map(int, input().split())

# On définit une constante M qui vaut 10^9 + 7. C'est un nombre premier couramment utilisé pour ramener de gros résultats
# dans des bornes raisonnables grâce au modulo, afin d'éviter les débordements.
M = 10 ** 9 + 7

# On définit la valeur de U. Elle servira à créer les matrices carrées qui stockent les coefficients et les sommes.
U = 2001

# On crée un tableau numpy de taille (U x U), rempli de zéros et devant contenir des entiers 64-bits (pour éviter le débordement intermédiaire).
# Ce tableau représentera probablement les coefficients combinatoires binomiaux (ou un objet similaire)
C = zeros((U, U), int64)

# On initialise la première valeur de notre tableau à 1. C'est la condition de base, probablement C[0,0] = 1
C[0, 0] = 1

# Cette boucle va de 1 à U-1 (inclus). Elle va servir à remplir notre tableau combinatoire C selon une certaine règle de récurrence.
for n in range(1, U):
    # On ajoute à chaque case C[n, 1:] (toutes les colonnes sauf la première) la valeur de la case à gauche sur la ligne précédente.
    # Ainsi, C[n, k] += C[n-1, k-1] pour tous les k >= 1
    C[n, 1:] += C[n-1, :-1]
    
    # On ajoute à chaque case C[n, :-1] (toutes les colonnes sauf la dernière) la valeur de la même case sur la ligne précédente.
    # Ainsi, C[n, k] += C[n-1, k] pour tous les k < U-1
    C[n, :-1] += C[n-1, :-1]
    
    # On prend le reste de la division de tous les éléments par M pour rester dans les bornes.
    C[n] %= M

# On crée un second tableau S, de la même forme et du même type que C, rempli de zéros.
# Ce tableau servira à stocker des sommes cumulées de coefficients.
S = zeros_like(C)

# On écrit un 1 dans la première ligne du tableau S, car la somme partielle des coefficients au rang 0 est 1.
S[0] = 1

# Pour chaque ligne de S à partir de la ligne 1,
# on calcule la somme cumulée des coefficients de la ligne précédente sur l'axe horizontal (axis=1), puis on prend la somme cumulée à nouveau,
# le tout modulo M.
# Cela crée une table où chaque S[n, k] stocke des sommes partielles imbriquées de coefficients combinatoires modulaires.
S[1:] = (C[:-1].cumsum(axis=1) % M).cumsum(axis=1) % M

# On va calculer une somme finale selon une certaine formule :
# Il s'agit de la somme, pour chaque k entre 0 et A inclus, de :
#   C[B-1, k] * (somme des S[k, j] pour j allant de 0 à A-k inclus) (modulo M)
# Le tout, résultat final, est ramené modulo M.
# La compréhension de la somme interne et externe permet de combiner toutes les valeurs nécessaires selon la logique combinatoire du problème.
print(
    sum(
        # Pour chaque k allant de 0 à A inclus :
        C[B-1, k] *                          # On prend le coefficient C[B-1, k]
        (
            sum(S[k, :A-k+1]) % M            # On additionne tous les S[k, j] pour j de 0 à A-k inclus, puis modulo M
        ) % M                               # On applique à ce produit un modulo M
        for k in range(A + 1)                 # Pour tous les entiers k de 0 à A inclus
    ) % M                                    # Et on fait la somme de tout cela, puis modulo M pour obtenir la réponse finale
)