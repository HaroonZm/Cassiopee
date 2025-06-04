def read_input():
    return input()

def to_int(s):
    return int(s)

def split_string(s):
    return s.split()

def map_to_int(lst):
    return list(map(int, lst))

def get_n():
    s = read_input()
    return to_int(s)

def get_x():
    s = read_input()
    lst = split_string(s)
    return map_to_int(lst)

def get_max(lst):
    return max(lst)

def get_min(lst):
    return min(lst)

def compute_a(mx, mn):
    return mx + mn

def compute_b(a):
    return a // 2

def compute_diff(mx, b):
    return mx - b

def main():
    n = get_n()
    x = get_x()
    mx = get_max(x)
    mn = get_min(x)
    a = compute_a(mx, mn)
    b = compute_b(a)
    diff = compute_diff(mx, b)
    print(diff)

main()