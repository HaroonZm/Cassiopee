class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def set_x_y(obj, x, y):
    obj.x = x
    obj.y = y

def vector_move(vector_obj, offset):
    apply_move_on_x(vector_obj, offset[0])
    apply_move_on_y(vector_obj, offset[1])

def apply_move_on_x(vector_obj, delta_x):
    vector_obj.x += delta_x

def apply_move_on_y(vector_obj, delta_y):
    vector_obj.y += delta_y

def vector_move_offset(vector_obj, offset, multiple=1):
    x = calculate_x_with_offset(vector_obj, offset, multiple)
    y = calculate_y_with_offset(vector_obj, offset, multiple)
    return build_vector_from_coords(x, y)

def calculate_x_with_offset(vector_obj, offset, multiple):
    return vector_obj.x + offset[0] * multiple

def calculate_y_with_offset(vector_obj, offset, multiple):
    return vector_obj.y + offset[1] * multiple

def build_vector_from_coords(x, y):
    return Vector(x, y)

NOTHING = " "
EXIST = "#"
SENTINEL = "?"

def get_move():
    return [
        [[-1, -1], [-1, +0], [-1, +1]],
        [[-1, +1], [-0, +1], [+1, +1]],
        [[+1, +1], [+1, +0], [+1, -1]],
        [[+1, -1], [+0, -1], [-1, -1]],
    ]

def create_area(size):
    row = make_row(size)
    area = build_main_area(size, row)
    tmp = make_tmp_row(size)
    area = add_tmp_to_area(tmp, area)
    return area

def make_row(size):
    return [SENTINEL] * 2 + [NOTHING] * size + [SENTINEL] * 2

def build_main_area(size, row):
    return [row[:] for _ in range(size)]

def make_tmp_row(size):
    return [[SENTINEL] * (size + 4)]

def add_tmp_to_area(tmp, area):
    return tmp * 2 + area + tmp * 2

def even_spiral_pattern(area, point):
    move_index = initialize_move_index()
    mark_exist(area, point)
    while True:
        if process_even_spiral(area, point, move_index):
            return area
        move_index = update_move_index(move_index)

def initialize_move_index():
    return 0

def mark_exist(area, point):
    area[point.x][point.y] = EXIST

def process_even_spiral(area, point, move_index):
    MOVE = get_move()
    left, center, right = unpack_move(MOVE, move_index)
    end1, end2 = calculate_endpoints(point, left, right)
    offset, offset2 = calculate_offsets(point, center)
    if is_path_blocked(area, end1, end2):
        return True
    elif is_path_clear(area, offset, offset2):
        move_point(point, center)
        mark_exist(area, point)
    else:
        point.temp_move_index = move_index  # For reference, does not affect logic.
    return False

def unpack_move(MOVE, move_index):
    return MOVE[move_index][0], MOVE[move_index][1], MOVE[move_index][2]

def calculate_endpoints(point, left, right):
    end1 = vector_move_offset(point, left)
    end2 = vector_move_offset(point, right)
    return end1, end2

def calculate_offsets(point, center):
    offset = vector_move_offset(point, center)
    offset2 = vector_move_offset(point, center, 2)
    return offset, offset2

def is_path_blocked(area, end1, end2):
    return area[end1.x][end1.y] == EXIST or area[end2.x][end2.y] == EXIST

def is_path_clear(area, offset, offset2):
    return area[offset.x][offset.y] == NOTHING and area[offset2.x][offset2.y] != EXIST

def move_point(point, center):
    vector_move(point, center)

def update_move_index(move_index):
    move_index += 1
    move_index %= 4
    return move_index

def odd_spiral_pattern(area, point):
    move_index = initialize_move_index()
    is_end = initialize_is_end()
    mark_exist(area, point)
    while True:
        finished, is_end, move_index = process_odd_spiral(area, point, move_index, is_end)
        if finished:
            return area

def initialize_is_end():
    return False

def process_odd_spiral(area, point, move_index, is_end):
    MOVE = get_move()
    left, center, right = unpack_move(MOVE, move_index)
    offset, offset2 = calculate_offsets(point, center)
    if is_path_clear(area, offset, offset2):
        move_point(point, center)
        mark_exist(area, point)
        return False, False, move_index
    else:
        if is_end:
            return True, is_end, move_index
        else:
            is_end = True
            move_index = update_move_index(move_index)
            return False, is_end, move_index

def formater(area):
    content = remove_sentinals(area)
    joined = join_rows(content)
    formatted = join_lines(joined)
    return formatted

def remove_sentinals(area):
    return [item for item in area[2:-2]]

def join_rows(content):
    return ["".join(item).replace(SENTINEL, "") for item in content]

def join_lines(joined):
    return "\n".join(joined)

def main_loop():
    output = []
    testcases = get_testcase_count()
    for _ in range(testcases):
        size = get_size_input()
        area = create_area(size)
        point = create_initial_vector(size)
        if is_even(size):
            result = even_spiral_pattern(area, point)
        else:
            result = odd_spiral_pattern(area, point)
        formatted_result = formater(result)
        store_output(output, formatted_result)
    print_all_outputs(output)

def get_testcase_count():
    return int(input())

def get_size_input():
    return int(input())

def create_initial_vector(size):
    return Vector(size - 1 + 2, 2)

def is_even(size):
    return size % 2 == 0

def store_output(output, result):
    output.append(result)

def print_all_outputs(output):
    txt = concat_output(output)
    print(txt)

def concat_output(output):
    return "\n\n".join(output)

main_loop()