def main():
    white, black = [int(e) for e in input().split()]

    w = 100
    h = 50

    line = [0] * w
    field = [list(line) for _ in range(h)]

    white -= 1

    if white > 0:
        black -= 1

        for y in range(0, h, 2):
            for x in range(0, w, 2):
                field[y][x + 1] = field[y + 1][x] = field[y + 1][x + 1] = 1
                white -= 1
                if white == 0:
                    break
            if white == 0:
                break

    if black > 0:
        for y in range(24, h, 2):
            for x in range(0, w, 2):
                field[y][x] = 1
                black -= 1
                if black == 0:
                    break
            if black == 0:
                break

    print('{} {}'.format(h, w))
    for line in field:
        print(''.join(['#' if c else '.' for c in line]))

if __name__ == '__main__':
    main()