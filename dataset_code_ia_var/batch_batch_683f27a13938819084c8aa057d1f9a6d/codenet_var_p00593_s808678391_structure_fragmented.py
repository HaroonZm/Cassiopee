def read_input():
    return int(input())

def should_terminate(n):
    return n == 0

def init_jpeg(n):
    return [[0] * n for _ in range(n)]

def process_main_loop(n):
    jpeg = init_jpeg(n)
    n1 = n - 1
    px = [0, 0]
    cur = 1
    while continue_filling(px, n):
        i, j = px
        assign_pixel(jpeg, i, j, cur)
        update_position(px, n1)
        cur += 1
    return jpeg

def continue_filling(px, n):
    return px[0] < n

def assign_pixel(jpeg, i, j, cur):
    jpeg[i][j] = cur

def update_position(px, n1):
    i, j = px
    odd = position_is_odd(i, j)
    if is_at_end(px, odd, n1):
        increment(px, odd)
    elif is_at_start(px, odd):
        increment(px, not odd)
    else:
        increment(px, not odd)
        decrement(px, odd)

def position_is_odd(i, j):
    return (i + j) % 2

def is_at_end(px, odd, n1):
    return px[not odd] == n1

def is_at_start(px, odd):
    return not px[odd]

def increment(px, idx):
    px[idx] += 1

def decrement(px, idx):
    px[idx] -= 1

def print_case_header(case):
    print('Case {}:'.format(case))

def print_jpeg(jpeg):
    for row in jpeg:
        print(''.join(format_pixel(pixel) for pixel in row))

def format_pixel(pixel):
    return '{:>3}'.format(pixel)

def main():
    case = 1
    while True:
        n = read_input()
        if should_terminate(n):
            break
        jpeg = process_main_loop(n)
        print_case_header(case)
        print_jpeg(jpeg)
        case += 1

main()