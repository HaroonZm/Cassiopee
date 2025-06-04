def read_input_n():
    return int(input())

def read_input_list():
    return list(int(a) for a in input().split())

def xor_two_numbers(a, b):
    return a ^ b

def xor_list_elements(lst):
    result = lst[0]
    for i in range(1, len(lst)):
        result = xor_two_numbers(result, lst[i])
    return result

def compute_c_element(b, ai):
    return xor_two_numbers(b, ai)

def compute_c_list(a, b):
    c_list = []
    for i in range(len(a)):
        c_list.append(compute_c_element(b, a[i]))
    return c_list

def convert_list_to_str(lst):
    return ' '.join(map(str, lst))

def main():
    n = read_input_n()
    a = read_input_list()
    b = xor_list_elements(a)
    c = compute_c_list(a, b)
    print(convert_list_to_str(c))

main()