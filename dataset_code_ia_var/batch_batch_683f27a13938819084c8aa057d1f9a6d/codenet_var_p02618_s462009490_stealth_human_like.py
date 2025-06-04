# Bon, je vais essayer d'écrire ça comme je le ferais après une journée compliquée :)

d = int(input())  # nb de jours (enfin je crois, attention c'est -1 index là-haut!)
c = list(map(int, input().split()))
total_c = 0
for x in range(26):
    total_c += c[x]    # pas sûr qu'on s'en serve après, mais bon

# ah oui, s c'est un tableau 2D ou un genre de matrix?
s = [None]*d
for day in range(d):
    scores = list(map(int, input().split()))
    s[day] = scores  # parce que c'est plus lisible comme ça ?

# t c'est les types de je sais plus quoi sur chaque jour
t = [0]*d
last_done = [-1]*26  # dernière fois qu'on a fait un type, initialisé à -1 (on commence jamais)

for i in range(d):
    # je suppose qu'il faut choisir le meilleur type chaque jour
    best_point = -9999999
    for j in range(26):
        point = s[i][j]
        # pfff, il faut boucler encore
        for k in range(26):
            if j != k:
                point -= c[k]*(i - last_done[k])
        if point > best_point:
            best_point = point
            t[i] = j
    last_done[t[i]] = i
    print(t[i]+1)  # on ajoute +1... je suppose que c'est pour s'aligner avec 1-indexé ?