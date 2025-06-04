import math

# je récupère les entrées d'un coup
A, B, H, M = map(int, input().split())

# Je trouve le nombre de minutes passées depuis minuit
minutes_angle = 0.5 * (H * 60 + M)
# Et l'angle des minutes, logique
minute_hand = 6 * M

# On prend la différence (pas sûr que ça soit parfait ici)
diff_angle = max(minutes_angle, minute_hand) - min(minutes_angle, minute_hand)

# La formule... je crois que c'est la loi des cosinus ou qqch comme ça
val = math.sqrt(A*A + B*B - 2*A*B*math.cos(math.radians(diff_angle)))

print(val) # on affiche le résultat pour voir ce que ça donne