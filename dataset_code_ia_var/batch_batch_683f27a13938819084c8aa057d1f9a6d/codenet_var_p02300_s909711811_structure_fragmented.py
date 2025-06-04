def get_x(point):
    return point[0]

def get_y(point):
    return point[1]

def sub_x(p1, p2):
    return get_x(p1) - get_x(p2)

def sub_y(p1, p2):
    return get_y(p1) - get_y(p2)

def get_last(lst):
    return lst[-1]

def get_second_last(lst):
    return lst[-2]

def get_third_last(lst):
    return lst[-3]

def signed_area_component(pA, pB, pC):
    x1 = get_x(pA) - get_x(pB)
    y1 = -get_y(pB) + get_y(pC)
    x2 = get_x(pC) - get_x(pB)
    y2 = -get_y(pB) + get_y(pA)
    return x1 * y1 - x2 * y2

def isCLKWISE(ph):
    if len(ph) < 3:
        return True
    pA = get_last(ph)
    pB = get_third_last(ph)
    pC = get_second_last(ph)
    return not (signed_area_component(pA, pB, pC) < 0)

def sort_points(P):
    return sorted(P)

def append_point(lst, p):
    lst.append(p)

def remove_second_last(lst):
    del lst[-2]

def process_upper(P):
    phU = []
    append_point(phU, P[0])
    append_point(phU, P[1])
    for p in P[2:]:
        append_point(phU, p)
        if isCLKWISE(phU):
            continue
        while True:
            remove_second_last(phU)
            try:
                if isCLKWISE(phU):
                    break
            except IndexError:
                break
    return phU

def process_lower(P):
    phL = []
    append_point(phL, P[-1])
    append_point(phL, P[-2])
    for p in P[-3::-1]:
        append_point(phL, p)
        if isCLKWISE(phL):
            continue
        while True:
            remove_second_last(phL)
            try:
                if isCLKWISE(phL):
                    break
            except IndexError:
                break
    return phL

def remove_first_and_last(lst):
    del lst[0]
    del lst[-1]

def concat_lists(a, b):
    return a + b

def ConvexHullScan(P):
    P = sort_points(P)
    phU = process_upper(P)
    phL = process_lower(P)
    remove_first_and_last(phL)
    ph = concat_lists(phU, phL)
    return ph

def read_n():
    return int(input())

def range_n(n):
    return range(n)

def read_point():
    return [int(x) for x in input().split()]

def read_points(n):
    return [read_point() for _ in range_n(n)]

def reverse_list(lst):
    lst.reverse()

def print_len(lst):
    print(len(lst))

def get_enumerated_point_info(point, idx):
    return [get_y(point), get_x(point), idx]

def min_index(points):
    infos = [get_enumerated_point_info(point, idx) for idx, point in enumerate(points)]
    return min(infos)[2]

def print_point(p):
    print(p[0], p[1])

def main():
    n = read_n()
    P = read_points(n)
    P = ConvexHullScan(P)
    reverse_list(P)
    print_len(P)
    idx = min_index(P)
    ordered = P[idx:] + P[:idx]
    for p in ordered:
        print_point(p)

main()