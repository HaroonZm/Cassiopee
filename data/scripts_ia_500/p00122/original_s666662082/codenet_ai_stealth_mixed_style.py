def search(table, x, y, depth, max_depth):
    moves = [(-2,-1),(-2,0),(-2,1),(-1,-2),(0,-2),(1,-2),(2,-1),(2,0),(2,1),(-1,2),(0,2),(1,2)]
    if depth == max_depth:
        return True
    if not(0 <= x < 10 and 0 <= y < 10):
        return False
    if depth >= 0:
        if table[x][y][depth] == 0:
            return False
    for dx, dy in moves:
        if search(table, x+dx, y+dy, depth+1, max_depth):
            return True
    return False

def main():
    while True:
        try:
            px, py = map(int, input().split())
        except EOFError:
            break
        if (px, py) == (0, 0):
            break
        table = []
        for _ in range(10):
            row = []
            for __ in range(10):
                row.append([0]*10)
            table.append(row)

        n = int(input())
        N = list(map(int, input().split()))
        for i in range(0, len(N), 2):
            x = N[i]
            y = N[i+1]
            prx = x-1 if x > 0 else 0
            pry = y-1 if y > 0 else 0
            pox = x+1 if x < 9 else 9
            poy = y+1 if y < 9 else 9
            d = i//2
            positions = [
                (prx, pry), (prx, y), (prx, poy),
                (x, pry), (x, y), (x, poy),
                (pox, pry), (pox, y), (pox, poy)
            ]
            for (xx, yy) in positions:
                table[xx][yy][d] = 1

        if search(table, px, py, -1, n):
            print("OK")
        else:
            print("NA")

if __name__ == "__main__":
    main()