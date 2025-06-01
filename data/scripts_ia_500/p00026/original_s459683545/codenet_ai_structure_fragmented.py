Masu = []

def init_masu():
    for _ in range(10):
        Masu.append([0]*10)

def is_out_of_bounds(x,y):
    if x < 0 or y < 0 or x > 9 or y > 9:
        return True
    return False

def increment_cell(x,y):
    if not is_out_of_bounds(x,y):
        Masu[y][x] += 1

def process_s1(x,y):
    def increment_three_vertical(y,x):
        for j in range(3):
            increment_cell(x,y+1-j)
    def increment_sides(y,x):
        increment_cell(x-1,y)
        increment_cell(x+1,y)
    increment_three_vertical(y,x)
    increment_sides(y,x)

def process_s2(x,y):
    def increment_square(y,x):
        for k in range(3):
            for l in range(3):
                increment_cell(x+1-l,y+1-k)
    increment_square(y,x)

def process_s3(x,y):
    def increment_square(y,x):
        for k in range(3):
            for l in range(3):
                increment_cell(x+1-l,y+1-k)
    def increment_cross(y,x):
        increment_cell(x,y-2)
        increment_cell(x,y+2)
        increment_cell(x+2,y)
        increment_cell(x-2,y)
    increment_square(y,x)
    increment_cross(y,x)

def count_zeros():
    count = 0
    for row in Masu:
        count += row.count(0)
    return count

def find_max():
    current_max = 0
    for row in Masu:
        row_max = max(row)
        if row_max > current_max:
            current_max = row_max
    return current_max

def main_loop():
    init_masu()
    while True:
        try:
            line = input()
            x,y,s = parse_input(line)
            handle_s_value(x,y,s)
        except (EOFError, ValueError):
            total_zeros = count_zeros()
            max_value = find_max()
            print(total_zeros)
            print(max_value)
            break

def parse_input(line):
    parts = line.split(",")
    if len(parts) != 3:
        raise ValueError
    return map(int, parts)

def handle_s_value(x,y,s):
    if s == 1:
        process_s1(x,y)
    elif s == 2:
        process_s2(x,y)
    elif s == 3:
        process_s3(x,y)

main_loop()