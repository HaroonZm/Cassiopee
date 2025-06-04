def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_int_list(str_list):
    return list(map(int, str_list))

def calc_sum(int_list):
    return sum(int_list)

def is_win(total):
    return total < 22

def print_result(result):
    if result:
        print("win")
    else:
        print("bust")

def main():
    s = read_input()
    str_list = split_input(s)
    int_list = convert_to_int_list(str_list)
    total = calc_sum(int_list)
    result = is_win(total)
    print_result(result)

main()