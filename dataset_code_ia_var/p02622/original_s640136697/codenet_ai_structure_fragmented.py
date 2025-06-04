def get_input():
    return input()

def to_list(s):
    return list(s)

def get_length(lst):
    return len(lst)

def get_element(lst, i):
    return lst[i]

def are_not_equal(a, b):
    return a != b

def increment(n):
    return n + 1

def compare_elements(s_list, t_list, i):
    s_elem = get_element(s_list, i)
    t_elem = get_element(t_list, i)
    return are_not_equal(s_elem, t_elem)

def compare_strings(s_list, t_list):
    length = get_length(s_list)
    ans = 0
    for i in range(length):
        if compare_elements(s_list, t_list, i):
            ans = increment(ans)
    return ans

def print_result(ans):
    print(ans)

def main():
    s_str = get_input()
    t_str = get_input()
    s_list = to_list(s_str)
    t_list = to_list(t_str)
    ans = compare_strings(s_list, t_list)
    print_result(ans)

main()