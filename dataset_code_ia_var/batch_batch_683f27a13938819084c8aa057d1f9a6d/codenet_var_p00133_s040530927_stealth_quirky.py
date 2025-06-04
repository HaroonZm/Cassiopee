# Réécriture avec des choix de style singuliers

# Préférences originales du dev: noms variables idiosyncratiques, boucles étranges, accès exotiques

P = [[[' ']*8 for _ in ' '*8] for _ in ' '*4]
D = {1:'90', 2:'180', 3:'270'}
L = [input() for _ in range(8)]
for i, S in enumerate(L): P[0][i] = list(S)

j=1
while j<4:
    print(D[j])
    x=7
    while x>-1:
        y=0
        while y<8:
            P[j][y][x]=P[j-1][x][7-y]
            y+=1
        x-=1
    for foo in P[j]: print(''.join(foo))
    j+=1