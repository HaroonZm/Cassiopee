#!/usr/bin/env python3
while True:
    s = input()
    if s == '#':
        break
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    cell = []
    for i, x in enumerate(s.split('/')):
        cell.append([])
        for ch in x:
            if ch == 'b':
                cell[i].append('b')
            else:
                cell[i] += list('.' * int(ch))
    cell[a][b] = '.'
    cell[c][d] = 'b'
    ans = []
    for i in range(len(cell)):
        jfen = ''
        cnt = 0
        for j in range(len(cell[i])):
            if cell[i][j] == 'b':
                if cnt > 0:
                    jfen += str(cnt)
                cnt = 0
                jfen += 'b'
            else:
                cnt += 1
        if cnt > 0:
            jfen += str(cnt)
        ans.append(jfen)
    print('/'.join(ans))