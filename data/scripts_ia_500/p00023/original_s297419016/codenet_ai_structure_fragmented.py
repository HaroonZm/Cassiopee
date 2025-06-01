def read_number_of_cases():
    return int(input())

def read_circle_parameters():
    return list(map(float, input().split()))

def calculate_distance_squared(xa, ya, xb, yb):
    return (xa - xb) ** 2 + (ya - yb) ** 2

def calculate_sum_radii_squared(ra, rb):
    return (ra + rb) ** 2

def calculate_diff_radii_squared(ra, rb):
    return (ra - rb) ** 2

def compare_distances(d1, d2):
    return d1 <= d2

def compare_diff_and_distance(dr, d1):
    return dr > d1

def decide_output_case1(ra, rb):
    if ra > rb:
        return 2
    else:
        return -2

def decide_output(d1, d2, dr, ra, rb):
    if compare_distances(d1, d2):
        if compare_diff_and_distance(dr, d1):
            return decide_output_case1(ra, rb)
        else:
            return 1
    else:
        return 0

def process_single_case():
    xa, ya, ra, xb, yb, rb = read_circle_parameters()
    d1 = calculate_distance_squared(xa, ya, xb, yb)
    d2 = calculate_sum_radii_squared(ra, rb)
    dr = calculate_diff_radii_squared(ra, rb)
    result = decide_output(d1, d2, dr, ra, rb)
    print(result)

def main():
    n = read_number_of_cases()
    for _ in range(n):
        process_single_case()

main()