Masu = []
for i in range(10):
    Masu.append([0,0,0,0,0,0,0,0,0,0])
kosu = 0
komax = 0
while True:
    try:
        x, y, s = map(int, input().split(","))
        if s == 1:
            for j in range(3):
                _x = y + 1 - j
                _y = x
                if 0 <= _x <= 9 and 0 <= _y <= 9:
                    Masu[_x][_y] += 1
            _x = y
            _y = x - 1
            if 0 <= _x <= 9 and 0 <= _y <= 9:
                Masu[_x][_y] += 1
            _x = y
            _y = x + 1
            if 0 <= _x <= 9 and 0 <= _y <= 9:
                Masu[_x][_y] += 1
        elif s == 2:
            for k in range(3):
                for l in range(3):
                    _x = y + 1 - k
                    _y = x + 1 - l
                    if 0 <= _x <= 9 and 0 <= _y <= 9:
                        Masu[_x][_y] += 1
        elif s == 3:
            for k in range(3):
                for l in range(3):
                    _x = y + 1 - k
                    _y = x + 1 - l
                    if 0 <= _x <= 9 and 0 <= _y <= 9:
                        Masu[_x][_y] += 1
            _x = y - 2
            _y = x
            if 0 <= _x <= 9 and 0 <= _y <= 9:
                Masu[_x][_y] += 1
            _x = y + 2
            _y = x
            if 0 <= _x <= 9 and 0 <= _y <= 9:
                Masu[_x][_y] += 1
            _x = y
            _y = x + 2
            if 0 <= _x <= 9 and 0 <= _y <= 9:
                Masu[_x][_y] += 1
            _x = y
            _y = x - 2
            if 0 <= _x <= 9 and 0 <= _y <= 9:
                Masu[_x][_y] += 1
    except (EOFError, ValueError):
        for i in range(10):
            kosu += Masu[i].count(0)
        for j in range(10):
            if komax < max(Masu[j]):
                komax = max(Masu[j])
        print(kosu)
        print(komax)
        break