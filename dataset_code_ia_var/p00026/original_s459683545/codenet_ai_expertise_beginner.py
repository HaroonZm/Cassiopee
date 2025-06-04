Masu = []
for i in range(10):
    Masu.append([0] * 10)

def access(x, y):
    if x < 0 or y < 0 or x > 9 or y > 9:
        return
    Masu[y][x] = Masu[y][x] + 1

kosu = 0
komax = 0

while True:
    try:
        user_input = input()
        values = user_input.split(",")
        x = int(values[0])
        y = int(values[1])
        s = int(values[2])
        if s == 1:
            for j in range(3):
                access(y + 1 - j, x)
            access(y, x - 1)
            access(y, x + 1)
        elif s == 2:
            for k in range(3):
                for l in range(3):
                    access(y + 1 - k, x + 1 - l)
        elif s == 3:
            for k in range(3):
                for l in range(3):
                    access(y + 1 - k, x + 1 - l)
            access(y - 2, x)
            access(y + 2, x)
            access(y, x + 2)
            access(y, x - 2)
    except (EOFError, ValueError, IndexError):
        for i in range(10):
            for j in range(10):
                if Masu[i][j] == 0:
                    kosu = kosu + 1
        for i in range(10):
            row_max = max(Masu[i])
            if komax < row_max:
                komax = row_max
        print(kosu)
        print(komax)
        break