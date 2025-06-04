from collections import Counter

N = int(input())
S = input()

# Compter la fréquence de chaque chiffre dans S
freq = Counter(S)

# Les chiffres de 1 à 9 sous forme de liste de chaînes
digits = [str(i) for i in range(1, 10)]

# Trier les digits par fréquence décroissante, 
# en cas d'égalité par ordre naturel croissant (pour la stabilité)
# On veut les chiffres les plus fréquents en positions "centrales"
freq_sorted = sorted(digits, key=lambda x: (-freq[x], x))

# Positions du clavier 3x3 indexées (0 à 8)
# On va organiser les positions par leur "centralité" sur le clavier
# Positions: indices
# 0 1 2
# 3 4 5
# 6 7 8
# On considère la position centrale 4 plus centrale que les bords, puis les centres de bord (1,3,5,7), puis les coins (0,2,6,8)
positions_order = [4,1,3,5,7,0,2,6,8]

# On crée un tableau vide
layout = [None]*9

# On place les chiffres dans l'ordre des positions
for pos, d in zip(positions_order, freq_sorted):
    layout[pos] = d

# Pour les positions restantes qui n'ont pas de chiffre (si jamais), on remplit avec les chiffres restants en ordre naturel
remaining_digits = [d for d in digits if d not in layout]
for i in range(9):
    if layout[i] is None:
        layout[i] = remaining_digits.pop(0)

# On vérifie maintenant la contrainte de lex minimal en cas d'égalité possible:
# Comme on a trié freq_sorted par fréquence décroissante puis par ordre naturel, 
# et placé selon centralité, 
# il se peut que plusieurs configurations aient même coût, mais on a choisi lex minimal en triant correctement.

# On formate la sortie
print("".join(layout[0:3]))
print("".join(layout[3:6]))
print("".join(layout[6:9]))