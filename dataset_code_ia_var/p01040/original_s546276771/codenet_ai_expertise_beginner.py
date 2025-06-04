import datetime

# Lire les entrées
y1, m1, d1, y2, m2, d2 = map(int, input().split())

# Calcul pour ajuster les années
qq = y1 // 400
y1 = y1 % 400
y1 += 400
qq = qq - 1
q = (y2 - y1) // 400
y2 = y2 - 400 * q
a = 688 * (q - qq)

# Création de la date de départ
date_depart = datetime.date(y1, m1, d1)
date_fin = datetime.date(y2, m2, d2)

# Boucle sur chaque jour entre date_depart et date_fin
while date_depart <= date_fin:
    # Vérifier si c'est un vendredi 13
    if date_depart.day == 13 and date_depart.weekday() == 4:
        a += 1
    # Passer au jour suivant
    date_depart = date_depart + datetime.timedelta(days=1)

print(a)