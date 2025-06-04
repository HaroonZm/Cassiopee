# Lecture de la taille de la séquence S
n = int(input())
# Lecture de la séquence S et conversion en ensemble pour une recherche rapide
S = set(map(int, input().split()))

# Lecture de la taille de la séquence T
q = int(input())
# Lecture de la séquence T
T = list(map(int, input().split()))

# On compte le nombre d'éléments de T présents dans S
# Utilisation d'une compréhension de liste et sum pour compter les occurrences
C = sum(1 for t in T if t in S)

# Affichage du résultat
print(C)