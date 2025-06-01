def main(piece, c):
    global ans
    for h in range(n - m + 1):
        w = 0
        while w < n - m + 1:
            if f(piece, h, w):
                break
            w += 1
    if c != 4:
        move(piece, c)
    else:
        if ans:
            print(ans[0], ans[1])
        else:
            print("NA")

def f(piece, h, w):
    global ans
    coordinate = None
    for _h in range(m):
        for _w in range(m):
            if piece[_h][_w] != '-1':
                if piece[_h][_w] == picture[h + _h][w + _w]:
                    if coordinate is None:
                        coordinate = (w + _w + 1, h + _h + 1)
                else:
                    return
    else:
        if ans is None:
            ans = coordinate
        elif coordinate[1] < ans[1]:
            ans = coordinate
        elif coordinate[1] == ans[1] and coordinate[0] < ans[0]:
            ans = coordinate
        return True

def move(piece, c):
    _piece = []
    h = 0
    while h < m:
        lis = []
        w = 0
        while w < m:
            lis.append(piece[m - 1 - w][h])
            w += 1
        _piece.append(lis)
        h += 1
    main(_piece, c + 1)

while True:
    line = raw_input()
    if not line:
        continue
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    picture = []
    for _ in range(n):
        picture.append(raw_input().split())
    piece = []
    for _ in range(m):
        piece.append(raw_input().split())
    ans = None
    main(piece, 1)