def get_input():
    return input()

def parse_input(input_str):
    return list(map(int, input_str.split()))

def sort_pair(a, b):
    return sorted([a, b])

def create_range_list(start, end):
    return [i for i in range(start, end)]

def check_in_range(value, range_list):
    return value in range_list

def print_yes():
    print("Yes")

def print_no():
    print("No")

def main():
    user_input = get_input()
    values = parse_input(user_input)
    a, b, c = values[0], values[1], values[2]
    sorted_pair = sort_pair(a, b)
    start = sorted_pair[0]
    end = sorted_pair[1]
    range_list = create_range_list(start, end)
    if check_in_range(c, range_list):
        print_yes()
    else:
        print_no()

main()