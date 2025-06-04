def read_dimensions():
    return tuple(map(int, input().split()))

def read_n():
    return int(input())

def read_data():
    return list(map(int, input().split()))

def create_ans_matrix(H, W):
    return [[0]*W for _ in range(H)]

def initial_w():
    return 0

def initial_h():
    return 0

def initial_direction():
    return 1

def initial_num():
    return 0

def set_ans(Ans, h, w, num):
    Ans[h][w] = num

def is_last_col(w, W):
    return w == W - 1

def is_first_col(w):
    return w == 0

def increment_w(w):
    return w + 1

def decrement_w(w):
    return w - 1

def increment_h(h):
    return h + 1

def change_direction_to_2():
    return 2

def change_direction_to_1():
    return 1

def fill_data_on_board(H, W, Data):
    Ans = create_ans_matrix(H, W)
    w = initial_w()
    h = initial_h()
    direction = initial_direction()
    num = initial_num()
    for d in Data:
        num = increment_num(num)
        for _ in range(d):
            set_ans(Ans, h, w, num)
            w, h, direction = next_step(w, h, direction, W)
    return Ans

def increment_num(num):
    return num + 1

def next_step(w, h, direction, W):
    if direction == 1:
        if is_last_col(w, W):
            direction = change_direction_to_2()
            h = increment_h(h)
        else:
            w = increment_w(w)
    else:
        if is_first_col(w):
            direction = change_direction_to_1()
            h = increment_h(h)
        else:
            w = decrement_w(w)
    return w, h, direction

def print_ans(Ans, H, W):
    for h in range(H):
        print_row(Ans, h, W)

def print_row(Ans, h, W):
    for w in range(W):
        print_cell(Ans, h, w)
    print()

def print_cell(Ans, h, w):
    print(Ans[h][w], end=' ')

def main():
    H, W = read_dimensions()
    N = read_n()
    Data = read_data()
    Ans = fill_data_on_board(H, W, Data)
    print_ans(Ans, H, W)

main()