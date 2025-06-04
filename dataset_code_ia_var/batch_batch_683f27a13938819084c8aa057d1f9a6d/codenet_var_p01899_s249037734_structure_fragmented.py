def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_int_list(str_list):
    return list(map(int, str_list))

def get_n_and_d(str_list):
    return int(str_list[0]), int(str_list[1])

def get_lst_from_input():
    return convert_to_int_list(split_input(read_input()))

def filter_diff_positive(lst, d):
    return [x - d for x in lst if x - d >= 0]

def sum_list(lst):
    return sum(lst)

def print_result(total):
    if total:
        print(total)
    else:
        print("kusoge")

def main():
    n_d_input = read_input()
    n_d_list = split_input(n_d_input)
    n, d = get_n_and_d(n_d_list)
    lst = get_lst_from_input()
    diff_list = filter_diff_positive(lst, d)
    total = sum_list(diff_list)
    print_result(total)

main()