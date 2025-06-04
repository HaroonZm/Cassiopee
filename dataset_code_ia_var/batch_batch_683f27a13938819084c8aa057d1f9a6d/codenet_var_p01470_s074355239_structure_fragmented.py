m = 10000000019
x = 0

def mod_value(val):
    return (val % m + m) % m

def pow_base(x, a):
    ret = 1
    while a:
        if is_odd(a):
            ret = mod_mult(x, ret)
        x = mod_mult(x, x)
        a = shift_right(a)
    return ret

def is_odd(a):
    return a & 1

def shift_right(a):
    return a >> 1

def mod_mult(a, b):
    return mod_value(a * b)

def add_mod(x, y):
    return (x + y) % m

def sub_mod(x, y):
    return (x - y) % m

def process_op(x, o, y):
    if is_op_add(o):
        return add_mod(x, y)
    elif is_op_sub(o):
        return sub_mod(x, y)
    elif is_op_mult(o):
        return mod_mult(x, y)
    else:
        return div_mod(x, y)

def is_op_add(o):
    return o == 1

def is_op_sub(o):
    return o == 2

def is_op_mult(o):
    return o == 3

def div_mod(x, y):
    return mod_mult(x, pow_base(y, m - 2))

def read_num():
    return int(input())

def read_two_ints():
    return map(int, input().split())

def main():
    global x
    t = read_num()
    for _ in range(loop_range(t)):
        o, y = read_two_ints()
        x = process_op(x, o, y)
    print_result(x)

def print_result(val):
    if less_than(val, one_shift_31()):
        print(val)
    else:
        print(val - m)

def less_than(a, b):
    return a < b

def one_shift_31():
    return 1 << 31

def loop_range(t):
    return t

main()