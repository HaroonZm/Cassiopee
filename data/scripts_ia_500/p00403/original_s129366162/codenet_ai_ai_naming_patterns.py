nombre_entrees = int(input())
liste_chats = list(map(int, input().split()))

pile_trous = []
statut_resultat = "OK"

for index_chaton in range(nombre_entrees):
    valeur_chaton = liste_chats[index_chaton]
    if valeur_chaton < 0:
        if len(pile_trous) == 0 or valeur_chaton != -1 * pile_trous[-1]:
            statut_resultat = str(index_chaton + 1)
            break
        else:
            pile_trous.pop()
    else:
        if valeur_chaton in pile_trous:
            statut_resultat = str(index_chaton + 1)
            break
        else:
            pile_trous.append(valeur_chaton)

print(statut_resultat)