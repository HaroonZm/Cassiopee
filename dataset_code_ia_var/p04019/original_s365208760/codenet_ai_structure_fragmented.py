def get_input():
    return input()

def to_list(s):
    return list(s)

def contains_e(s_list):
    return 'E' in s_list

def contains_w(s_list):
    return 'W' in s_list

def contains_n(s_list):
    return 'N' in s_list

def contains_s(s_list):
    return 'S' in s_list

def check_e_w(s_list):
    if contains_e(s_list):
        if contains_w(s_list):
            return 0
        else:
            return 1
    return 0

def check_w_e(s_list):
    if contains_w(s_list):
        if contains_e(s_list):
            return 0
        else:
            return 1
    return 0

def check_n_s(s_list):
    if contains_n(s_list):
        if contains_s(s_list):
            return 0
        else:
            return 1
    return 0

def check_s_n(s_list):
    if contains_s(s_list):
        if contains_n(s_list):
            return 0
        else:
            return 1
    return 0

def final_check(s_list):
    chk = 0
    chk += check_e_w(s_list)
    chk += check_w_e(s_list)
    chk += check_n_s(s_list)
    chk += check_s_n(s_list)
    if chk == 0:
        return 0
    else:
        return 1

def print_result(chk):
    if chk == 0:
        print('Yes')
    else:
        print('No')

def main():
    s = get_input()
    s_list = to_list(s)
    chk = final_check(s_list)
    print_result(chk)

main()