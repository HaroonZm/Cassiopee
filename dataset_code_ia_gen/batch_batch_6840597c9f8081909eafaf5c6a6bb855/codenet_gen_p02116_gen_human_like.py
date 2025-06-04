n = int(input())

# d'après le théorème de Lucas pour les combinaisons modulo 2,
# nCm est impair si et seulement si m & n == m (en binaire)
# on cherche donc le plus petit m tel que nCm soit pair,
# donc le plus petit m où m & n != m,
# c'est-à-dire où m contient un bit à 1 là où n a un 0.

m = 1
while (m & n) == m:
    m += 1
print(m)