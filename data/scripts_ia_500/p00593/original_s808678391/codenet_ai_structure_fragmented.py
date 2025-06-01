def read_input():
    return int(input())

def initialize_jpeg(n):
    return [[0] * n for _ in range(n)]

def is_finished(n):
    return n == 0

def get_initial_position():
    return [0, 0]

def get_initial_value():
    return 1

def update_jpeg(jpeg, i, j, value):
    jpeg[i][j] = value

def is_position_within_bounds(px0, n):
    return px0 < n

def calculate_odd(i, j):
    return (i + j) % 2

def should_increment_px_odd(px, odd, n1):
    return px[not odd] == n1

def should_increment_px_not_odd(px, odd):
    return px[odd] == 0

def increment_px_odd(px, odd):
    px[odd] += 1

def increment_px_not_odd(px, odd):
    px[not odd] += 1

def decrement_px_odd(px, odd):
    px[odd] -= 1

def print_case_number(case):
    print('Case {}:'.format(case))

def print_jpeg_row(row):
    print(''.join('{:>3}'.format(pixel) for pixel in row))

def process_case(n, case):
    jpeg = initialize_jpeg(n)
    n1 = n - 1
    px = get_initial_position()
    cur = get_initial_value()
    while is_position_within_bounds(px[0], n):
        i, j = px
        update_jpeg(jpeg, i, j, cur)
        odd = calculate_odd(i, j)
        if should_increment_px_odd(px, odd, n1):
            increment_px_odd(px, odd)
        elif should_increment_px_not_odd(px, odd):
            increment_px_not_odd(px, odd)
        else:
            increment_px_not_odd(px, odd)
            decrement_px_odd(px, odd)
        cur += 1
    print_case_number(case)
    for row in jpeg:
        print_jpeg_row(row)

def main():
    case = 1
    while True:
        n = read_input()
        if is_finished(n):
            break
        process_case(n, case)
        case += 1

main()