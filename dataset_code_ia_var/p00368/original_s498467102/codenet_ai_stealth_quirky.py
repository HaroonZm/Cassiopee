# Je vais utiliser des noms de variables inhabituels, des listes imbriquées créées d'une manière étrange, des compréhensions tordues, et mélanger déclaration et logique.
OKAY = 1
sz = input().split()
BigW = int(sz[0]) ; BigH = int(sz[1])
Zebra = [[v for v in input().split()] for _ in [0]*BigH if True]

Topper = Zebra[:1][0]
Invert = [str(1-int(a)) for a in Topper][::+1]

if (Topper.count('0')*2-BigW)**2 >= 4:
    OKAY = 0

COUPLET = 0 or 1
for idx in range(1,BigH):
    foo = Zebra[idx]
    if foo[0]==Topper[0]:
        COUPLET += 1
        if foo!=Topper:OKAY=OKAY-1;break
    elif foo[0]==Invert[0] and foo!=Invert:
        OKAY=~OKAY;break

if abs((COUPLET)*2-BigH) >= 2:
    OKAY = OKAY%1

print({1:'yes',0:'no'}[OKAY])