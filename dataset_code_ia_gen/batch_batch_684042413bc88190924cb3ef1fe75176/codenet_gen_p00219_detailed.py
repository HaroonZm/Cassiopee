# Programme pour afficher un histogramme des ventes de 10 types d'ice cream, de 0 à 9.
# Pour chaque dataset, on compte combien de fois chaque type est vendu.
# Ensuite, pour chaque type, on imprime autant d'étoiles que le nombre vendu.
# S'il n'y a aucune vente pour un type, on imprime un tiret.
# L'entrée se termine par un zéro seul.

while True:
    n = int(input())
    if n == 0:
        # Fin des entrées
        break

    # Initialisation d'une liste pour compter les ventes de chaque type (0 à 9)
    counts = [0] * 10

    # Lecture des types vendus et comptage
    for _ in range(n):
        c = int(input())
        counts[c] += 1

    # Affichage de l'histogramme selon les règles
    for count in counts:
        if count == 0:
            print("-")
        else:
            print("*" * count)