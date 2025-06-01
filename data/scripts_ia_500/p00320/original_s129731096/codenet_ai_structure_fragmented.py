def read_pair():
    return sorted(map(int, input().split()))

def initialize_list(size):
    return [[0, 0] for _ in range(size)]

def fill_list_with_input(lst):
    for i in range(len(lst)):
        lst[i] = read_pair()

def sort_list(lst):
    lst.sort()

def pairs_equal(lst, index1, index2):
    return lst[index1] == lst[index2]

def condition_to_print_yes(lst):
    return lst[0][0] == lst[2][0] and lst[0][1] == lst[4][0] and lst[2][1] == lst[4][1]

def check_pairs_and_print_result(lst):
    for i in range(0, len(lst), 2):
        if not pairs_equal(lst, i, i+1):
            print('no')
            return
    print(['no', 'yes'][condition_to_print_yes(lst)])

def main():
    c = initialize_list(6)
    fill_list_with_input(c)
    sort_list(c)
    check_pairs_and_print_result(c)

main()