def get_input():
    return input().rstrip()

def define_weather_list():
    return ['Sunny', 'Cloudy', 'Rainy']

def get_length_of_list(lst):
    return len(lst)

def get_element_at_index(lst, idx):
    return lst[idx]

def compare_values(val1, val2):
    return val1 == val2

def increment_index(idx):
    return idx + 1

def modulo_operation(val, mod):
    return val % mod

def print_value(val):
    print(val)

def main():
    Ss = get_input()
    Ts = define_weather_list()
    length = get_length_of_list(Ts)
    for i in range(length):
        current_element = get_element_at_index(Ts, i)
        if compare_values(current_element, Ss):
            next_index_base = increment_index(i)
            next_index = modulo_operation(next_index_base, length)
            value_to_print = get_element_at_index(Ts, next_index)
            print_value(value_to_print)

main()