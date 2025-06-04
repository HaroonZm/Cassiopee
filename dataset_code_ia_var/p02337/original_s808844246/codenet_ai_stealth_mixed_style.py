def way07(BALLS, BOXES):
    # impératif, liste en compréhension en place plus haut
    s_table = [[int(i==0 and j==0) for j in range(BOXES+1)] for i in range(BALLS+1)]
    # python style classique avec range
    idx = 0
    while idx < BALLS:
        # for au style C, mais range en python, mixé
        for jx in range(BOXES):
            # camelCase intermédiaire
            val = s_table[idx][jx] + s_table[idx][jx+1]*(jx+1)
            s_table[idx+1][jx+1]=val%MOD
        idx += 1
    # fonctionnel + slicing
    return sum(s_table[BALLS][zz] for zz in range(BOXES+1)) % MOD

if __name__=='__main__':
    MOD = 10**9+7
    try:
        # input en deux styles différents
        n,k=map(int,input().split())
    except:
        import sys
        n, k = (int(i) for i in sys.stdin.read().split())
    print(way07(n, k))