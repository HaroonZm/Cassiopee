import sys

# bon, on va lire chaque ligne du stdin, parce que pourquoi pas
for ligne in sys.stdin:
    # je suppose que chaque ligne a deux nombres
    nombres = ligne.split()
    a = int(nombres[0])
    b = int(nombres[1])
    # affichons leur somme
    print(a + b)