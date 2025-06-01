n = int(input())
binaire = bin(n)
longueur = len(binaire)
position_1 = binaire.find("1")
exposant = longueur - 1 - position_1
resultat = 2 ** exposant
print(resultat)