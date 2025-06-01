nombre_total_jours = int(input())
nombre_evenements = int(input())
niveau_actuel = niveau_maximum = nombre_evenements
for index_evenement in range(nombre_total_jours):
    valeur_entree, valeur_sortie = [int(valeur) for valeur in input().split()]
    if niveau_actuel < 0:
        continue
    niveau_actuel += valeur_entree - valeur_sortie
    if niveau_maximum < niveau_actuel:
        niveau_maximum = niveau_actuel
    if niveau_actuel < 0:
        niveau_maximum = 0
print(niveau_maximum)