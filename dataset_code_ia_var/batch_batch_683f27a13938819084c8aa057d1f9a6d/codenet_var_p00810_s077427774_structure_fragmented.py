def calculate_square_difference(a, b):
    return (a - b) ** 2

def calculate_difference(a, b):
    return a - b

def pair_elements(star, position):
    return zip(star, position)

def compute_squared_differences(star, position):
    return [calculate_square_difference(a, b) for a, b in pair_elements(star, position)]

def sum_of_list(lst):
    return sum(lst)

def sqrt_value(x):
    return x ** 0.5

def distance(star, position):
    sq_diffs = compute_squared_differences(star, position)
    total = sum_of_list(sq_diffs)
    return sqrt_value(total)

def compute_differences(star, position):
    return [calculate_difference(a, b) for a, b in pair_elements(star, position)]

def input_n():
    return int(input())

def input_star():
    return list(map(float, input().split()))

def read_stars(n):
    stars = []
    for _ in range(n):
        stars.append(input_star())
    return stars

def number_of_dimensions():
    return 3

def sum_coordinates(stars, i):
    return sum([s[i] for s in stars])

def compute_position(stars):
    dims = number_of_dimensions()
    n = len(stars)
    pos = []
    for i in range(dims):
        total = sum_coordinates(stars, i)
        pos.append(total / n)
    return pos

def adjust_move_rate(move_rate):
    return move_rate / 2

def find_max_distance_index(stars, position):
    max_dis = 0
    max_index = 0
    for j, star in enumerate(stars):
        dis = distance(star, position)
        if max_dis < dis:
            max_dis = dis
            max_index = j
    return max_index, max_dis

def update_position(position, diff, move_rate):
    return [position[i] + diff[i] * move_rate for i in range(number_of_dimensions())]

def format_distance(value):
    return format(value, ".5f")

def optimization_loop(stars, position):
    move_rate = 1
    max_iterations = 3000
    for i in range(max_iterations):
        if i % 100 == 0:
            move_rate = adjust_move_rate(move_rate)
        index, dis_max = find_max_distance_index(stars, position)
        diff = compute_differences(stars[index], position)
        position = update_position(position, diff, move_rate)
    return dis_max

def main_loop():
    while True:
        n = input_n()
        if n == 0:
            break
        stars = read_stars(n)
        position = compute_position(stars)
        dis_max = optimization_loop(stars, position)
        print(format_distance(dis_max))

main_loop()