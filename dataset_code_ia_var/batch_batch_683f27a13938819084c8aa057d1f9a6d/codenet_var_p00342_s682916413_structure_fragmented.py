import copy

def read_input_size():
    return int(input())

def read_input_data():
    return list(map(int, input().split()))

def sort_data(data):
    return sorted(data)

def copy_data(data):
    return copy.copy(data)

def pop_last(data):
    return data.pop()

def find_min_diff_pair(data):
    min_diff = float('inf')
    C = D = None
    for i in range(len(data) - 1):
        diff = data[i+1] - data[i]
        if diff < min_diff:
            min_diff = diff
            C = data[i+1]
            D = data[i]
    return C, D

def calc_ans(a, b, c, d):
    return (a + b) / (c - d)

def process_first_case(data):
    data1 = copy_data(data)
    A = pop_last(data1)
    B = pop_last(data1)
    n_1 = len(data1)
    C, D = find_min_diff_pair(data1)
    return calc_ans(A, B, C, D)

def find_and_remove_min_diff_pair(data):
    C, D = find_min_diff_pair(data)
    data.remove(C)
    data.remove(D)
    return C, D

def process_second_case(data):
    data2 = copy_data(data)
    C, D = find_and_remove_min_diff_pair(data2)
    A = pop_last(data2)
    B = pop_last(data2)
    return calc_ans(A, B, C, D)

def main():
    n = read_input_size()
    data = read_input_data()
    data_sorted = sort_data(data)
    ans_1 = process_first_case(data_sorted)
    ans_2 = process_second_case(data_sorted)
    print(max(ans_1, ans_2))

main()