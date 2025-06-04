def read_input():
    return int(input()), [int(x) for x in input().split()]

def create_count_dict():
    return {}

def update_dict(d, k):
    try:
        d[k] += 1
    except KeyError:
        d[k] = 1

def process_series(series, n, even_dict, odd_dict):
    for i in range(n):
        k = series[i]
        if i % 2 == 0:
            update_dict(even_dict, k)
        else:
            update_dict(odd_dict, k)

def extract_counts(count_dict):
    result = []
    for key in count_dict:
        result.append([count_dict[key], key])
    return result

def sort_counts(vals):
    vals.sort(reverse=True)
    return vals

def get_single_case_counts(odd_vals, even_vals):
    return odd_vals[0][0], even_vals[0][0], odd_vals[0][1], even_vals[0][1]

def get_multi_case_counts(odd_vals, even_vals):
    a = odd_vals[0][0]
    b = odd_vals[1][0]
    c = even_vals[0][0]
    d = even_vals[1][0]
    return a, b, c, d

def single_case(n, odd_vals, even_vals):
    a, b, odd_key, even_key = get_single_case_counts(odd_vals, even_vals)
    if odd_key != even_key:
        print(n - a - b)
    else:
        print(n // 2)

def multi_case(n, odd_vals, even_vals):
    if odd_vals[0][1] != even_vals[0][1]:
        print(n - odd_vals[0][0] - even_vals[0][0])
    else:
        a, b, c, d = get_multi_case_counts(odd_vals, even_vals)
        print(min(n - a - d, n - b - c))

def mixed_case(n, odd_vals, even_vals):
    a = odd_vals[0][0]
    b = even_vals[0][0]
    if len(odd_vals) == 1:
        c = even_vals[1][0]
    else:
        c = odd_vals[1][0]
    if odd_vals[0][1] != even_vals[0][1]:
        print(n - a - b)
    else:
        print(n - a - c)

def main():
    n, series = read_input()
    odd_dict = create_count_dict()
    even_dict = create_count_dict()
    process_series(series, n, even_dict, odd_dict)
    odd_vals = extract_counts(odd_dict)
    even_vals = extract_counts(even_dict)
    odd_vals = sort_counts(odd_vals)
    even_vals = sort_counts(even_vals)
    odd_len = len(odd_vals)
    even_len = len(even_vals)
    if odd_len == 1 and even_len == 1:
        single_case(n, odd_vals, even_vals)
    elif odd_len > 1 and even_len > 1:
        multi_case(n, odd_vals, even_vals)
    else:
        mixed_case(n, odd_vals, even_vals)

main()