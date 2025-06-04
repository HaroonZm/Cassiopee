# Importation du module 'sys', qui permet d'accéder à certaines variables utilisées ou maintenues par l'interpréteur Python
import sys
# Affectation à la variable 'read' de la méthode 'read' du buffer d'entrée standard (c'est-à-dire une fonction qui lira tous les octets depuis l'entrée standard)
read = sys.stdin.buffer.read
# Affectation à la variable 'readline' de la méthode 'readline' du buffer d'entrée standard (permet de lire une ligne à la fois comme des octets)
readline = sys.stdin.buffer.readline
# Affectation à la variable 'readlines' de la méthode 'readlines' du buffer d'entrée standard (permet de lire toutes les lignes sous forme de liste d'octets)
readlines = sys.stdin.buffer.readlines

# Import du module numpy (généralement utilisé pour travailler avec des tableaux multidimensionnels et offrir des méthodes mathématiques avancées)
import numpy as np

# Utilisation de 'read' pour lire toutes les données d'entrée sous forme d'octets,
# puis appel de la méthode 'split' pour séparer les données sur les espaces ou nouvelles lignes
# Finalement, 'map' convertit chaque élément en int, le résultat est unpacké dans A et B
A, B = map(int, read().split())

# Définition d'une constante entière MOD contenant la valeur 10^9 + 7 (nombre premier utilisé pour faire des calculs modulo afin d'éviter le débordement d'entier)
MOD = 10 ** 9 + 7

# Définition d'une constante entière U valant 2001 ; c'est une borne supérieure pour les dimensions des tableaux
U = 2001

# Création d'un tableau numpy de taille U x U rempli de zéros, avec type d'entier 64 bits (np.int64)
comb = np.zeros((U, U), np.int64)
# Initialisation de la toute première case du tableau à 1 : comb[0,0] = 1.
# Cela représente que C(0,0) = 1 (c'est-à-dire "0 parmi 0")
comb[0, 0] = 1

# Boucle pour remplir le tableau "comb" (tableau des combinaisons, aussi appelé triangle de Pascal) :
for n in range(1, U):  # Pour n de 1 à U-1 inclus (notez que la borne supérieure n'est pas incluse avec 'range')
    # Ajout (incrémentation) des valeurs au-dessus à gauche dans le triangle de Pascal :
    # comb[n, k] += comb[n-1, k]
    comb[n, 0:n] += comb[n-1, 0:n]
    # Ajout (incrémentation) des valeurs au-dessus à droite dans le triangle de Pascal :
    # comb[n, k+1] += comb[n-1, k]
    comb[n, 1:n+1] += comb[n-1, 0:n]
    # Prise du résultat modulo MOD pour garder les valeurs dans une plage raisonnable et éviter le débordement
    comb[n, :n+1] %= MOD

# Calcul du cumulatif (somme partielle le long de l'axe des colonnes) du tableau 'comb'
# (cumsum(axis=1) renvoie pour chaque ligne la liste des sommes cumulées par colonne)
comb_cum = comb.cumsum(axis=1)

# Création d'un tableau numpy S de taille U x U rempli de zéros de type int64
S = np.zeros((U, U), np.int64)
# Remplit la première ligne de S avec des 1.
# Cela veut dire que si on a 0 "bleu" ou objet à disposition, il n'y a qu'une façon d'avoir n'importe quel nombre de "rouge" ou objets restants
S[0, :] = 1
# On remplit S pour les autres lignes :
# - comb_cum[:-1] est le tableau "comb_cum" de toutes les lignes, sauf la dernière (soit ligne 0 jusqu'à U-2)
# - cumsum(axis=1) fait de nouveau la somme cumulée par ligne
# - Le tout est pris modulo MOD, et on affecte cela aux lignes 1 à U-1 de S
S[1:, :] = comb_cum[:-1].cumsum(axis=1) % MOD

# Initialisation d'une variable x à 0 ; elle va servir à accumuler le résultat final
x = 0
# On parcourt tous les k de 0 à A inclus (donc de 0 à A)
for k in range(A+1):
    # Calcul intermédiaire :
    # - comb[B-1, k] : le nombre de façons de choisir k éléments dans B-1 (C(B-1, k))
    # - S[k, :A-k+1] : sous-tableau contenant les valeurs de S pour l'indice k, colonnes de 0 à A-k inclus.
    #   Cela correspond à toutes les façons d'obtenir un total de A objets, en prenant k objets d'une sorte et le reste de l'autre sorte,
    #   tout en restant dans les bornes du problème.
    #   Le '.sum()' fait la somme de toutes ces valeurs.
    #   Le résultat est pris modulo MOD pour éviter le débordement.
    # Tout est multiplié avec opérateur modulo, puis ajouté à x, lui-même sous modulo MOD ensuite.
    x += comb[B-1, k] * (S[k, :A-k+1].sum() % MOD) % MOD
# On applique le modulo final à x une fois la somme terminée, pour s'assurer que la sortie est bien dans [0, MOD)
x %= MOD

# Affichage du résultat final avec la fonction 'print'.
print(x)