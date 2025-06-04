def get_input():
    return input("")

def initialize_flag():
    return [False for _ in range(4)]

def set_n_flag(ch, flag):
    if ch == 'N':
        flag[0] = True

def set_w_flag(ch, flag):
    if ch == 'W':
        flag[1] = True

def set_s_flag(ch, flag):
    if ch == 'S':
        flag[2] = True

def set_e_flag(ch, flag):
    if ch == 'E':
        flag[3] = True

def update_flags_with_char(ch, flag):
    set_n_flag(ch, flag)
    set_w_flag(ch, flag)
    set_s_flag(ch, flag)
    set_e_flag(ch, flag)

def update_flags(strbuf, flag):
    for i in range(len(strbuf)):
        update_flags_with_char(strbuf[i], flag)

def is_ns_invalid(flag):
    return (flag[0] and not flag[2]) or (flag[2] and not flag[0])

def is_we_invalid(flag):
    return (flag[1] and not flag[3]) or (flag[3] and not flag[1])

def print_result(flag):
    if is_ns_invalid(flag):
        print("No")
    elif is_we_invalid(flag):
        print("No")
    else:
        print("Yes")

def main23():
    strbuf = get_input()
    flag = initialize_flag()
    update_flags(strbuf, flag)
    print_result(flag)

if __name__ == '__main__':
    main23()