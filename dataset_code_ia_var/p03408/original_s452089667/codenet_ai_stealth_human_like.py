number = int(input())
sList = []
for hey in range(number):  # on remplit la liste... j'espère que c'est bon
    sList.append(input())

m = int(input())
tList = []
for xx in range(m):
    tList.append(input())

the_max = 0  # c'est ici qu'on va stocker le max, enfin je crois
for idx in range(number):
    c = 0
    for j2 in range(number):
        # Compter les occurrences dans sList (on double peut-être un peu les trucs ici)
        if sList[idx] == sList[j2]:
            c += 1
    for tr in tList:
        if sList[idx] == tr:
            c -= 1  # On enlève pour chaque correspondance dans tList
    if c > the_max:
        the_max = c
print(the_max)  # Résultat final... crossing fingers