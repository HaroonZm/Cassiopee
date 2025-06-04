def get_initial_values():
    return map(int, input().split())

def set_initial_bounds(w, h):
    return 0, w, 0, h

def read_instruction():
    return map(int, input().split())

def update_bounds_a1(x, xl, xr):
    if x < xl:
        return xl, xr
    elif xl <= x <= xr:
        return x, xr
    else:
        return 0, 0

def update_bounds_a2(x, xl, xr):
    if xr < x:
        return xl, xr
    elif xl <= x <= xr:
        return xl, x
    else:
        return 0, 0

def update_bounds_a3(y, yd, yu):
    if y < yd:
        return yd, yu
    elif yd <= y <= yu:
        return y, yu
    else:
        return 0, 0

def update_bounds_a4(y, yd, yu):
    if y > yu:
        return yd, yu
    elif yd <= y <= yu:
        return yd, y
    else:
        return 0, 0

def apply_instruction(x, y, a, xl, xr, yd, yu):
    if a == 1:
        xl, xr = update_bounds_a1(x, xl, xr)
    elif a == 2:
        xl, xr = update_bounds_a2(x, xl, xr)
    elif a == 3:
        yd, yu = update_bounds_a3(y, yd, yu)
    elif a == 4:
        yd, yu = update_bounds_a4(y, yd, yu)
    return xl, xr, yd, yu

def process_instructions(n, xl, xr, yd, yu):
    for _ in range(n):
        x, y, a = read_instruction()
        xl, xr, yd, yu = apply_instruction(x, y, a, xl, xr, yd, yu)
    return xl, xr, yd, yu

def compute_area(xl, xr, yd, yu):
    return max(0, xr - xl) * max(0, yu - yd)

def main():
    w, h, n = get_initial_values()
    xl, xr, yd, yu = set_initial_bounds(w, h)
    xl, xr, yd, yu = process_instructions(n, xl, xr, yd, yu)
    print(compute_area(xl, xr, yd, yu))

main()