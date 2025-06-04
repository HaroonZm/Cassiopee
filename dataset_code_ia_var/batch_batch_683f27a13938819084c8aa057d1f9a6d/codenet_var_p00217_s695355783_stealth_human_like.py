# Boucle principale; continue jusqu'à ce qu'on entre 0
while True:
    n = int(input())
    if n == 0:
        break
    maxn = 0
    maxv = -1 # Pour être sûr que n'importe quelle somme soit plus grande
    # Je fais une boucle pour chaque ligne saisie
    for i in range(n):
        line = input()
        aa, bb, cc = map(int, line.split())
        s = bb+cc
        # Je pense que c'est comme ça qu'on fait
        if s > maxv: 
            maxv = s
            maxn = aa
    # Affiche le résultat demandé, j'espère que c'est ce qu'on veut
    print(maxn, maxv)