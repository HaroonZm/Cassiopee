def create_table(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]

def read_rectangle():
    return [int(i) for i in input().split()]

def mark_rectangle(table, x, y, w, h):
    count = 0
    for i in range(x, x + w):
        for j in range(y, y + h):
            table[i][j] = 1
            count += 1
    return count

def toggle_rectangle(table, x, y, w, h):
    delta = 0
    for i in range(x, x + w):
        for j in range(y, y + h):
            if table[i][j] == 0:
                table[i][j] = 1
                delta += 1
            else:
                table[i][j] = 0
                delta -= 1
    return delta

def main():
    table = create_table(2001, 2001)
    x1, y1, w1, h1 = read_rectangle()
    x2, y2, w2, h2 = read_rectangle()
    ans = mark_rectangle(table, x1, y1, w1, h1)
    ans += toggle_rectangle(table, x2, y2, w2, h2)
    print(ans)

main()