def read_dimensions():
    return [int(i) for i in input().split(" ")]

def read_city_row():
    return input()

def initialize_timer():
    return -1000

def process_character(c, timer):
    if c == "c":
        timer = 0
        value = timer
    else:
        timer += 1
        value = timer
    return timer, value

def build_row(C):
    timer = initialize_timer()
    row = []
    for c in C:
        timer, value = process_character(c, timer)
        row.append(value)
    return row

def build_city(H):
    city = []
    for _ in range(H):
        C = read_city_row()
        row = build_row(C)
        city.append(row)
    return city

def replace_negative_values(city):
    for i in range(len(city)):
        for j in range(len(city[0])):
            city[i][j] = str(city[i][j]) if city[i][j] >= 0 else "-1"

def print_city(city):
    for row in city:
        print(" ".join(row))

def main():
    H, W = read_dimensions()
    city = build_city(H)
    replace_negative_values(city)
    print_city(city)

main()