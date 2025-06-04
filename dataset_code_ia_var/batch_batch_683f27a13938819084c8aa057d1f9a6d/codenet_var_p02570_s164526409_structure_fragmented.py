def get_input():
    return input()

def split_input(input_str):
    return input_str.split()

def map_to_int(str_list):
    return list(map(int, str_list))

def unpack_values(values):
    return values[0], values[1], values[2]

def can_reach_destination(D, T, S):
    return T * S >= D

def print_yes():
    print("Yes")

def print_no():
    print("No")

def main():
    inp = get_input()
    splitted = split_input(inp)
    int_values = map_to_int(splitted)
    D, T, S = unpack_values(int_values)
    if can_reach_destination(D, T, S):
        print_yes()
    else:
        print_no()

main()