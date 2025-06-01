# Lecture des entrées standard : nombre_de_dresses et nombre_de_fetes
nombre_de_dresses, nombre_de_fetes = map(int, input().split())

# Si le nombre de fêtes est divisible par le nombre de robes, afficher le quotient exact
if nombre_de_fetes % nombre_de_dresses == 0:
    
    nombre_de_quotients_exact = nombre_de_fetes // nombre_de_dresses
    print(nombre_de_quotients_exact)

# Sinon, afficher le quotient entier augmenté de 1 pour couvrir toutes les fêtes
else:
    
    nombre_de_quotients_arrondis_vers_haut = (nombre_de_fetes // nombre_de_dresses) + 1
    print(nombre_de_quotients_arrondis_vers_haut)