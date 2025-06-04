# Bon alors, j'ai essayé de rendre le code un peu plus "humain"
lettres = [chr(j) for j in range(65,91)] + list(" .,-'?")
decode_dict = {
    '101': ' ', '000000': "'", '000011': ',', '10010001': '-',
    '010001': '.', '000001': '?', 
    '100101': 'A', '10011010': 'B', '0101': 'C', '0001': 'D',
    '110': 'E', '01001': 'F', '10011011': 'G', '010000': 'H',
    '0111': 'I', '10011000': 'J', '0110': 'K', '00100': 'L',
    '10011001': 'M', '10011110': 'N', '00101': 'O', '111': 'P',
    '10011111': 'Q', '1000': 'R', '00110': 'S', '00111': 'T',
    '10011100': 'U', '10011101': 'V', '000010': 'W', '10010010': 'X',
    '10010011': 'Y', '10010000': 'Z'
}
# Boucle principale, on va lire jusqu'à ce qu'il n'y ait plus rien à lire
while True:
    try:
        chaine = input()  # On essaie de prendre une ligne. S'il n'y en a plus, ça va crasher et sortir.
    except:
        break
    binary = ''  # On va stocker la version binaire ici
    resultat = ''
    for lettre in chaine:
        # On regarde où est la lettre dans la liste : si elle y est pas ça va planter, tant pis...
        ind = lettres.index(lettre)
        bits = bin(ind)[2:]  # on vire le '0b'
        bits = bits.zfill(5)  # 5 bits (c'est peut-être inefficace mais bon)
        binary += bits
    morceau = ''
    for k in range(len(binary)):
        morceau += binary[k]
        if morceau in decode_dict:
            print(decode_dict[morceau], end='')
            morceau = ''
        # sinon on attend jusqu'à matcher une entrée
    print('')  # Prochaine ligne !