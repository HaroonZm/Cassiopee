def read_input_line():
    return input()

def split_input_data(input_data):
    return input_data.split(' ')

def to_int_list(str_list):
    return [int(i) for i in str_list]

def initialize_sugoroku_final():
    return 1

def initialize_sugoroku_temp():
    return 1

def process_datum(datum, sugoroku_temp):
    if datum == 1:
        return sugoroku_temp + 1
    else:
        return 1

def update_sugoroku_final(sugoroku_final, sugoroku_temp):
    return max(sugoroku_final, sugoroku_temp)

def loop_over_data(list_data):
    sugoroku_final = initialize_sugoroku_final()
    sugoroku_temp = initialize_sugoroku_temp()
    for datum in list_data:
        if datum == 1:
            sugoroku_temp = process_datum(datum, sugoroku_temp)
        else:
            sugoroku_final = update_sugoroku_final(sugoroku_final, sugoroku_temp)
            sugoroku_temp = process_datum(datum, sugoroku_temp)
    sugoroku_final = update_sugoroku_final(sugoroku_final, sugoroku_temp)
    return sugoroku_final

def main():
    _ = read_input_line()
    input_data = read_input_line()
    str_data = split_input_data(input_data)
    list_data = to_int_list(str_data)
    result = loop_over_data(list_data)
    print(result)

main()