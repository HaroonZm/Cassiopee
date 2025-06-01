def adjust_month_year(y, m):
    if m <= 2:
        m += 12
        y -= 1
    return y, m

def compute_fliegel(y, m, d):
    y, m = adjust_month_year(y, m)
    part1 = int(365.25 * y)
    part2 = int(30.59 * (m - 2))
    part3 = y // 400
    part4 = y // 100
    return part1 + part2 + part3 - part4 + d - 678912

def Fliegel(y, m, d):
    return compute_fliegel(y, m, d)

def adjust_inv_month_year(y, m):
    if m > 12:
        m -= 12
        y += 1
    return y, m

def compute_a(mjd):
    part1 = 4 * mjd + 3
    part2 = 3 * (1 + 4 * (mjd + 1) // 146097) // 4
    return part1 + 4 * part2

def compute_b(a):
    return 2 + 5 * ((a % 1461) // 4)

def compute_y(a):
    return a // 1461

def compute_m(b):
    return 3 + b // 153

def compute_d(b):
    return 1 + (b % 153) // 5

def InvFliegel(mjd):
    mjd += 678881
    a = compute_a(mjd)
    b = compute_b(a)
    y = compute_y(a)
    m = compute_m(b)
    d = compute_d(b)
    y, m = adjust_inv_month_year(y, m)
    return y, m, d

def get_maya_unit():
    return [13, 20, 20, 18, 20]

def get_maya_cycle():
    u = get_maya_unit()
    cycle = 1
    for x in u:
        cycle *= x
    return cycle

def parse_input(s):
    return list(map(int, s.split(".")))

def is_gregorian_date(v):
    return len(v) == 3

def compute_mjd_base():
    return Fliegel(2012, 12, 21)

def convert_gregorian_to_maya(v, mjd_base, maya_cycle):
    mjd = Fliegel(v[0], v[1], v[2]) - mjd_base
    mjd %= maya_cycle
    return mjd

def convert_maya_to_base_units(mjd, maya_unit):
    m = []
    for u in reversed(maya_unit):
        m.append(int(mjd % u))
        mjd /= u
    return m[::-1]

def print_maya_date(m):
    print(f"{m[0]}.{m[1]}.{m[2]}.{m[3]}.{m[4]}")

def convert_maya_to_mjd(v, maya_unit):
    mjd = v[0]
    for i in range(1, 5):
        mjd *= maya_unit[i]
        mjd += v[i]
    return mjd

def print_gregorian_date(y, m, d):
    print(f"{y}.{m}.{d}")

def main_loop():
    mjd_base = compute_mjd_base()
    maya_unit = get_maya_unit()
    maya_cycle = get_maya_cycle()
    while True:
        s = input()
        if s == "#":
            break
        v = parse_input(s)
        if is_gregorian_date(v):
            mjd = convert_gregorian_to_maya(v, mjd_base, maya_cycle)
            m = convert_maya_to_base_units(mjd, maya_unit)
            print_maya_date(m)
        else:
            mjd = convert_maya_to_mjd(v, maya_unit)
            y, m, d = InvFliegel(mjd + mjd_base)
            print_gregorian_date(y, m, d)

main_loop()