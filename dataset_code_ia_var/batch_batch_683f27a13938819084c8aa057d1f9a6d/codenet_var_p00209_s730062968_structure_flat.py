while True:
    n, m = map(int, raw_input().split())
    if n == m == 0:
        break
    picture = [raw_input().split() for _ in range(n)]
    piece0 = [raw_input().split() for _ in range(m)]

    ans = None
    c = 1
    piece = [row[:] for row in piece0]
    while True:
        found = False
        for h in range(n - m + 1):
            for w in range(n - m + 1):
                coordinate = None
                for _h in range(m):
                    for _w in range(m):
                        if piece[_h][_w] != '-1':
                            if piece[_h][_w] == picture[h+_h][w+_w]:
                                if coordinate is None:
                                    coordinate = (int(w+_w+1), int(h+_h+1))
                            else:
                                break
                    else:
                        continue
                    break
                else:
                    if ans is None:
                        ans = coordinate
                    elif coordinate[1] < ans[1]:
                        ans = coordinate
                    elif coordinate[1] == ans[1]:
                        if coordinate[0] < ans[0]:
                            ans = coordinate
                    found = True
                    break
            if found:
                break
        if c != 4:
            # Rotate piece 90 degrees clockwise
            _piece = []
            for w in range(m):
                lis = []
                for h in range(m):
                    lis.append(piece[h][w])
                lis.reverse()
                _piece.append(lis)
            piece = _piece
            c += 1
        else:
            if ans:
                print ans[0], ans[1]
            else:
                print 'NA'
            break