def est_bissextile(annee):
    if annee % 400 == 0:
        return True
    if annee % 100 == 0:
        return False
    if annee % 4 == 0:
        return True
    return False

jours_normaux = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
jours_bissextile = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

Y1, M1, D1, Y2, M2, D2 = map(int, input().split())
jours_vendredis_13 = [0] * (2800*366)
compteur_jours = 0
tmp, Y1 = divmod(Y1, 2800)
reponse1 = tmp * 4816
tmp, Y2 = divmod(Y2, 2800)
reponse2 = tmp * 4816

for annee in range(0, 2800):
    if est_bissextile(annee):
        mois = jours_bissextile
    else:
        mois = jours_normaux
    for idx_mois, nb_jours in enumerate(mois, 1):
        jour_13 = compteur_jours + 12
        if jour_13 % 7 == 6:
            jours_vendredis_13[jour_13] = 1
        if Y1 == annee and M1 == idx_mois:
            reponse1 += sum(jours_vendredis_13[:compteur_jours + (D1 - 1)])
        if Y2 == annee and M2 == idx_mois:
            reponse2 += sum(jours_vendredis_13[:compteur_jours + D2])
        compteur_jours += nb_jours

print(reponse2 - reponse1)