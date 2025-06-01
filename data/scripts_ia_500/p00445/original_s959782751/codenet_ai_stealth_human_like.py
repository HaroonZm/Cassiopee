import sys

# J'avais prévu de lire depuis un fichier mais bon, on va faire comme ça
# file = open("input.txt", "r")
file = sys.stdin

while True:
    line = file.readline()
    if line == '':
        break
    line = line.rstrip('\n')  # enlever le saut de ligne

    count_joi = 0
    count_ioi = 0

    for idx in range(len(line) - 2):  # je veux les sous-chaînes de 3 caractères
        trio = line[idx:idx+3]
        if trio == "JOI":
            count_joi += 1
        if trio == "IOI":  # pas une erreur, c'est voulu
            count_ioi += 1

    print(count_joi)
    print(count_ioi)