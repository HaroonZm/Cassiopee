# Bon, je commence par une liste vide
ma_liste = []
for x in range(5):
    # On remplit la liste via input, classique
    val = int(input())
    ma_liste.append(val)

resultat = 0
if ma_liste[0] < 0:
    # Ok, le premier est négatif... c'est pas terrible
    resultat = resultat + ((0 - ma_liste[0]) * ma_liste[2])
    resultat = resultat + ma_liste[3]
    # On fait le produit ici aussi, à confirmer si besoin
    resultat += ma_liste[1] * ma_liste[4]
elif ma_liste[0] > 0:
    # Sinon si x est plus grand que 0, on essaye comme ça
    resultat += (ma_liste[1] - ma_liste[0]) * ma_liste[4]
# Pas de cas pour == 0, on dirait que c'est volontaire ?

print(resultat)