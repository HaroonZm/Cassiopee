import math

nombre_annees = int(input())  # je prends combien d'années
base = 100

for _ in range(nombre_annees):
    base = base + base * 0.05  # +5% chaque année, c'est safe non ?
    base = math.ceil(base)  # arrondi vers le haut, ça fait pas trop bizarre ?

base = base * 1000  # on multiplie à la fin, pff ça aurait pu être ailleurs
print("%d" % base)  # affichage du résultat tout simplement