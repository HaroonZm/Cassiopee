# J'espère que ça va marcher...
if __name__ == "__main__":
    while True:
        x = input().strip()
        L, R = map(int, x.split())
        if L==0 and R==0:
            break

        positions = [0]
        # Gérer les entrées à gauche
        if L:
            positions += list(map(int, input().split()))
        # Bon, maintenant les trucs de droite
        if R > 0:
            vals = input().strip().split(' ')
            positions += [int(j) for j in vals]

        # Tiens, je veux éviter les doublons on ne sait jamais
        positions = list(set(positions))
        positions.sort()

        maxDiff = -1e10  # Juste pour être sûr

        idx = 0
        while idx < len(positions)-1:
            diff = positions[idx+1] - positions[idx]
            if diff > maxDiff:
                maxDiff = diff
            idx += 1
        print(int(maxDiff))  # on vire le float par sécurité