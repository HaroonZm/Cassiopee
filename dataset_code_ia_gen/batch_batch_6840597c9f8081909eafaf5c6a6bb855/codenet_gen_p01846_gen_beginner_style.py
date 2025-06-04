while True:
    S = input()
    if S == '#':
        break
    a,b,c,d = map(int, input().split())
    rows = S.split('/')
    H = len(rows)
    # Décoder la première ligne pour trouver la largeur
    W = 0
    for ch in rows[0]:
        if ch == 'b':
            W += 1
        else:
            W += int(ch)
    # Construire la grille en liste de listes
    grid = []
    for row in rows:
        line = []
        i = 0
        while i < len(row):
            if row[i] == 'b':
                line.append('b')
                i += 1
            else:
                num = 0
                while i < len(row) and row[i].isdigit():
                    num = num * 10 + int(row[i])
                    i += 1
                for _ in range(num):
                    line.append('.')
        grid.append(line)
    # Déplacer la balle (a,b) vers (c,d)
    grid[a-1][b-1] = '.'
    grid[c-1][d-1] = 'b'
    # Générer le jfen
    result_rows = []
    for line in grid:
        res = ''
        count = 0
        for cell in line:
            if cell == '.':
                count += 1
            else:
                if count > 0:
                    res += str(count)
                    count = 0
                res += 'b'
        if count > 0:
            res += str(count)
        result_rows.append(res)
    print('/'.join(result_rows))