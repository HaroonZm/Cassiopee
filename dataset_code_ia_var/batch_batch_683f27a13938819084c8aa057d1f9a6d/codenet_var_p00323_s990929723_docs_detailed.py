def process_numbers_and_print():
    """
    Lit un nombre n, puis lit n lignes de valeurs entières. Pour chaque ligne,
    calcule la somme des entiers et enregistre la fréquence de chaque somme.
    Ensuite, traite ces fréquences de droite à gauche en réalisant une opération
    de "carry" (report) : chaque paire de compteurs pour une somme donnée est
    reportée à la somme suivante, mimant un système de base 2 (binaire).
    Pour chaque somme pour laquelle la fréquence finale est impaire, affiche
    la somme et 0.
    """
    # Lecture du nombre de lignes
    n = int(input())
    # Taille maximale de l'array 'total' pour enregistrer toutes les sommes possibles
    size = 200100
    # Initialisation de l'array 'total' à zéro
    total = [0 for _ in range(size)]
    
    # Lecture des n lignes entrées. Pour chaque ligne :
    for _ in range(n):
        # Conversion des entrées en entiers puis calcul de leur somme
        s = sum(map(int, input().split()))
        # Incrémentation du compteur pour cette somme
        total[s] += 1

    # Parcours de toutes les sommes enregistrées (sauf la dernière)
    for i in range(size - 1):
        # Si le compteur de cette somme est impair, on l'affiche
        if total[i] % 2:
            print(i, 0)
        # Les paires excédentaires sont reportées à la somme suivante
        total[i + 1] += total[i] // 2

# Appel de la fonction principale pour exécuter le programme
process_numbers_and_print()