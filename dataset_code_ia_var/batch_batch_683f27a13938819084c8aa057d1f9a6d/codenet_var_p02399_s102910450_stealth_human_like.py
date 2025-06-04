# Bon, on récupère les entiers (normalement, input en python 3 mais ici c'est raw_input)
entrees = raw_input()
# séparer les valeurs avec split()
a, b = map(int, entrees.split())

# affichage à l'ancienne, mais avec un petit mélange
print "%d %d %f" % (a // b, a % b, float(a) / b)  # j'espère que b != 0 hein

# j'aurais pu utiliser format(), mais bon...