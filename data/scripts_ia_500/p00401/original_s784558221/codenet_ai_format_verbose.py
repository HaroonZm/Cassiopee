nombre_entree = int(input())

longueur_binaire_nombre = len(bin(nombre_entree)) - 1

position_premier_un = bin(nombre_entree).find("1")

exposant_puissance = longueur_binaire_nombre - position_premier_un

resultat = 2 ** exposant_puissance

print(resultat)