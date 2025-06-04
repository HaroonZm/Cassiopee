def get_input_value():
    return int(input())

def get_list_size():
    return get_input_value()

def get_next_input():
    return get_input_value()

def initialize_list_with_input(size):
    lst = []
    for _ in range(size):
        lst.append(get_next_input())
    return lst

def initialize_single_element_list():
    return [1]

def initialize_bot():
    return 1

def initialize_flag():
    return True

def update_bot_value(current_bot, a):
    return a[current_bot - 1]

def is_bot_equal_to_two(bot):
    return bot == 2

def print_result(value):
    print(value)

def update_flag_on_success():
    return False

def process_loop(n, a):
    l = initialize_single_element_list()
    bot = initialize_bot()
    flag = initialize_flag()
    for i in range(n):
        bot = update_bot_value(bot, a)
        if is_bot_equal_to_two(bot):
            print_result(i + 1)
            flag = update_flag_on_success()
            break
    return flag

def main():
    n = get_list_size()
    a = initialize_list_with_input(n)
    flag = process_loop(n, a)
    if flag:
        print_result(-1)

main()