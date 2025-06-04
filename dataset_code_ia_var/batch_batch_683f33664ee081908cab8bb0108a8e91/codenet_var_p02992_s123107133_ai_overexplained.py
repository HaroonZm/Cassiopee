# Définition d'une constante mod représentant un grand nombre premier, utilisé pour prendre les résultats "modulo" cette valeur afin d'éviter le dépassement d'entier.
mod = 1000000007

# Lecture de deux entiers depuis l'entrée standard séparés par un espace, assignés à n et k respectivement.
# 'map' applique int à chaque élément produit par 'input().split()', convertissant les chaînes en entiers.
n, k = map(int, input().split())

# Calcul de la racine carrée entière de n, puis conversion explicite en entier pour s'assurer que la variable s est de type int.
s = int(n ** 0.5)

# Création d'une liste 'Num' remplie de zéros, de longueur s+1. Cette liste va stocker certains valeurs intermédiaires.
Num = [0] * (s + 1)

# Boucle for allant de 's' jusqu'à 1 (inclus), en décrémentant de 1 à chaque itération (marche arrière).
for i in range(s, 0, -1):
    # L'élément à l'indice 'i' de la liste 'Num' est assigné à la valeur 'i' lui-même.
    Num[i] = i
    # Ajoute à la fin de la liste Num la valeur entière de n divisé par i (division entière)
    Num.append(n // i)

# La variable 'l' reçoit la longueur actuelle de la liste 'Num', qui est maintenant plus grande que s+1.
l = len(Num)

# Boucle for qui commence à l'indice 1 jusqu'à l-1 inclus (car range s'arrête avant l).
for i in range(1, l):
    # L'élément de Num en partant de la fin (-i) est diminué par la valeur précédente Num[-i-1].
    # Cela met à jour Num pour représenter la différence cumulée entre les éléments successifs.
    Num[-i] = Num[-i] - Num[-i - 1]

# Création d'une nouvelle liste 'DP' (tableau dynamique), une liste à deux dimensions de taille k * l, initialisée à zéro.
# Chaque élément de 'DP' est une sous-liste contenant 'l' zéros.
DP = [[0] * l for _ in range(k)]

# Affectation de la première ligne de 'DP' à être une copie de Num. Cette opération se fait pour ne pas lier DP[0] et Num.
DP[0] = Num[:]

# Boucle principale dynamique pour remplir tout DP sauf la première ligne.
for i in range(1, k):
    # Initialisation d'une variable temporaire à zéro, qui servira à stocker des accumulations partielles.
    tmp = 0
    # Parcours les indices de 1 à l-1 inclus. Notez que DP et Num utilisent l comme taille.
    for j in range(1, l):
        # Ajoute à tmp la valeur de DP à l'étape précédente (i-1) pour le même indice j.
        tmp += DP[i - 1][j]
        # Fait un modulo mod pour rester dans la plage des entiers acceptables.
        tmp %= mod
        # Met à jour la valeur de DP à la ligne courante (i) et à l'indice '-j' (partant de la fin de la liste) 
        # Multipliant tmp par Num[-j], avec une réduction modulo mod.
        DP[i][-j] = (tmp * Num[-j]) % mod

# Initialisation de la variable de résultat final à zéro.
ans = 0

# Parcourt les éléments de la dernière ligne du tableau DP (DP[-1]), sauf le premier élément ([1:])
for i in DP[-1][1:]:
    # Ajoute chaque élément à la variable de résultat ans.
    ans += i
    # Prend le résultat modulo mod pour éviter le dépassement.
    ans %= mod

# Affiche la réponse finale, qui est le résultat du calcul.
print(ans)