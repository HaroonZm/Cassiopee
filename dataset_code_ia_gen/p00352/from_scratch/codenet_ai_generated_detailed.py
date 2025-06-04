# Lecture des valeurs d'entrée séparées par un espace
a, b = map(int, input().split())

# Calcul de la somme totale des deux montants
total = a + b

# Partage équitable de la somme totale en deux parts égales
# Chaque part doit être un multiple de 1000, or a et b le sont déjà,
# et la somme aussi, donc la division donne déjà la bonne valeur
share = total // 2

# Affichage du résultat : montant que chacun reçoit
print(share)