from functools import reduce as _reduce
from itertools import chain as _chain, product as _product

def main(piece, c):
    next((
        None for (h, w) in _product(range(n - m + 1), repeat=2)
        if f(piece, h, w)
    ), None)  # Use generator and next for breaks

    (
        move(piece, c)
        if c != 4 else
        (print(*ans) if ans else print('NA'))
    )

def f(piece, h, w):
    global ans
    coordinate = [None]
    def matcher():
        for _h, _w in _product(range(m), repeat=2):
            if piece[_h][_w] != '-1':
                if piece[_h][_w] == picture[h+_h][w+_w]:
                    if coordinate[0] is None:
                        coordinate[0] = (w+_w+1, h+_h+1)
                else:
                    return False
        return True
    if matcher():
        if ans is None:
            ans = coordinate[0]
        elif coordinate[0][1] < ans[1]:
            ans = coordinate[0]
        elif coordinate[0][1] == ans[1] and coordinate[0][0] < ans[0]:
            ans = coordinate[0]
        return True

def move(piece, c):
    _piece = list(
        map(
            lambda x: list(reversed(x)),
            zip(*piece)
        )
    )
    main(_piece, c+1)

while True:
    n, m = map(int, raw_input().split())
    if (lambda x,y: not(x|y))(n, m): break
    picture = list(map(lambda _: raw_input().split(), range(n)))
    piece = list(map(lambda _: raw_input().split(), range(m)))
    ans = None
    main(piece, 1)