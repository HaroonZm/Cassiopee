def get_input():
    return input()

def convert_to_list(s):
    return list(s)

def get_first_char(lst):
    return lst[0]

def initialize_tmp():
    return 1

def initialize_ans():
    return "No"

def check_equal(a, b):
    return a == b

def increment_tmp(tmp):
    return tmp + 1

def check_tmp_equals_three(tmp):
    return tmp == 3

def set_ans_yes():
    return "Yes"

def set_ans_no():
    return "No"

def update_before_num(char):
    return char

def print_result(ans):
    print(ans)

def main_logic(N):
    ans = initialize_ans()
    before_num = get_first_char(N)
    tmp = initialize_tmp()
    for i in range(1, len(N)):
        if check_equal(N[i], before_num):
            tmp = increment_tmp(tmp)
            if check_tmp_equals_three(tmp):
                ans = set_ans_yes()
                break
        else:
            tmp = initialize_tmp()
            before_num = update_before_num(N[i])
    return ans

def main():
    s = get_input()
    N = convert_to_list(s)
    ans = main_logic(N)
    print_result(ans)

main()