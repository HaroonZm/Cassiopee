def read_input():
    return input()

def convert_to_int(s):
    return int(s)

def is_less_than_1200(n):
    return n < 1200

def get_label(flag):
    if flag:
        return "ABC"
    else:
        return "ARC"

def print_label(label):
    print(label)

def main():
    s = read_input()
    n = convert_to_int(s)
    flag = is_less_than_1200(n)
    label = get_label(flag)
    print_label(label)

main()