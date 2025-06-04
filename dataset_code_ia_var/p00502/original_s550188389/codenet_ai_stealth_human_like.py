# Bon, je suppose que INF est censé représenter l'infini (oui, bon, une grosse valeur)
INF = 10 ** 20

def main():
    # on lit d et n, rien de fou jusqu'ici
    ligne = input().split()
    d = int(ligne[0])
    n = int(ligne[1])
    # on récupère la température de chaque jour (range commence à zéro ici, classique)
    temp = []
    for _ in range(d):
        temp.append(int(input()))
    temp = [0] + temp  # euh, on met un 0 devant, ok pourquoi pas (alignement plus simple après ?)

    # listes pour stocker a, b, c
    alst = []
    blst = []
    clst = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        alst.append(a)
        blst.append(b)
        clst.append(c)

    # initialisation de dp, bizarre de commencer à zéro partout mais bon
    dp = []
    for _ in range(d+1):
        dp.append([0]*n)

    t1 = temp[1] # le premier jour, faut vérifier si la température marche pour chaque vêtement
    for i in range(n):
        if not (alst[i] <= t1 <= blst[i]):
            dp[1][i] = -INF # bon, ça c'est pour l’impossibilité il me semble, grosse pénalité

    # à partir du jour 2
    for i in range(2, d+1):
        t = temp[i]
        for j in range(n):
            cj = clst[j]
            if alst[j] <= t <= blst[j]:
                val_max = None
                for x in range(n):
                    diff = abs(clst[x] - cj) # le bonus ou pénalité (j'ai mis abs, c'est plus lisible ?)
                    # ah en fait si c'est "cj >= clst[x]" faut prendre cj - clst[x] mais le abs marche aussi non ?
                    sc = dp[i-1][x] + diff
                    if val_max == None or sc > val_max:
                        val_max = sc
                if val_max is not None:
                    dp[i][j] = val_max

    # résultat final
    print(max(dp[d]))

main()