def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def extract_a(parts):
    return parts[0]

def extract_b(parts):
    return parts[1]

def extract_c(parts):
    return parts[2]

def convert_to_int(value):
    return int(value)

def convert_to_str(value):
    return str(value)

def process_operator(b, a, c):
    if b == "+":
        return add(a, c)
    else:
        return subtract(a, c)

def add(a, c):
    return a + c

def subtract(a, c):
    return a - c

def print_result(result):
    print(result)

def main():
    user_input = get_input()
    parts = split_input(user_input)
    a_raw = extract_a(parts)
    b = extract_b(parts)
    c_raw = extract_c(parts)
    a = convert_to_int(a_raw)
    c = convert_to_int(c_raw)
    result = process_operator(b, a, c)
    print_result(result)

main()