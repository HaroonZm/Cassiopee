def read_input():
    return input()

def parse_input(input_str):
    return map(int, input_str.split())

def assign_values(values):
    a, b, c, d = values
    return a, b, c, d

def diff(x, y):
    return abs(x - y)

def can_direct_reach(a, c, d):
    return diff(a, c) <= d

def can_via_b(a, b, c, d):
    return diff(a, b) <= d and diff(b, c) <= d

def decide(a, b, c, d):
    if can_direct_reach(a, c, d):
        return "Yes"
    elif can_via_b(a, b, c, d):
        return "Yes"
    else:
        return "No"

def output(result):
    print(result)

def main():
    input_str = read_input()
    values = parse_input(input_str)
    a, b, c, d = assign_values(values)
    result = decide(a, b, c, d)
    output(result)

main()