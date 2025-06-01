def get_input():
    return input()

def get_length(s):
    return len(s)

def get_char_at(s, index):
    return s[index]

def char_to_num(c):
    return ord(c)

def num_adjust(num):
    if is_num_ge_68(num):
        return subtract_3(num)
    else:
        return add_23(num)

def is_num_ge_68(num):
    return num >= 68

def subtract_3(num):
    return num - 3

def add_23(num):
    return num + 23

def num_to_char(num):
    return chr(num)

def print_char(c):
    print(c, end='')

def print_newline():
    print()

def main():
    ch = get_input()
    length = get_length(ch)
    for i in range(length):
        char = get_char_at(ch, i)
        num = char_to_num(char)
        adjusted_num = num_adjust(num)
        ans = num_to_char(adjusted_num)
        print_char(ans)
    print_newline()

main()