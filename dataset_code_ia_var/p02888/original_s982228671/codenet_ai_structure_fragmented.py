import bisect

def get_input():
    return input()

def parse_int(s):
    return int(s)

def parse_int_list(s):
    return list(map(int, s.split()))

def sort_list(lst):
    return sorted(lst)

def get_length(lst):
    return len(lst)

def get_element(lst, idx):
    return lst[idx]

def get_slice(lst, start, end):
    return lst[start:end]

def bisect_left_in_list(lst, value):
    return bisect.bisect_left(lst, value)

def calculate_pairs(L, N):
    ans = 0
    i = 0
    while i < N - 2:
        a = get_element(L, i)
        ans += calculate_for_i(L, N, i, a)
        i += 1
    return ans

def calculate_for_i(L, N, i, a):
    res = 0
    j = i + 1
    while j < N - 1:
        b = get_element(L, j)
        idx = bisect_left_in_list(L, a + b)
        res += idx - j - 1
        j += 1
    return res

def print_result(res):
    print(res)

def main():
    N = parse_int(get_input())
    L = parse_int_list(get_input())
    L = sort_list(L)
    ans = calculate_pairs(L, N)
    print_result(ans)

main()