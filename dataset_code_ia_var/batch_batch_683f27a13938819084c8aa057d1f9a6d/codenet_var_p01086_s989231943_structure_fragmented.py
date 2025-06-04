def get_input():
    return input()

def parse_int(s):
    return int(s)

def set_n():
    global n
    n = parse_int(get_input())
    return n

def get_n():
    return n

def create_w_list(size):
    return [0] * size

def append_w(w, value):
    w.append(value)

def input_and_length():
    return len(get_input())

def fill_w(n):
    global w
    w = []
    for i in range(n):
        word_length = input_and_length()
        append_w(w, word_length)

def get_w():
    global w
    return w

def advance_p(p):
    return p + 1

def decrement_l(l, amount):
    return l - amount

def get_w_elem(w, p):
    return w[p]

def l_equals_zero(l):
    return l == 0

def increment_i(i):
    return i + 1

def is_p_negative(p):
    return p < 0

def is_p_in_range(p, n):
    return p < n

def is_l_pos(l):
    return l > 0

def pos(p, l):
    global w
    if is_p_negative(p):
        return -1
    while is_l_pos(l) and is_p_in_range(p, n):
        l = decrement_l(l, get_w_elem(w, p))
        p = advance_p(p)
        if l_equals_zero(l):
            return p
    return -1

def multi_pos(i):
    return pos(pos(pos(pos(pos(i,5),7),5),7),7)

def check_and_print(n):
    for i in range(n):
        v = multi_pos(i)
        if v >= 0:
            print(increment_i(i))
            break

def main_loop():
    while set_n() > 0:
        fill_w(get_n())
        check_and_print(get_n())

main_loop()