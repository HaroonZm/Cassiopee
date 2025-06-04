def get_input_count():
    return int(input())

def get_range_list(n):
    return [0] * n

def parse_coordinates():
    x_str, y_str, w_str = input().split()
    return int(x_str), int(y_str), int(w_str)

def update_dictionary(a, key, w):
    if key not in a:
        a[key] = 0
    a[key] += w

def update_maximum(b, val):
    return max(b, val)

def process_rectangle(a, b, x, y, w):
    for i in range(2):
        for j in range(2):
            key = (x + i, y + j)
            update_dictionary(a, key, w)
            b = update_maximum(b, a[key])
    return b

def process_all_rectangles(a, b, count):
    rlist = get_range_list(count)
    for _ in rlist:
        x, y, w = parse_coordinates()
        b = process_rectangle(a, b, x, y, w)
    return b

def format_output(b):
    return str(b) + ' / 1'

def main():
    a = {}
    b = 0
    count = get_input_count()
    b = process_all_rectangles(a, b, count)
    print(format_output(b))

main()