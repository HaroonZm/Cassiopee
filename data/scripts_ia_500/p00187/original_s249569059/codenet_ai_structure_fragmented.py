def extract_points(xy):
    return xy[0], xy[1], xy[2], xy[3]

def calculate_tc(ax, ay, bx, by, cx, cy):
    return (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)

def calculate_td(ax, ay, bx, by, dx, dy):
    return (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

def isX(xy1, xy2):
    ax, ay, bx, by = extract_points(xy1)
    cx, cy, dx, dy = extract_points(xy2)
    tc = calculate_tc(ax, ay, bx, by, cx, cy)
    td = calculate_td(ax, ay, bx, by, dx, dy)
    return tc * td < 0

def calculate_dn(ax, ay, bx, by, cx, cy, dx, dy):
    return ((by - ay) * (dx - cx) - (bx - ax) * (dy - cy)) * 1.0

def calculate_x(ax, ay, bx, by, cx, cy, dx, dy, dn):
    part1 = (cy * dx - cx * dy) * (bx - ax)
    part2 = (ay * bx - ax * by) * (dx - cx)
    return (part1 - part2) / dn

def calculate_y(ax, ay, bx, by, cx, cy, dx, dy, dn):
    part1 = (cy * dx - cx * dy) * (by - ay)
    part2 = (ay * bx - ax * by) * (dy - cy)
    return (part1 - part2) / dn

def ip(xy1, xy2):
    ax, ay, bx, by = extract_points(xy1)
    cx, cy, dx, dy = extract_points(xy2)
    dn = calculate_dn(ax, ay, bx, by, cx, cy, dx, dy)
    x = calculate_x(ax, ay, bx, by, cx, cy, dx, dy, dn)
    y = calculate_y(ax, ay, bx, by, cx, cy, dx, dy, dn)
    return x, y

def read_points():
    return map(int, raw_input().split())

def count_zeros_in_list(lst):
    return lst.count(0)

def area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

def print_result(S):
    if S >= 1900000:
        print "dai-kichi"
    elif S >= 1000000:
        print "chu-kichi"
    elif S >= 100000:
        print "kichi"
    elif S > 0:
        print "syo-kichi"
    else:
        print "kyo"

def main_loop():
    while True:
        xy1 = read_points()
        if count_zeros_in_list(xy1) == 4:
            break
        xy2 = read_points()
        xy3 = read_points()
        if isX(xy1, xy2) and isX(xy2, xy3) and isX(xy3, xy1):
            x1, y1 = ip(xy1, xy2)
            x2, y2 = ip(xy2, xy3)
            x3, y3 = ip(xy3, xy1)
            S = area(x1, y1, x2, y2, x3, y3)
            print_result(S)
        else:
            print "kyo"

main_loop()