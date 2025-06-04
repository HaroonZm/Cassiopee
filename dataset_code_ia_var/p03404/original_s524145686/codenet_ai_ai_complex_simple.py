from functools import reduce
from operator import add, itemgetter
from itertools import product, islice, cycle

def main():
    W, B = map(int, input().split())
    w, h = 100, 50

    zero = 0
    row_proto = list(map(int, '0'*w))
    field = list(map(lambda _: list(row_proto), range(h)))

    W -= 1

    if W > 0:
        B -= 1
        cord_iter = ((y, x) for y, x in product(range(0, h, 2), range(0, w, 2)))
        for y, x in cord_iter:
            for dy, dx in ((0,1),(1,0),(1,1)):
                field[y+dy][x+dx] = 1
            W -= 1
            if not W:
                break

    if B > 0:
        blacker = islice(product(range(24, h, 2), range(0, w, 2)), B)
        for y, x in blacker:
            field[y][x] = 1

    print(f"{h} {w}")
    tr = str.maketrans('01', '.#')
    converter = lambda ln: ''.join(map(str, ln)).translate(tr)
    print('\n'.join(map(converter, field)))

if __name__ == '__main__':
    main()