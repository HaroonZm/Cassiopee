def get_rr_list():
    return [0,0,0,1,1,1,2,2,2]

def get_cc_list():
    return [0,1,2,0,1,2,0,1,2]

def get_A_ord():
    return ord('A')

def to_char_ord(char):
    return ord(char)

def get_input_as_list():
    return list(input())

def get_position(index, buf, rr, cc, A):
    return rr[to_char_ord(buf[index])-A], cc[to_char_ord(buf[index])-A]

def update_indices(j):
    return j + 1

def equal_rows(r1, r2):
    return r1 == r2

def equal_cols(c1, c2):
    return c1 == c2

def valid_column_move(c, c2):
    return c2 == c + 1 or c2 == c - 1

def valid_row_move(r, r2):
    return r2 == r + 1 or r2 == r - 1

def check_move(r, c, r2, c2):
    if equal_rows(r2, r):
        if valid_column_move(c, c2):
            return True
    elif equal_cols(c2, c):
        if valid_row_move(r, r2):
            return True
    return False

def print_buffer(buf):
    print(*buf, sep='')

def process_input_line(buf, rr, cc, A):
    j = 0
    r, c = get_position(j, buf, rr, cc, A)
    j = update_indices(j)
    f = True
    while j < len(buf) and f:
        f = False
        r2, c2 = get_position(j, buf, rr, cc, A)
        j = update_indices(j)
        if check_move(r, c, r2, c2):
            f = True
        r, c = r2, c2
    if f:
        print_buffer(buf)

def main_loop():
    rr = get_rr_list()
    cc = get_cc_list()
    A = get_A_ord()
    for _ in range(1000):
        buf = get_input_as_list()
        process_input_line(buf, rr, cc, A)

main_loop()