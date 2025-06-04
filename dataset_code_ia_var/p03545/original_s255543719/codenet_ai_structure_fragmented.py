def get_input():
    return input()

def parse_input(s):
    return list(map(int, s))

def assign_vars(lst):
    return lst[0], lst[1], lst[2], lst[3]

def sum_all(a, b, c, d):
    return a + b + c + d

def format_expression(a, b, c, d, ops):
    return f"{a}{ops[0]}{b}{ops[1]}{c}{ops[2]}{d}=7"

def check_pattern1(a, b, c, d):
    if sum_all(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['+','+','+']))
        exit()

def calc1(a, b, c, d):
    return a + b + c - d

def check_pattern2(a, b, c, d):
    if calc1(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['+','+','-']))
        exit()

def calc2(a, b, c, d):
    return a + b - c - d

def check_pattern3(a, b, c, d):
    if calc2(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['+','-','-']))
        exit()

def calc3(a, b, c, d):
    return a - b - c - d

def check_pattern4(a, b, c, d):
    if calc3(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['-','-','-']))
        exit()

def calc4(a, b, c, d):
    return a - b + c - d

def check_pattern5(a, b, c, d):
    if calc4(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['-','+','-']))
        exit()

def calc5(a, b, c, d):
    return a - b - c + d

def check_pattern6(a, b, c, d):
    if calc5(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['-','-','+']))
        exit()

def calc6(a, b, c, d):
    return a + b - c + d

def check_pattern7(a, b, c, d):
    if calc6(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['+','-','+']))
        exit()

def calc7(a, b, c, d):
    return a - b + c + d

def check_pattern8(a, b, c, d):
    if calc7(a, b, c, d) == 7:
        print(format_expression(a, b, c, d, ['-','+','+']))
        exit()

def check_all_patterns(a, b, c, d):
    check_pattern1(a, b, c, d)
    check_pattern2(a, b, c, d)
    check_pattern3(a, b, c, d)
    check_pattern4(a, b, c, d)
    check_pattern5(a, b, c, d)
    check_pattern6(a, b, c, d)
    check_pattern7(a, b, c, d)
    check_pattern8(a, b, c, d)

def main():
    s = get_input()
    lst = parse_input(s)
    a, b, c, d = assign_vars(lst)
    check_all_patterns(a, b, c, d)

main()