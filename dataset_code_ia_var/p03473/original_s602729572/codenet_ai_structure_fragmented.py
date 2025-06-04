def get_input():
    return input()

def to_int(s):
    return int(s)

def calculate_difference(a, b):
    return a - b

def print_result(result):
    print(result)

def main():
    m_str = get_input()
    m = to_int(m_str)
    base = 48
    diff = calculate_difference(base, m)
    print_result(diff)

main()