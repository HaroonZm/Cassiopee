def get_input():
    return input()

def to_int(value):
    return int(value)

def calculate_difference(total, subtrahend):
    return total - subtrahend

def print_result(result):
    print(result)

def main():
    total = get_total()
    subtrahend = get_subtrahend()
    result = calculate_difference(total, subtrahend)
    print_result(result)

def get_total():
    return 48

def get_subtrahend():
    return to_int(get_input())

main()