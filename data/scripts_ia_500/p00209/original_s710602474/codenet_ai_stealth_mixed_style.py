def main(piece, c):
    for h in range(n - m + 1):
        for w in range(n - m + 1):
            res = f(piece, h, w)
            if res:
                break
    if c != 4:
        move(piece, c)
    else:
        if ans:
            print(ans[0], ans[1])
        else:
            print('NA')

def f(piece, h, w):
    global ans
    coordinate = None
    for _h in range(m):
        for _w in range(m):
            if piece[_h][_w] != '-1':
                if piece[_h][_w] == picture[h + _h][w + _w]:
                    if coordinate is None:
                        coordinate = (w + _w + 1, h + _h + 1)
                        if ans is not None:
                            if coordinate[1] > ans[1]:
                                return
                            elif coordinate[1] == ans[1] and coordinate[0] > ans[0]:
                                return
                else:
                    return
    else:
        ans = coordinate
        return True

def move(piece, c):
    _piece = []
    for w in range(m):
        lis = []
        for h in range(m):
            lis.append(piece[h][w])
        lis.reverse()
        _piece.append(lis)
    main(_piece, c + 1)

while True:
    try:
        n, m = [int(x) for x in raw_input().strip().split()]
    except Exception:
        break
    if n == 0 and m == 0:
        break
    picture = []
    for _ in range(n):
        picture.append(raw_input().strip().split())
    piece = list()
    for _ in range(m):
        piece.append(raw_input().strip().split())
    ans = None
    main(piece, 1)