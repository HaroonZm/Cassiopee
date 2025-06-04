def read_input_count():
    return int(input())

def read_operation_and_argument():
    l = input()
    l += ' 1'
    return l.split()[:2]

def bit_mask(arg):
    return 1 << int(arg)

def new_bit():
    return {'data': 0}

def get_func(bit_obj):
    return (lambda arg: test_func(bit_obj, arg),
            lambda arg: set_func(bit_obj, arg),
            lambda arg: clear_func(bit_obj, arg),
            lambda arg: flip_func(bit_obj, arg),
            lambda arg: all_func(bit_obj, arg),
            lambda arg: any_func(bit_obj, arg),
            lambda arg: none_func(bit_obj, arg),
            lambda arg: count_func(bit_obj, arg),
            lambda arg: val_func(bit_obj, arg))

def process_operation(bit_obj, op, arg):
    funcs = get_func(bit_obj)
    func_index = int(op)
    funcs[func_index](arg)

def test_func(bit_obj, arg):
    print(int(bool(bit_obj['data'] & bit_mask(arg))))

def set_func(bit_obj, arg):
    bit_obj['data'] |= bit_mask(arg)

def clear_func(bit_obj, arg):
    bit_obj['data'] &= ~bit_mask(arg)

def flip_func(bit_obj, arg):
    bit_obj['data'] ^= bit_mask(arg)

def all_func(bit_obj, arg):
    print(int(count_ones(bit_obj['data']) == 64))

def any_func(bit_obj, arg):
    print(int(bit_obj['data'] != 0))

def none_func(bit_obj, arg):
    print(int(bit_obj['data'] == 0))

def count_func(bit_obj, arg):
    print(count_ones(bit_obj['data']))

def val_func(bit_obj, arg):
    print(bit_obj['data'])

def count_ones(data):
    return bin(data).count('1')

def main():
    b = new_bit()
    for _ in range(read_input_count()):
        op, arg = read_operation_and_argument()
        process_operation(b, op, arg)

main()