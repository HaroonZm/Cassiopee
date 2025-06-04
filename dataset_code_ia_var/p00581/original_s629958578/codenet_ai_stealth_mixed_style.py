def main():
    # Style procédural pour la lecture d'entrée
    dimensions = input().split()
    h = int(dimensions[0])
    w = int(dimensions[1])
    mp = []
    for _ in range(h):
        mp.append(input())

    # Style liste en compréhension pour initialisation
    i_cnt, o_cnt = [[0]*w for _ in range(h)], []
    for _ in range(h):
        o_cnt.append([0]*w)

    # Boucle de type C
    x = 0
    while x < w:
        if mp[-1][x] == 'I':
            i_cnt[-1][x] = 1
        x += 1

    # Utilisation de range et enumerate
    for idx, row in enumerate(mp):
        if row[-1] == 'O':
            o_cnt[idx][-1] = 1

    ans = 0

    # Style fonctionnel mélangé à l'impératif
    rows = list(range(h-2, -1, -1))
    for y in rows:
        for x in reversed(range(w-1)):
            c = mp[y][x]
            if c == "I":
                i_cnt[y][x] = i_cnt[y+1][x] + 1
                o_cnt[y][x] = o_cnt[y][x+1]
            elif c == "O":
                i_cnt[y][x] = i_cnt[y+1][x]
                o_cnt[y][x] = o_cnt[y][x+1] + 1
            else:
                # Style pythonique (in-line calculation)
                i_cnt[y][x], o_cnt[y][x] = i_cnt[y+1][x], o_cnt[y][x+1]
                ans += i_cnt[y][x] * o_cnt[y][x]

    # Style one-liner
    print(ans)

main()