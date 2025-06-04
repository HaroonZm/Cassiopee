# Importation du module sys qui fournit des fonctions et objets liés à l’interpréteur Python.
import sys
# On redéfinit la fonction input() pour qu'elle lise directement depuis l'entrée standard (par ligne), 
# ce qui est utile pour lire des données d'entrée plus rapidement, surtout si cette entrée est importante.
input = sys.stdin.readline

# On importe 'deque' depuis 'collections', un type de liste optimisé pour faire des ajouts/suppressions rapides des deux côtés.
from collections import deque

# Lecture des deux entiers h et w sur une seule ligne, séparés par un espace.
# 'map(int, ...)' convertit chaque morceau de la ligne d'entrée en entier.
h, w = map(int, input().split())

# Initialisation d'une liste vide 's' pour stocker les chaînes de caractères qui représentent la grille.
s = []
# Boucle pour lire chaque ligne de la grille.
for i in range(h):
    # On lit chaque ligne, on retire le retour à la ligne final grâce à 'rstrip()', et on stocke dans 'q'.
    q = input().rstrip()
    # On ajoute cette chaîne à la liste 's' représentant la grille.
    s.append(q)

# Création d'une matrice 'chk' de dimensions (h-1) x (w-1) initialisée à zéro, où chaque élément sera utilisé pour représenter 
# une caractéristique spécifique selon les motifs des cases du quadrillage.
chk = [[0] * (w - 1) for i in range(h - 1)]

# Double boucle pour calculer les valeurs de 'chk' selon un motif particulier pour chaque petit carré 2x2 du quadrillage.
# Parcourt chaque colonne (sauf la dernière).
for i in range(w - 1):
    # Parcourt chaque ligne (sauf la dernière).
    for j in range(h - 1):
        # Pour chaque carré 2x2, on va déterminer si la parité du nombre de '#' dans les 4 coins de ce carré est paire (-> True)
        # ou impaire (-> False), via un XOR (^) logique.
        # La conversion en int'(True/False)' donne 1 si la case contient un '#', 0 sinon.
        # Puis on fait '1 - valeur' pour inverser le résultat final, stocké dans chk[j][i].
        chk[j][i] = 1 - int((s[j][i] == '#') ^ (s[j + 1][i] == '#') ^ (s[j][i + 1] == '#') ^ (s[j + 1][i + 1] == '#'))

# Définition d'une fonction f(a) qui prend en argument une liste 'a'.
# Cette fonction va analyser un "histogramme" et retourner la plus grande aire possible d'un rectangle 
# (ici adapté aux besoins du problème, dépendant de 'a').
def f(a):
    # On ajoute un '0' à la fin du tableau pour forcer la vidange de la pile à la fin de la boucle.
    a += [0]
    # On initialise une pile, ici avec la structure 'deque' qui est plus performante pour l’ajout/suppression sur les deux extrémités.
    stack = deque()
    # Variable 'ans' pour stocker la plus grande aire trouvée, initialisée à -1 (valeur minimale impossible).
    ans = -1
    # On parcourt chaque colonne, de 0 à w-1 (w éléments car a a un élément supplémentaire ajouté).
    for i in range(w):
        # Si la pile est vide, il n'y a aucune barre dans l'histogramme en cours de traitement, on ajoute l'élément courant.
        if stack == deque():
            # On ajoute un tuple (hauteur, position) à la pile.
            stack.append((a[i], i))
        # Si la hauteur en haut de la pile est inférieure à la hauteur actuelle, on étend le rectangle et on empile.
        elif stack[-1][0] < a[i]:
            stack.append((a[i], i))
        # Si la hauteur en haut de la pile est supérieure à la hauteur actuelle, on doit traiter les barres plus hautes.
        elif stack[-1][0] > a[i]:
            # On retire les barres dont la hauteur est strictement supérieure à a[i].
            while stack and stack[-1][0] >= a[i]:
                # On dépile la barre, récupérant sa hauteur (x) et sa position initiale (y).
                x, y = stack.pop()
                # On calcule l'aire du rectangle possible à cet emplacement, et on garde le maximum rencontré.
                ans = max((x + 1) * (i - y + 1), ans)
            # Après avoir vidé les barres trop hautes, on empile la nouvelle barre avec sa hauteur actuelle et la dernière position valide 'y'.
            stack.append((a[i], y))
    # On retourne la plus grande aire trouvée dans cet "histogramme".
    return ans

# On va remplir une table dynamique 'dp' de même dimension que 'chk' pour utiliser la technique du plus grand rectangle.
dp = [[0] * (w - 1) for i in range(h - 1)]
# On recopie la première ligne de 'chk' dans 'dp', c'est l'initialisation de la programmation dynamique.
for i in range(w - 1):
    dp[0][i] = chk[0][i]

# Remplissage du tableau "dp" par programmation dynamique.
# En partant de la deuxième ligne, on vérifie si la case est "valide" (valeur 1 dans 'chk').
for i in range(1, h - 1):
    for j in range(w - 1):
        # Si 'chk[i][j]' vaut 1, alors on empile la hauteur de toutes les lignes consécutives de 1 obtenues
        # en prenant la valeur au-dessus + 1 (c'est-à-dire l'accumulation verticale de cases valides).
        if chk[i][j]:
            dp[i][j] = dp[i - 1][j] + 1

# Initialisation de la variable 'ans' avec la plus grande des deux dimensions de la grille, 
# c'est une valeur de départ pour la réponse (minimum possible dans ce problème).
ans = max(h, w)
# Pour chaque ligne du tableau 'dp', on calcule la plus grande aire possible à cet endroit en utilisant la fonction 'f'.
for i in range(h - 1):
    ans = max(ans, f(dp[i]))

# On affiche la plus grande aire trouvée, qui est la réponse finale du problème.
print(ans)