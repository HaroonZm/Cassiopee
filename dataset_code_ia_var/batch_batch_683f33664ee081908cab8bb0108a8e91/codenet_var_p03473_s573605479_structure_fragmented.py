def get_input():
    return input()

def convert_to_int(s):
    return int(s)

def calculate_difference(x):
    return 48 - x

def display_result(result):
    print(result)

def main():
    a = get_input()
    x = convert_to_int(a)
    result = calculate_difference(x)
    display_result(result)

main()