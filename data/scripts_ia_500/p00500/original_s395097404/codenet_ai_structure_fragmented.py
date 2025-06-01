def read_int():
    return int(raw_input())

def read_int_list():
    return map(int, raw_input().split())

def init_list(n):
    a = []
    for _ in range(n):
        a.append(read_int_list())
    return a

def init_flag():
    return [1, 1, 1]

def compare_elements(a_i, a_j, f):
    for k in range(3):
        if a_i[k] == a_j[k]:
            f[k] = 0
    return f

def process_flags(i, a, n):
    f = init_flag()
    for j in range(n):
        if i == j:
            continue
        f = compare_elements(a[i], a[j], f)
    return f

def compute_result(a_i, f):
    return a_i[0]*f[0] + a_i[1]*f[1] + a_i[2]*f[2]

def main():
    n = read_int()
    a = init_list(n)
    for i in range(n):
        f = process_flags(i, a, n)
        result = compute_result(a[i], f)
        print result

main()