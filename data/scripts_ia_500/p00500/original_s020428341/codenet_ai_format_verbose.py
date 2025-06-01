nombre_de_triplets = int(input())

liste_premieres_valeurs = []
liste_secondes_valeurs = []
liste_troisiemes_valeurs = []

for indice in range(nombre_de_triplets):
    premiere_valeur, seconde_valeur, troisieme_valeur = map(int, input().split())
    liste_premieres_valeurs.append(premiere_valeur)
    liste_secondes_valeurs.append(seconde_valeur)
    liste_troisiemes_valeurs.append(troisieme_valeur)

resultats = [0] * nombre_de_triplets

for indice in range(nombre_de_triplets):
    valeur_premiere = liste_premieres_valeurs[indice]
    valeur_seconde = liste_secondes_valeurs[indice]
    valeur_troisieme = liste_troisiemes_valeurs[indice]

    if liste_premieres_valeurs.count(valeur_premiere) == 1:
        resultats[indice] += valeur_premiere

    if liste_secondes_valeurs.count(valeur_seconde) == 1:
        resultats[indice] += valeur_seconde

    if liste_troisiemes_valeurs.count(valeur_troisieme) == 1:
        resultats[indice] += valeur_troisieme

    print(resultats[indice])