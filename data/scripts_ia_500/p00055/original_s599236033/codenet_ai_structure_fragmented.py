def read_input():
    return raw_input()

def convert_to_float(value):
    return float(value)

def initialize_values(value):
    a = s = value
    return a, s

def is_even(number):
    return number % 2 == 0

def process_even(a):
    a *= 2.0
    return a

def process_odd(a):
    a /= 3.0
    return a

def update_sum(s, a):
    s += a
    return s

def process_iteration(a, s, i):
    if is_even(i):
        a = process_even(a)
    else:
        a = process_odd(a)
    s = update_sum(s, a)
    return a, s

def print_result(s):
    print s

def main_loop():
    while 1:
        try:
            raw_value = read_input()
            value = convert_to_float(raw_value)
            a, s = initialize_values(value)
            for i in range(2,11):
                a, s = process_iteration(a, s, i)
            print_result(s)
        except:
            break

main_loop()