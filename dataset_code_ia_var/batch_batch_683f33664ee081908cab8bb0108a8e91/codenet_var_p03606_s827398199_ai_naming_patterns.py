nombre_groupes = int(input())
liste_intervalles = []
for indice_groupe in range(1, nombre_groupes + 1):
    entree_intervalle = input()
    liste_intervalles.append(entree_intervalle)
compteur_total = 0
for intervalle_str in liste_intervalles:
    borne_debut, borne_fin = intervalle_str.split()
    compteur_total += (int(borne_fin) - int(borne_debut)) + 1
print(compteur_total)