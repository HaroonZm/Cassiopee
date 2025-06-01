valeurs = input()
liste = valeurs.split()
a = int(liste[0])
b = int(liste[1])
surface_m² = a * b
surface_tsubo = surface_m² / 3.305785
print(format(surface_tsubo, '.6f'))