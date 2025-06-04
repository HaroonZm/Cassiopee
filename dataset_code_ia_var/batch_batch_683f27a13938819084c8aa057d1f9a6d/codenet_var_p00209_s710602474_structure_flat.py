while True:
    n, m = map(int, raw_input().split())
    if n == m == 0:
        break
    picture = [raw_input().split() for i in range(n)]
    piece = [raw_input().split() for i in range(m)]
    ans = None
    c = 1
    _piece_list = [piece]
    c_list = [c]
    while c_list:
        piece = _piece_list.pop()
        c = c_list.pop()
        found = False
        h_loop_break = False
        for h in range(n - m + 1):
            if h_loop_break:
                break
            for w in range(n - m + 1):
                coordinate = None
                ok = True
                for _h in range(m):
                    if not ok:
                        break
                    for _w in range(m):
                        if piece[_h][_w] != '-1':
                            if piece[_h][_w] == picture[h + _h][w + _w]:
                                if coordinate is None:
                                    coordinate = (int(w + _w + 1), int(h + _h + 1))
                                    if ans:
                                        if coordinate[1] > ans[1]:
                                            ok = False
                                            break
                                        elif coordinate[1] == ans[1]:
                                            if coordinate[0] > ans[0]:
                                                ok = False
                                                break
                            else:
                                ok = False
                                break
                    if not ok:
                        break
                else:
                    ans = coordinate
                    found = True
                    h_loop_break = True
                    break
        if c != 4:
            # rotate piece
            _piece = []
            for w in range(m):
                lis = []
                for h in range(m):
                    lis.append(piece[h][w])
                lis.reverse()
                _piece.append(lis)
            _piece_list.append(_piece)
            c_list.append(c + 1)
            continue
        else:
            if ans:
                print ans[0], ans[1]
            else:
                print 'NA'