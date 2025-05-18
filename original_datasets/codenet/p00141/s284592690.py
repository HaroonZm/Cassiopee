class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, offset):
        self.x += offset[0]
        self.y += offset[1]

    def move_offset(self, offset, multiple=1):
        x = self.x + offset[0] * multiple
        y = self.y + offset[1] * multiple
        return Vector(x, y)

NOTHING = " "
EXIST = "#"
SENTINEL = "?"

MOVE = [
    [[-1, -1], [-1, +0], [-1, +1]],
    [[-1, +1], [-0, +1], [+1, +1]],
    [[+1, +1], [+1, +0], [+1, -1]],
    [[+1, -1], [+0, -1], [-1, -1]],
]

def create_area(size):
    area = [[SENTINEL] * 2 + [NOTHING] * size + [SENTINEL] * 2 for _ in range(size)]
    tmp = [[SENTINEL] * size + [SENTINEL] * 2 * 2]
    area = tmp * 2 + area + tmp * 2
    return area

def even_spiral_pattern(area, point):
    move_index = 0
    area[point.x][point.y] = EXIST

    while True:

        left, center, right = MOVE[move_index]
        end1, end2 = point.move_offset(left), point.move_offset(right)
        offset, offset2 = point.move_offset(center), point.move_offset(center, 2)

        if area[end1.x][end1.y] == EXIST or area[end2.x][end2.y] == EXIST:
            return area
        elif area[offset.x][offset.y] == NOTHING and area[offset2.x][offset2.y] != EXIST:
            point.move(center)
            area[point.x][point.y] = EXIST
        else:
            move_index += 1
            move_index %= 4

def odd_spiral_pattern(area, point):
    move_index = 0
    is_end = False
    area[point.x][point.y] = EXIST

    while True:

        left, center, right = MOVE[move_index]
        offset, offset2 = point.move_offset(center), point.move_offset(center, 2)

        if area[offset.x][offset.y] == NOTHING and area[offset2.x][offset2.y] != EXIST:
            point.move(center)
            area[point.x][point.y] = EXIST
            is_end = False
        else:
            if is_end:
                return area
            else:
                is_end = True

            move_index += 1
            move_index %= 4

def formater(area):
    output = ["".join(item).replace(SENTINEL, "") for item in result[2:-2]]
    output = "\n".join(output)
    return output

output = []

for _ in range(int(input())):
    size = int(input())

    area = create_area(size)
    point = Vector(size - 1 + 2, 2)

    if size % 2 == 0:
        result = even_spiral_pattern(area, point)
    else:
        result = odd_spiral_pattern(area, point)

    output.append(formater(result))

print("\n\n".join(output))