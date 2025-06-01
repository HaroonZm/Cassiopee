nombre_total_entrees = int(input())

valeur_a = int(input())

valeur_b = int(input())

valeur_c = int(input())

valeur_d = int(input())

rapport_a_sur_c = valeur_a / valeur_c

rapport_b_sur_d = valeur_b / valeur_d

maximum_rapport = max(rapport_a_sur_c, rapport_b_sur_d)

resultat_final = int(nombre_total_entrees - maximum_rapport)

print(resultat_final)