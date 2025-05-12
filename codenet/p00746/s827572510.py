move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def main(n):
    field = [(0, 0)]
    for _ in range(n - 1):
        ni, di = map(int, input().split())
        field.append((field[ni][0] + move[di][0], field[ni][1] + move[di][1]))
    minx = field[0][0]
    maxx = field[0][0]
    miny = field[0][1]
    maxy = field[0][1]
    for fx, fy in field:
        minx = min(minx, fx)
        maxx = max(maxx, fx)
        miny = min(miny, fy)
        maxy = max(maxy, fy)
    print(maxx - minx + 1, maxy - miny + 1)

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)