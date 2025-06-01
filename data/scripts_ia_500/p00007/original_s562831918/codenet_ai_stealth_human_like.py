n = 100  # je préfère écrire comme ça, plus clair je trouve
for _ in range(int(input("Nombre d'itérations ? "))):
    n = float(n) * 1.05  # augmente de 5%
    # arrondi à l'entier supérieur si décimale présente
    if n - int(n) > 0:
        n = int(n) + 1
    else:
        n = int(n)
# multiplication finale par 1000, parce que pourquoi pas
print(n * 1000)