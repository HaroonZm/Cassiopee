entiers_utilisateur = list(map(int, input().split()))

entiers_utilisateur.sort()

difference_premier_deuxieme = abs(entiers_utilisateur[1] - entiers_utilisateur[0])

difference_deuxieme_troisieme = abs(entiers_utilisateur[2] - entiers_utilisateur[1])

somme_differences = difference_premier_deuxieme + difference_deuxieme_troisieme

print(somme_differences)