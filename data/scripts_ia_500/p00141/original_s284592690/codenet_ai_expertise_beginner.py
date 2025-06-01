class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, offset):
        self.x = self.x + offset[0]
        self.y = self.y + offset[1]

    def move_offset(self, offset, multiple=1):
        new_x = self.x + offset[0] * multiple
        new_y = self.y + offset[1] * multiple
        return Vector(new_x, new_y)

NOTHING = " "
EXIST = "#"
SENTINEL = "?"

MOVE = [
    [[-1, -1], [-1, 0], [-1, 1]],
    [[-1, 1], [0, 1], [1, 1]],
    [[1, 1], [1, 0], [1, -1]],
    [[1, -1], [0, -1], [-1, -1]],
]

def create_area(size):
    area = []
    for _ in range(size):
        row = [SENTINEL]*2 + [NOTHING]*size + [SENTINEL]*2
        area.append(row)
    border_row = [SENTINEL]*(size + 4)
    area = border_row*2 + area + border_row*2
    return area

def even_spiral_pattern(area, point):
    move_index = 0
    area[point.x][point.y] = EXIST
    while True:
        left = MOVE[move_index][0]
        center = MOVE[move_index][1]
        right = MOVE[move_index][2]
        end1 = point.move_offset(left)
        end2 = point.move_offset(right)
        offset = point.move_offset(center)
        offset2 = point.move_offset(center, 2)
        if area[end1.x][end1.y] == EXIST or area[end2.x][end2.y] == EXIST:
            return area
        elif area[offset.x][offset.y] == NOTHING and area[offset2.x][offset2.y] != EXIST:
            point.move(center)
            area[point.x][point.y] = EXIST
        else:
            move_index = (move_index + 1) % 4

def odd_spiral_pattern(area, point):
    move_index = 0
    is_end = False
    area[point.x][point.y] = EXIST
    while True:
        left = MOVE[move_index][0]
        center = MOVE[move_index][1]
        right = MOVE[move_index][2]
        offset = point.move_offset(center)
        offset2 = point.move_offset(center, 2)
        if area[offset.x][offset.y] == NOTHING and area[offset2.x][offset2.y] != EXIST:
            point.move(center)
            area[point.x][point.y] = EXIST
            is_end = False
        else:
            if is_end:
                return area
            else:
                is_end = True
            move_index = (move_index + 1) % 4

def formater(area):
    lines = []
    for line in area[2:-2]:
        s = "".join(line).replace(SENTINEL, "")
        lines.append(s)
    return "\n".join(lines)

output = []
t = int(input())
for _ in range(t):
    size = int(input())
    area = create_area(size)
    point = Vector(size - 1 + 2, 2)
    if size % 2 == 0:
        result = even_spiral_pattern(area, point)
    else:
        result = odd_spiral_pattern(area, point)
    output.append(formater(result))

print("\n\n".join(output))