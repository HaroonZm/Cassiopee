def read_int():
    return int(input())

def read_input_list():
    return input().split()

def convert_to_int_list(str_list):
    return [int(i) for i in str_list]

def init_data_dict():
    return {}

def update_data_dict(data, num):
    if num_in_dict(data, num):
        increment_data_value(data, num)
    else:
        set_data_value(data, num, 1)

def num_in_dict(data, num):
    return num in data

def increment_data_value(data, num):
    data[num] += 1

def set_data_value(data, num, value):
    data[num] = value

def fill_data_dict(a):
    data = init_data_dict()
    for num in a:
        update_data_dict(data, num)
    return data

def calculate_ans(data):
    ans = 0
    for key in get_keys(data):
        ans = add_to_ans(ans, process_key(data, key))
    return ans

def get_keys(data):
    return data.keys()

def process_key(data, key):
    if less_than_count(key, data[key]):
        return value_to_add(data[key], key)
    else:
        return value_to_add(data[key], key)
        
def less_than_count(key, count):
    return count < key

def value_to_add(count, key):
    if count < key:
        return count
    else:
        return count - key

def print_ans(ans):
    print(ans)

def main():
    N = read_int()
    str_list = read_input_list()
    a = convert_to_int_list(str_list)
    data = fill_data_dict(a)
    ans = calculate_ans(data)
    print_ans(ans)

main()