import math

def read_number_of_tests():
    return int(input())

def read_circle_params():
    return list(map(float, input().split()))

def get_circle_variables():
    xa, ya, ra, xb, yb, rb = read_circle_params()
    return xa, ya, ra, xb, yb, rb

def compute_squared_distance(xa, ya, xb, yb):
    return (xa - xb) ** 2 + (ya - yb) ** 2

def compute_sum_radii_squared(ra, rb):
    return (ra + rb) ** 2

def compute_diff_radii_squared(ra, rb):
    return (ra - rb) ** 2

def same_center_dr_larger(d1, dr):
    return dr > d1

def print_overlap_result(ra, rb):
    if ra > rb:
        print(2)
    else:
        print(-2)

def print_touching_result():
    print(1)

def print_disjoint_result():
    print(0)

def process_single_case():
    xa, ya, ra, xb, yb, rb = get_circle_variables()
    d1 = compute_squared_distance(xa, ya, xb, yb)
    d2 = compute_sum_radii_squared(ra, rb)
    dr = compute_diff_radii_squared(ra, rb)
    if d1 <= d2:
        if same_center_dr_larger(d1, dr):
            print_overlap_result(ra, rb)
        else:
            print_touching_result()
    else:
        print_disjoint_result()

def process_all_cases():
    n = read_number_of_tests()
    for _ in range(n):
        process_single_case()

process_all_cases()