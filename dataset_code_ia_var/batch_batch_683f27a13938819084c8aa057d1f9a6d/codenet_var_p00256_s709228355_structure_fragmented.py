def adjust_month_and_year(y, m):
    if m <= 2:
        m += 12
        y -= 1
    return y, m

def calculate_fliegel_julian(y, m):
    return int(365.25 * y)

def calculate_fliegel_month(m):
    return int(30.59 * (m - 2))

def calculate_fliegel_century_adjustments(y):
    return (y // 400) - (y // 100)

def Fliegel(y, m, d):
    y, m = adjust_month_and_year(y, m)
    julian = calculate_fliegel_julian(y, m)
    month = calculate_fliegel_month(m)
    century = calculate_fliegel_century_adjustments(y)
    return julian + month + century + d - 678912

def invfliegel_add_mjd_offset(mjd):
    return mjd + 678881

def invfliegel_compute_a(mjd):
    return 4 * mjd + 3 + 4 * (3 * (1 + 4 * (mjd + 1) // 146097) // 4)

def invfliegel_compute_b(a):
    return 2 + 5 * ((a % 1461) // 4)

def invfliegel_compute_y(a):
    return a // 1461

def invfliegel_compute_m(b):
    return 3 + b // 153

def invfliegel_compute_d(b):
    return 1 + (b % 153) // 5

def invfliegel_adjust_month_and_year(y, m):
    if m > 12:
        m -= 12
        y += 1
    return y, m

def InvFliegel(mjd):
    mjd = invfliegel_add_mjd_offset(mjd)
    a = invfliegel_compute_a(mjd)
    b = invfliegel_compute_b(a)
    y = invfliegel_compute_y(a)
    m = invfliegel_compute_m(b)
    d = invfliegel_compute_d(b)
    y, m = invfliegel_adjust_month_and_year(y, m)
    return y, m, d

def get_mjd_base():
    return Fliegel(2012, 12, 21)

def get_maya_unit():
    return [13, 20, 20, 18, 20]

def get_maya_cycle(maya_unit):
    res = 1
    for u in maya_unit:
        res *= u
    return res

def parse_input(s):
    if "." in s:
        return list(map(int, s.split(".")))
    return [int(s)]

def compute_maya_date_from_ymd(v, mjd_base, maya_unit, maya_cycle):
    mjd = (Fliegel(v[0], v[1], v[2]) - mjd_base) % maya_cycle
    m = []
    mjd_values = []
    return mjd, m

def compute_maya_date_bars(mjd, maya_unit):
    m = []
    for u in reversed(maya_unit):
        m.append(mjd % u)
        mjd //= u
    return list(reversed(m))

def print_maya_date(m):
    print("%d.%d.%d.%d.%d" % (m[0], m[1], m[2], m[3], m[4]))

def compute_mjd_from_maya(v, maya_unit):
    mjd = v[0]
    for i in range(1, 5):
        mjd *= maya_unit[i]
        mjd += v[i]
    return mjd

def print_ymd(y, m, d):
    print("%d.%d.%d" % (y, m, d))

def main_loop():
    mjd_base = get_mjd_base()
    maya_unit = get_maya_unit()
    maya_cycle = get_maya_cycle(maya_unit)
    while True:
        s = input()
        if s == '#':
            break
        v = parse_input(s)
        if len(v) == 3:
            mjd = (Fliegel(v[0], v[1], v[2]) - mjd_base) % maya_cycle
            m = compute_maya_date_bars(mjd, maya_unit)
            print_maya_date(m)
        else:
            mjd = compute_mjd_from_maya(v, maya_unit)
            y, m, d = InvFliegel(mjd + mjd_base)
            print_ymd(y, m, d)

main_loop()