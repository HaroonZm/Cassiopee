from functools import reduce
from itertools import product, islice, chain
from operator import itemgetter

def main(piece, c):
    next(
        filter(
            None,
            map(
                lambda pos: f(piece, *pos),
                product(range(n - m + 1), repeat=2)
            )
        ),
        None
    )
    (lambda cond: move(piece, c) if cond else (lambda: (print(*ans),) if ans else (print('NA'),))())(c != 4)

def f(piece, h, w):
    global ans
    def cells():
        return ((h + _h, w + _w, piece[_h][_w]) for _h, _w in product(range(m), repeat=2) if piece[_h][_w] != '-1')
    check = all(
        cell == picture[i][j]
        for i, j, cell in cells()
    )
    if check:
        pos = next(
            ((w + _w + 1, h + _h + 1) for _h, _w in product(range(m), repeat=2) if piece[_h][_w] != '-1'),
            None
        )
        if ans and (pos[1] > ans[1] or (pos[1] == ans[1] and pos[0] > ans[0])):
            return None
        ans = pos
        return True

def move(piece, c):
    _piece = list(
        map(
            list,
            map(
                lambda col: list(reversed(col)),
                zip(*piece)
            )
        )
    )
    main(_piece, c + 1)

while True:
    n, m = map(int, raw_input().split())
    if n == m == 0: break
    picture = [raw_input().split() for _ in range(n)]
    piece = [raw_input().split() for _ in range(m)]
    ans = None
    main(piece, 1)