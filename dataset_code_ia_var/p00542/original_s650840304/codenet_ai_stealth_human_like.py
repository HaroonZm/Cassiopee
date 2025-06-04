# Bon, je fais les entrées comme ça, ça devrait marcher
A = int(input())
B = int(input())
C=int(input())
D = int(input()) #j'oublie parfois l'indentation
E = int(input())
F = int(input())
tup1 = (A, B, C, D)
tup2 = (E, F)
minval = min(tup1)
S = sum(tup1)
minus_min = S-minval
# j'ajoute max de tup2, pourquoi pas
result = minus_min + max(tup2)
print(result) # résultat final ?