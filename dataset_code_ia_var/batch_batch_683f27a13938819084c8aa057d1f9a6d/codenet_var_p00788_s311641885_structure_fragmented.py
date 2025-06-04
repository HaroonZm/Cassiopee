import sys

def get_readline():
    return sys.stdin.readline

def get_write():
    return sys.stdout.write

def parse_line(line):
    return map(int, line.split())

def should_terminate(p):
    return p == 0

def get_initial_left():
    return 0, 1

def get_initial_right():
    return 1, 0

def get_initial_flags():
    return 1, 1

def get_initial_answers():
    return (0, 1), (1, 0)

def get_initial():
    la, lb = get_initial_left()
    ra, rb = get_initial_right()
    lu, ru = get_initial_flags()
    (lx, ly), (rx, ry) = get_initial_answers()
    return la, lb, ra, rb, lu, ru, lx, ly, rx, ry

def compute_ma_mb(la, ra, lb, rb):
    return la + ra, lb + rb

def is_left_branch(p, ma, mb):
    return p * mb * mb < ma * ma

def can_update(ma, mb, n):
    return ma <= n and mb <= n

def update_right(ra, rb, ma, mb):
    return ma, mb

def update_rx_ry(rx, ry, ma, mb):
    return ma, mb

def update_left(la, lb, ma, mb):
    return ma, mb

def update_lx_ly(lx, ly, ma, mb):
    return ma, mb

def set_flag_zero():
    return 0

def update_left_branch(ra, rb, rx, ry, ma, mb, n, lu):
    ra, rb = update_right(ra, rb, ma, mb)
    if can_update(ma, mb, n):
        rx, ry = update_rx_ry(rx, ry, ma, mb)
    else:
        lu = set_flag_zero()
    return ra, rb, rx, ry, lu

def update_right_branch(la, lb, lx, ly, ma, mb, n, ru):
    la, lb = update_left(la, lb, ma, mb)
    if can_update(ma, mb, n):
        lx, ly = update_lx_ly(lx, ly, ma, mb)
    else:
        ru = set_flag_zero()
    return la, lb, lx, ly, ru

def get_results(lx, ly, rx, ry):
    return lx, ly, rx, ry

def get_next_state(p, n, la, lb, ra, rb, lu, ru, lx, ly, rx, ry):
    ma, mb = compute_ma_mb(la, ra, lb, rb)
    if is_left_branch(p, ma, mb):
        ra, rb, rx, ry, lu = update_left_branch(ra, rb, rx, ry, ma, mb, n, lu)
    else:
        la, lb, lx, ly, ru = update_right_branch(la, lb, lx, ly, ma, mb, n, ru)
    return la, lb, ra, rb, lu, ru, lx, ly, rx, ry

def terminate_flags(lu, ru):
    return lu or ru

def stern_brocot(p, n):
    la, lb, ra, rb, lu, ru, lx, ly, rx, ry = get_initial()
    while terminate_flags(lu, ru):
        la, lb, ra, rb, lu, ru, lx, ly, rx, ry = get_next_state(
            p, n, la, lb, ra, rb, lu, ru, lx, ly, rx, ry
        )
    lx, ly, rx, ry = get_results(lx, ly, rx, ry)
    return lx, ly, rx, ry

def format_output(rx, ry, lx, ly):
    return "%d/%d %d/%d\n" % (rx, ry, lx, ly)

def main():
    readline = get_readline()
    write = get_write()
    while True:
        line = readline()
        p, n = parse_line(line)
        if should_terminate(p):
            break
        lx, ly, rx, ry = stern_brocot(p, n)
        output = format_output(rx, ry, lx, ly)
        write(output)

main()