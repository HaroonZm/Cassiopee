w, h, t = [int(x) for x in input().split()]
coords = []
for _ in range(int(input())):
    coords.append(tuple(map(int, input().split())))
rows = []
index = 0
while index < h:
    row = tuple([int(v) for v in input().split()])
    rows.append(row)
    index += 1
total = 0
def get_area_val(x, y):
    return rows[y][x]
for i in range(len(coords)):
    x, y = coords[i]
    total += get_area_val(x, y)
print(total)