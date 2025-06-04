def read_input():
    return int(input())

def read_height():
    return int(input())

def append_height(hl, height):
    hl.append(height)

def get_heights(n):
    hl = []
    for _ in range(n):
        height = read_height()
        append_height(hl, height)
    return hl

def sort_heights_descending(hl):
    return sorted(hl, reverse=True)

def initial_index():
    return 0

def initial_d():
    return 0

def initial_ans():
    return 1

def subtract_d_from_height(h, d):
    return h - d

def set_zero_if_negative(a):
    if a < 0:
        return 0
    return a

def add_to_ans(ans, a):
    return ans + a

def update_d(i, d):
    if i % 4 == 3:
        return d + 1
    return d

def process_heights(hl):
    ans = initial_ans()
    d = initial_d()
    for i, h in enumerate(hl):
        a = subtract_d_from_height(h, d)
        a = set_zero_if_negative(a)
        ans = add_to_ans(ans, a)
        d = update_d(i, d)
    return ans

def print_result(ans):
    print(ans)

def main():
    n = read_input()
    hl = get_heights(n)
    hl = sort_heights_descending(hl)
    ans = process_heights(hl)
    print_result(ans)

if __name__ == "__main__":
    main()