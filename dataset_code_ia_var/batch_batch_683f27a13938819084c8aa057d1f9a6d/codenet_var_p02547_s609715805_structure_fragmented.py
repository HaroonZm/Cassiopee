def read_input():
    return int(input())

def get_next_line():
    return input()

def split_line(line):
    return line.split()

def check_equal(a, b):
    return a == b

def increment_count(count):
    return count + 1

def reset_count():
    return 0

def is_three(count):
    return count == 3

def print_yes():
    print('Yes')

def print_no():
    print('No')

def do_exit():
    exit()

def process_pair(line, count):
    a, b = split_line(line)
    if check_equal(a, b):
        count = increment_count(count)
    else:
        count = reset_count()
    return count

def main_loop(s):
    count = 0
    for i in range(s):
        line = get_next_line()
        count = process_pair(line, count)
        if is_three(count):
            print_yes()
            do_exit()
    print_no()

def main():
    s = read_input()
    main_loop(s)

main()