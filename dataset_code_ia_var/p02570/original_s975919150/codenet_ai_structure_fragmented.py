def get_input():
    return input()

def rstrip_line(line):
    return line.rstrip()

def split_line(line):
    return line.split(" ")

def get_first_element(lst):
    return lst[0]

def get_second_element(lst):
    return lst[1]

def get_third_element(lst):
    return lst[2]

def to_int(s):
    return int(s)

def calculate_possible(distance, time, speed):
    return time * speed >= distance

def print_yes():
    print("Yes")

def print_no():
    print("No")

def main():
    line = get_input()
    line = rstrip_line(line)
    parts = split_line(line)
    D = to_int(get_first_element(parts))
    T = to_int(get_second_element(parts))
    S = to_int(get_third_element(parts))
    if calculate_possible(D, T, S):
        print_yes()
    else:
        print_no()

main()