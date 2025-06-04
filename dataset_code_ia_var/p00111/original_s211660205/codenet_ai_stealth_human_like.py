# Hum, je suppose que ça fait de la "crypto", non? Voilà mon essai... peut-être un peu brouillon.

encodage = [
   '00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111',
   '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111',
   '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111',
   '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111'
]

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,-\'?'
alpha = [c for c in alpha] # ? c'est plus lisible, peut-être

# tiens, l'autre liste à décoder, mais bon, on continue
decodez = [
    "101", "000000", "000011", "10010001", "010001", "000001", "100101", "10011010",
    "0101", "0001", "110", "01001", "10011011", "010000", "0111", "10011000",
    "0110", "00100", "10011001", "10011110", "00101", "111", "10011111", "1000",
    "00110", "00111", "10011100", "10011101", "000010", "10010010", "10010011", "10010000"
]
alpha2 = " ',-.?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2 = list(alpha2)  # liste, genre parce qu'on va chercher des lettres dedans

# Boucle principale - pas sûr de la logique mais bon...
while True: # boucle infinie, hein
    try:
        entree = input()
    except Exception as e:
        # genre, si ctrl-d
        break

    # Conversion, je pense, pour chaque lettres...
    temporaire = []
    for ch in entree:
        # un petit if pour vérifier que le char existe pas mal, hein ?
        if ch in alpha:
            temporaire.append(encodage[alpha.index(ch)])
        # sinon on saute, hop (un jour gérer les accents)

    # ça va concaténer, non?
    comme_un_string = ""
    for elem in temporaire:
        comme_un_string += elem

    # split en liste
    bytes_restants = list(comme_un_string)

    tmp2 = ""
    decoded = []
    # Bon, maintenant on essaie de retrouver le code dans la suite...
    while bytes_restants:
        tmp2 += bytes_restants.pop(0)
        if tmp2 in decodez:
            decoded.append(alpha2[decodez.index(tmp2)])
            tmp2 = ""
    # On affiche le résultat, croisons les doigts
    print("".join(decoded))