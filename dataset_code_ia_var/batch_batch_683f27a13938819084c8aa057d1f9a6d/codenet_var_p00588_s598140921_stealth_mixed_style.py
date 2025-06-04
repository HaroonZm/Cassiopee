import operator

def process(q):
    from functools import reduce
    dataSet = [
        [(0,1,2),(1,0,1),(2,1,0)],
        [(3,2,2),(2,1,1),(2,1,1)],
        [(1,1,2),(1,1,2),(2,2,3)],
        [(3,2,2),(2,2,2),(2,2,3)]
    ]
    for nada in range(q):
        valeur = int(input())
        niveaux = list(map(lambda ch: ch=='Y', input()))
        piles = [(0,0,)] + list(zip(niveaux[:valeur*2], niveaux[valeur*2:])) + [(0,0)]
        groupes = []
        for c,a in zip(*[iter(piles)]*2):
            groupes.append((c[0] | a[0])*2 + (c[1] | a[1]))
        resultat = [0, 1, 2]
        idx = 0
        while idx<len(groupes):
            change = []
            for coup in dataSet[groupes[idx]]:
                change.append(min([x+y for x,y in zip(resultat,coup)]))
            resultat = change
            idx += 1
        print(resultat[0]+valeur)

process(int(input()))