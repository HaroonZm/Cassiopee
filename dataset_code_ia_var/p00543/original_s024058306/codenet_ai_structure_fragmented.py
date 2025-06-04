def read_n_and_m():
    n, m = map(int, input().split())
    return n, m

def init_dict(n):
    d = {}
    for i in range(n):
        d[i+1] = int(input())
    return d

def perform_swaps_for_one_k(d, n, k):
    for j in range(n):
        i = j+1
        if i == n:
            break
        if d[i] % k > d[i+1] % k:
            swap_elements(d, i, i+1)

def swap_elements(d, idx1, idx2):
    temp = d[idx1]
    d[idx1] = d[idx2]
    d[idx2] = temp

def process_all_m(d, n, m):
    for l in range(m):
        k = l + 1
        perform_swaps_for_one_k(d, n, k)

def print_dict_in_order(d, n):
    for i in range(n):
        print(d[i+1])

def main():
    n, m = read_n_and_m()
    d = init_dict(n)
    process_all_m(d, n, m)
    print_dict_in_order(d, n)

main()