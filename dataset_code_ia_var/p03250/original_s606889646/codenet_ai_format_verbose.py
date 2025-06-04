premier_entier, deuxieme_entier, troisieme_entier = map(int, input().split())

liste_nombres = [premier_entier, deuxieme_entier, troisieme_entier]

somme_totale = sum(liste_nombres)

valeur_maximale = max(liste_nombres)

resultat_final = somme_totale - valeur_maximale + valeur_maximale * 10

print(resultat_final)