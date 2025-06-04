def get_input():
    return input()

def split_input(raw_input):
    return raw_input.split(",")

def map_to_str(split_list):
    return list(map(str, split_list))

def join_with_space(str_list):
    return " ".join(str_list)

def print_result(result):
    print(result)

def main():
    raw_input = get_input()
    splitted = split_input(raw_input)
    str_list = map_to_str(splitted)
    joined = join_with_space(str_list)
    print_result(joined)

main()