def read_input():
    return input()

def to_list(s):
    return list(s)

def to_int(char):
    return int(char)

def map_to_int(lst):
    return list(map(to_int, lst))

def sum_list(lst):
    return sum(lst)

def print_result(result):
    print(result)

def main():
    s = read_input()
    s_list = to_list(s)
    int_list = map_to_int(s_list)
    total = sum_list(int_list)
    print_result(total)

main()