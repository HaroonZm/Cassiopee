def read_input():
    return input()

def parse_int(string):
    return int(string)

def split_string(string):
    return string.split()

def map_to_int(lst):
    return list(map(int, lst))

def remove_first_element(lst):
    del lst[0]
    return lst

def inp2list():
    tmp = read_input()
    tmp = split_string(tmp)
    tmp = map_to_int(tmp)
    tmp = remove_first_element(tmp)
    return tmp

def create_false_list(n):
    return [False for _ in range(n)]

def count_in_list(lst, value):
    return lst.count(value)

def set_true(lst, index):
    lst[index] = True

def list_count_true(lst):
    return lst.count(True)

def should_set_true(i, A, B):
    no_in_A = (count_in_list(A, i) == 0)
    in_B = (count_in_list(B, i) != 0)
    return no_in_A or in_B

def process_C(C, A, B, R):
    for i in C:
        if should_set_true(i, A, B):
            set_true(R, i-1)

def main():
    N_line = read_input()
    N = parse_int(N_line)
    A = inp2list()
    B = inp2list()
    C = inp2list()
    R = create_false_list(N)
    process_C(C, A, B, R)
    print(list_count_true(R))

main()