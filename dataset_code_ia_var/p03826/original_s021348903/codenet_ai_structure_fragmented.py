def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_ints(strs):
    return list(map(int, strs))

def extract_values(values):
    a = values[0]
    b = values[1]
    c = values[2]
    d = values[3]
    return a, b, c, d

def calculate_area(x, y):
    return x * y

def compare_areas(area1, area2):
    if area1 > area2:
        return area1
    elif area2 >= area1:
        return area2

def print_result(res):
    print(res)

def main():
    raw_input = read_input()
    splitted = split_input(raw_input)
    numbers = convert_to_ints(splitted)
    a, b, c, d = extract_values(numbers)
    area1 = calculate_area(a, b)
    area2 = calculate_area(c, d)
    result = compare_areas(area1, area2)
    print_result(result)

main()