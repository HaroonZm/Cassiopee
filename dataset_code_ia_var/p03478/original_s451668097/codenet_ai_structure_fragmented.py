def read_input():
    return input()

def split_input(user_input):
    return user_input.split()

def parse_int_list(str_list):
    return list(map(int, str_list))

def unpack_inputs(inputs):
    return inputs[0], inputs[1], inputs[2]

def int_range(n):
    return range(n + 1)

def num_to_str(num):
    return str(num)

def len_of_str(s):
    return len(s)

def char_at(s, idx):
    return s[idx]

def char_to_int(char):
    return int(char)

def sum_digits_of_num(num):
    s = num_to_str(num)
    total = 0
    for j in range(len_of_str(s)):
        total += char_to_int(char_at(s, j))
    return total

def is_in_range(val, lower, upper):
    return lower <= val <= upper

def add_to_count(cond, val, count):
    if cond:
        return count + val
    return count

def print_result(result):
    print(result)

def main():
    user_input = read_input()
    str_inputs = split_input(user_input)
    int_inputs = parse_int_list(str_inputs)
    n, a, b = unpack_inputs(int_inputs)
    count = 0
    for i in int_range(n):
        digit_sum = sum_digits_of_num(i)
        valid = is_in_range(digit_sum, a, b)
        count = add_to_count(valid, i, count)
    print_result(count)

main()