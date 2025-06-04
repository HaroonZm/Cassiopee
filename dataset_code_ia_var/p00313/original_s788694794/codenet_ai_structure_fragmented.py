def read_n():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def slice_from_second_element(lst):
    return lst[1:]

def read_a():
    return slice_from_second_element(read_list())

def read_b():
    return slice_from_second_element(read_list())

def read_c():
    return slice_from_second_element(read_list())

def make_range(n):
    return range(1, n+1)

def item_not_in_lists(i, la, lb):
    return (i not in la) and (i not in lb)

def item_in_list(i, lc):
    return i in lc

def process_x(i, a, b, c):
    return item_not_in_lists(i, a, b) and item_in_list(i, c)

def process_y(i, b, c):
    return (i in b) and (i in c)

def count_x_y(n, a, b, c):
    x = 0
    y = 0
    for i in make_range(n):
        if process_x(i, a, b, c):
            x = increment(x)
        elif process_y(i, b, c):
            y = increment(y)
    return x, y

def increment(val):
    return val + 1

def output_result(x, y):
    print(x + y)

def main():
    n = read_n()
    a = read_a()
    b = read_b()
    c = read_c()
    x, y = count_x_y(n, a, b, c)
    output_result(x, y)

main()