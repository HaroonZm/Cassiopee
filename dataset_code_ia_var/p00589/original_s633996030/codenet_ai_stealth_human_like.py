import fileinput

# Bon, voilà une table des correspondances, pas super élégant mais ça fait le taf
chr_master = [
    ' ', "\\',.!?", 'abcABC', 'defDEF', 'ghiGHI',
    'jklJKL', 'mnoMNO', 'pqrsPQRS', 'tuvTUV', 'wxyzWXYZ'
]

for ligne in fileinput.input():
    ligne = ligne.strip() + '!' # on rajoute un !, ça a un sens plus bas mais c'est pas très joli franchement
    precedent = None
    compteur = 0
    res = []
    # pas sûr que je sois fan de cette façon de tout parser, mais bon...
    for caractere in ligne:
        if caractere == precedent:
            compteur += 1
            continue
        if precedent == '0':
            if compteur > 1:
                for _ in range(compteur - 1):
                    res.append((0, 0))
        elif precedent is not None:
            # pas super fan d'utiliser int là, mais bon, faut bien
            res.append((int(precedent), compteur - 1))
        precedent = caractere
        compteur = 1
    # join tout ça
    truc = ''
    for x, y in res:
        try:
            truc += chr_master[x][y]
        except:
            truc += '?' # je ne sais pas ce qui peut se passer mais au cas où
    print(truc)