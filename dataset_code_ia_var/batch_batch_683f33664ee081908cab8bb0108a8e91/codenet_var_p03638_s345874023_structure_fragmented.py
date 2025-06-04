def read_dimensions():
    return map(int, input().split())

def read_n():
    return int(input())

def read_a():
    return list(map(int, input().split()))

def generate_l_list(N, a):
    l = []
    for i in range(N):
        l += [i+1] * a[i]
    return l

def get_row(l_list, row_index, W):
    start = row_index * W
    end = (row_index + 1) * W
    return l_list[start:end]

def reverse_list_if_needed(p_list, should_reverse):
    if should_reverse:
        return p_list[::-1]
    return p_list

def print_row(p_list):
    for val in p_list:
        print(val, end=' ')
    print()

def process_grid(H, W, l_list):
    for i in range(H):
        row = get_row(l_list, i, W)
        row = reverse_list_if_needed(row, i % 2 == 1)
        print_row(row)

def main():
    H, W = read_dimensions()
    N = read_n()
    a = read_a()
    l_list = generate_l_list(N, a)
    process_grid(H, W, l_list)

main()