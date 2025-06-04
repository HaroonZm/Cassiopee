import itertools

def main():
    # Prépare les voisins de chaque case (en 0-based)
    k = [
        [1, 3, 4],
        [2, 0, 5],
        [3, 1, 6],
        [0, 2, 7],
        [7, 5, 0],
        [4, 6, 1],
        [5, 7, 2],
        [6, 4, 3]
    ]

    # Crée la liste de tous les motifs nécessaires
    patterns = []
    for i in range(8):
        for j in range(3):
            pattern = [-1] * 8
            pattern[0] = i
            pattern[1] = k[i][j]
            pattern[3] = k[i][(j+1)%3]
            # Trouve le point t[2]
            for l in range(8):
                if l == i:
                    continue
                if (pattern[1] in k[l]) and (pattern[3] in k[l]):
                    pattern[2] = l
                    break
            # Complète le motif pour t[4] à t[7]
            for l in range(4):
                neigs = k[pattern[l]]
                for m in range(3):
                    if neigs[m] not in pattern:
                        pattern[l+4] = neigs[m]
                        break
            patterns.append(pattern)

    # Fonction qui compte uniquement les choix distincts de permutations sous motifs symétriques
    def f(a):
        used = set()
        count = 0
        for t in itertools.permutations(a):
            if t in used:
                continue
            count += 1
            for p in patterns:
                used.add(tuple(t[p[i]] for i in range(8)))
        return count

    result = []
    while True:
        try:
            a = input().split()
        except EOFError:
            break
        if len(a) == 0:
            break
        res = f(a)
        result.append(str(res))

    print('\n'.join(result))

main()