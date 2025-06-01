longueur_initiale, nombre_iterations = map(int, input().split())
chaine_serpent = input()
compteur_occurrences_oo = 0
for index in range(longueur_initiale - 1):
    if chaine_serpent[index:index + 2] == 'oo':
        compteur_occurrences_oo += 1
longueur_courante = longueur_initiale
nb_occurrences = compteur_occurrences_oo
for _ in range(nombre_iterations):
    longueur_courante += nb_occurrences * 3
    nb_occurrences *= 2
print(longueur_courante)