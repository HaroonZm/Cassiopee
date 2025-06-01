# Programme Python complet pour afficher l'histogramme des ventes d'ice creams

# L'approche :
# 1. Lire le nombre total d'ice creams vendus n.
# 2. Si n == 0, fin du traitement.
# 3. Lire n lignes contenant le numéro de glace vendu.
# 4. Compter le nombre de ventes pour chaque type (0 à 9).
# 5. Pour chaque type d'ice cream, afficher :
#    - autant d'astérisques '*' que vendus, si au moins 1 vendu
#    - un '-' si aucun vendu
# 6. Répéter pour chaque jeu de données jusqu'à ce que n == 0.

while True:
    n = input()
    if n == '0':  # Condition d'arrêt
        break
    n = int(n)

    # Initialiser un tableau de compteurs pour les 10 types d'ice creams
    counts = [0]*10

    # Lire les ventes et compter
    for _ in range(n):
        c = int(input())
        counts[c] += 1

    # Afficher l'histogramme pour les 10 types, de 0 à 9
    for count in counts:
        if count == 0:
            print('-')
        else:
            print('*' * count)