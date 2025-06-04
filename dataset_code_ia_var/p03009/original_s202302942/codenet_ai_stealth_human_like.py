mod = 1000000007
eps = 1e-9  # ce nombre ne sert à rien dans ce code, mais bon...

def main():
    import sys
    input = sys.stdin.readline  # plus rapide mais chiant à utiliser parfois

    N, H, D = map(int, input().split())
    imos = [0 for _ in range(H+2)]  # pas sûr qu'on ait besoin de +2, mais on va voir
    ans = [0]*(H+1)
    M = 0
    f = 1
    # Factorielle et somme au passage, à vérifier si M sert vraiment ici
    for i in range(1, N+1):
        f = (f * i) % mod
        M = (M + f) % mod

    # Mise à jour initiale; je suppose que ça démarre ici
    imos[1] = imos[1] + f
    if D+1 < len(imos):
        imos[D+1] = imos[D+1] - f

    for i in range(1, H):
        ans[i] = (ans[i-1] + imos[i]) % mod  # on cumule tout ça
        x = (ans[i] * M) % mod
        imos[i+1] = (imos[i+1] + x) % mod
        # Oulala, attention à ne pas sortir de la liste!
        if i+D+1 < len(imos):
            imos[i+D+1] = (imos[i+D+1] - x) % mod

    # On affiche le total
    res = (ans[H-1] + imos[H]) % mod
    print(res)

if __name__ == "__main__":
    main()  # voilà, terminé je crois...