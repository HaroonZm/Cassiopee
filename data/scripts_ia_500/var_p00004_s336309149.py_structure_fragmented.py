#! /usr/bin/python3

def read_input():
    return input().split()

def convert_to_int_list(str_list):
    return list(map(int, str_list))

def compute_x(l):
    numerator = l[1]*l[5] - l[2]*l[4]
    denominator = l[1]*l[3] - l[0]*l[4]
    return numerator / denominator

def compute_y(l, x):
    numerator = l[2] - l[0]*x
    denominator = l[1]
    return numerator / denominator

def format_output(x, y):
    if x == 0:
        x = 0
    return "{0:.3f} {1:.3f}".format(x,y)

def main_loop():
    while True:
        try:
            input_str = read_input()
            l = convert_to_int_list(input_str)
            x = compute_x(l)
            y = compute_y(l, x)
            output = format_output(x, y)
            print(output)
        except:
            break

main_loop()