import sys

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 8)

def get_input():
    return sys.stdin.readline

def read_n(get_input_func):
    return int(get_input_func())

def read_array(get_input_func):
    return [int(x) for x in get_input_func().split()]

def compute_xor(arr):
    if not arr:
        return 0
    return xor_from_index(arr, 1, arr[0])

def xor_from_index(arr, idx, curr):
    if idx == len(arr):
        return curr
    return xor_from_index(arr, idx + 1, curr ^ arr[idx])

def compute_result_array(arr, val):
    return [element ^ val for element in arr]

def print_result_array(arr):
    for i in range(len(arr)):
        print_element(arr[i])
        print_end(i, len(arr))

def print_element(element):
    print(element, end="")

def print_end(i, length):
    if i < length - 1:
        print(" ", end="")
    else:
        print()

def main():
    set_recursion_limit()
    input_func = get_input()
    N = read_n(input_func)
    A = read_array(input_func)
    ans = compute_xor(A)
    result_arr = compute_result_array(A, ans)
    print_result_array(result_arr)

if __name__ == '__main__':
    main()