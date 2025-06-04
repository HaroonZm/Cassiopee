def get_input_count():
    return int(input())

def init_dictionary():
    return {}

def get_integer_input():
    return int(input())

def fill_dictionary(dic, N):
    for i in range(N):
        add_to_dictionary(dic, i+1, get_integer_input())

def add_to_dictionary(dic, key, value):
    dic[key] = value

def initialize_counter():
    return 0

def initialize_place():
    return 1

def check_in_dictionary(dic, place):
    return dic[place] in dic

def value_not_equal(dic, place):
    return dic[place] != place

def get_temp(dic, place):
    return dic[place]

def remove_key(dic, key):
    dic.pop(key)

def update_place(temp):
    return temp

def increment_counter(counter):
    return counter + 1

def set_counter_to_minus_one():
    return -1

def loop_condition(place):
    return place != 2

def print_result(counter):
    print(counter)

def main():
    N = get_input_count()
    dic = init_dictionary()
    fill_dictionary(dic, N)
    counter = initialize_counter()
    place = initialize_place()
    while loop_condition(place):
        if check_in_dictionary(dic, place) and value_not_equal(dic, place):
            temp = get_temp(dic, place)
            remove_key(dic, place)
            place = update_place(temp)
            counter = increment_counter(counter)
        else:
            counter = set_counter_to_minus_one()
            break
    print_result(counter)

main()