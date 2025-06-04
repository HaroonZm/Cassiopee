def calculer_plus_grand_commun_diviseur(nombre1, nombre2):
    if nombre2 == 0:
        return nombre1
    return calculer_plus_grand_commun_diviseur(nombre2, nombre1 % nombre2)


nombre_total_entrees = int(input())

liste_nombres = [int(input()) for compteur_index in range(nombre_total_entrees)]

plus_petit_commun_multiple = 1

for nombre_actuel in liste_nombres:
    pgcd = calculer_plus_grand_commun_diviseur(plus_petit_commun_multiple, nombre_actuel)
    plus_petit_commun_multiple = (plus_petit_commun_multiple * nombre_actuel) // pgcd

print(plus_petit_commun_multiple)