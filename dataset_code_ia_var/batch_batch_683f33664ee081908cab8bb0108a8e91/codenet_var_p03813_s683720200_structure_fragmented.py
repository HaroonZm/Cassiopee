def read_input():
    return input()

def to_int(s):
    return int(s)

def is_less_than_1200(x):
    return x < 1200

def get_abc():
    return 'ABC'

def get_arc():
    return 'ARC'

def select_string(x):
    if is_less_than_1200(x):
        return get_abc()
    else:
        return get_arc()

def main():
    s = read_input()
    x = to_int(s)
    result = select_string(x)
    print(result)

main()