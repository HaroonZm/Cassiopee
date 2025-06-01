# AOJ 0626 Collecting Stamps 2
# Python3 2018.7.2 bal4u

# Importation du module sys qui permet d'accéder à des variables et fonctions liées au système d'exploitation.
import sys
# Importation spécifique de la fonction stdin.readline depuis le module sys pour améliorer la vitesse de lecture des entrées.
from sys import stdin
# Redéfinition de la fonction input pour utiliser stdin.readline, plus rapide que la fonction input standard.
input = stdin.readline

# Lecture d'une ligne d'entrée contenant un entier n, transformation de cette chaîne en un entier avec int().
n = int(input())

# Initialisation de deux listes si et sj toutes deux de longueur n+1, remplies de zéros.
# Ces listes serviront à stocker des sommes cumulées (préfixes) de la fréquence des lettres 'I' et 'J' respectivement.
si, sj = [0]*(n+1), [0]*(n+1)

# Lecture d'une chaîne de caractères s (string) représentant la séquence des timbres,
# utilisation de strip pour enlever les caractères de fin de ligne et espaces inutiles.
s = input().strip()

# Boucle for parcourant chaque index i de 0 à n-1 (toutes les positions dans la chaîne s).
for i in range(n):
    # sj[i+1] devient la somme cumulative des 'J' jusqu'à la position i incluse.
    # On ajoute 1 si le caractère actuel s[i] est égal à 'J', sinon 0.
    sj[i+1] = sj[i] + (s[i] == 'J')
    # si[i+1] devient la somme cumulative des 'I' jusqu'à la position i incluse.
    # On ajoute 1 si le caractère actuel s[i] est égal à 'I', sinon 0.
    si[i+1] = si[i] + (s[i] == 'I')

# Initialisation des variables ans, a, b, c à 0.
# Ces variables serviront à accumuler différents résultats intermédiaires nécessaires pour le calcul final.
ans = a = b = c = 0

# Boucle de 1 à n-1 (indices correspondant aux positions possibles pour diviser la séquence).
for i in range(1, n):
    # a prend la valeur maximale entre sa valeur actuelle et le produit de sj[i] par (si[n] - si[i]).
    # sj[i] est le nombre de 'J' jusqu'à la position i (exclus),
    # si[n] - si[i] est le nombre de 'I' à partir de la position i jusqu'à la fin.
    # Cette expression cherche à maximiser la multiplication entre les nombres de 'J' et 'I' dans deux sous-intervalles.
    a = max(a, sj[i] * (si[n]-si[i]))

# Boucle parcourant tous les indices de la séquence s.
for i in range(n):
    # Condition vérifiant si le caractère à la position i est 'O'.
    if s[i] == 'O':
        # b accumule le nombre d'apparitions de 'I' après la position i (exclue),
        # calculé comme si[n] - si[i+1] où si[i+1] est la somme cumulative jusqu'à i incluse.
        b += si[n] - si[i+1]
        # c accumule le nombre d'apparitions de 'J' avant la position i (exclue),
        # calculé simplement comme sj[i], somme cumulative jusqu'à i exclu.
        c += sj[i]
        # ans est incrémenté par le produit du nombre d'I après i par le nombre de J avant i,
        # soit (si[n] - si[i+1]) * sj[i].
        ans += (si[n] - si[i+1]) * sj[i]

# Affichage du résultat final qui comprend:
# ans (cumul des produits pour les positions 'O'),
# ajouté au maximum parmi a, b, c qui représentent différentes configurations optimales.
print(ans + max(a, b, c))