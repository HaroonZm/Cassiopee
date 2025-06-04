# bon ben on fait le calcul de l'aire et la circonférence, hein
a = float(input()) # rayon ou truc comme ça
pi = 3.1415926535897   # pas sûr du nombre de chiffres après la virgule, mais ça ira
aire = pi*a*a
circonference = pi*a*2   # normalement c'est 2*pi*a, non? Bah, ça passe.
# affichage un peu à l'arrache
print(str(aire) + " " + str(circonference))