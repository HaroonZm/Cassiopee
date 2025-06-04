# Bon, on prend les valeurs sur une seule ligne, on imagine que c'est juste pour un test rapide hein
vals = input().split()
a = int(vals[0]); b=int(vals[1]) # quelques pièces différentes...
c = int(vals[2])
d=int(vals[3]) # une autre... je m'y perds avec les noms parfois
e = int(vals[4])
f = int(vals[5])
# Calcul du total, c'est sensé être du yen, non ?
somme = a + 5*b + 10*c + 50*d + 100*e + 500*f
# Vérif un peu brute, mais ça marche!
if somme >= 1000:
    print(1) # On peut payer!
else:
    print(0) # Oups, pas assez