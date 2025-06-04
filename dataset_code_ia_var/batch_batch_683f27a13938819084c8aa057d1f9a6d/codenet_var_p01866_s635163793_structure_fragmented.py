def read_n():
    return int(input())

def read_x():
    return input()

def read_d():
    return int(input())

def initialize_swap():
    return {}

def should_swap_left(d):
    return d != 0

def handle_left_pass(n, x, d, swap):
    i = 0
    while i < n and should_swap_left(d[0]):
        process_left_index(i, x, d, swap)
        i += 1

def process_left_index(i, x, d, swap):
    if is_zero(x, i):
        swap_index(swap, i)
        decrement_d(d)

def is_zero(x, i):
    return x[i] == "0"

def swap_index(swap, i):
    swap[i] = True

def decrement_d(d):
    d[0] -= 1

def should_swap_right(d):
    return d != 0

def handle_right_pass(n, x, d, swap):
    i = n - 1
    while i >= 0 and should_swap_right(d[0]):
        process_right_index(i, x, d, swap)
        i -= 1

def process_right_index(i, x, d, swap):
    if is_one(x, i):
        swap_index(swap, i)
        decrement_d(d)

def is_one(x, i):
    return x[i] == "1"

def build_output(n, x, swap):
    return "".join([apply_swap(i, x, swap) for i in range(n)])

def apply_swap(i, x, swap):
    if i in swap:
        return toggle(x[i])
    else:
        return x[i]

def toggle(c):
    if c == "1":
        return "0"
    else:
        return "1"

def main():
    n = read_n()
    x = read_x()
    d = [read_d()]
    swap = initialize_swap()
    handle_left_pass(n, x, d, swap)
    handle_right_pass(n, x, d, swap)
    out = build_output(n, x, swap)
    print(out)

main()