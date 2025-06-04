def read_input():
    return int(input())

def read_line():
    return input()

def split_line(line):
    return line.split(" ")

def str_list_to_int_list(str_list):
    return [int(x) for x in str_list]

def initialize_max():
    return 0

def initialize_count():
    return 0

def is_one(value):
    return value == 1

def increase(value):
    return value + 1

def update_count_on_one(count):
    return increase(count)

def reset_count():
    return 0

def update_max(maxVal, count):
    if maxVal < count:
        return count
    return maxVal

def process_array(A, N):
    maxVal = initialize_max()
    count = initialize_count()
    for i in range(N):
        if is_one(A[i]):
            count = update_count_on_one(count)
            maxVal = update_max(maxVal, count)
        else:
            count = reset_count()
    return maxVal

def add_one(val):
    return val + 1

def main():
    N = read_input()
    line = read_line()
    split = split_line(line)
    A = str_list_to_int_list(split)
    maxVal = process_array(A, N)
    res = add_one(maxVal)
    print(res)

main()