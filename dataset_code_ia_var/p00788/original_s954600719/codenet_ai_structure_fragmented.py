import math

def read_input():
    return [int(x) for x in raw_input().split()]

def should_terminate(p):
    return p == 0

def compute_sqrt(p):
    return math.sqrt(p)

def compute_smaller_initial(sqrtp):
    return [math.floor(sqrtp), int(math.floor(sqrtp)), 1]

def compute_larger_initial(sqrtp):
    return [math.ceil(sqrtp), int(math.ceil(sqrtp)), 1]

def loop_numerator_range(sqrtp, n):
    return range(int(math.floor(sqrtp)) + 1, n + 1)

def compute_denom_smaller(numerator, sqrtp):
    return math.ceil(numerator / sqrtp)

def compute_denom_larger(numerator, sqrtp):
    return math.floor(numerator / sqrtp)

def check_smaller_condition(numerator, denom_smaller, smaller, sqrtp):
    value = numerator / denom_smaller
    if value > smaller[0]:
        if smaller[1] * denom_smaller / float(smaller[2]) != numerator:
            return True
    return False

def update_smaller(smaller, numerator, denom_smaller):
    return [numerator / denom_smaller, numerator, int(denom_smaller)]

def check_larger_condition(numerator, denom_larger, larger, sqrtp):
    value = numerator / denom_larger
    if value < larger[0]:
        if larger[1] * denom_larger / float(larger[2]) != numerator:
            return True
    return False

def update_larger(larger, numerator, denom_larger):
    return [numerator / denom_larger, numerator, int(denom_larger)]

def print_result(larger, smaller):
    print str(larger[1]) + "/" + str(larger[2]) + " " + str(smaller[1]) + "/" + str(smaller[2])

def process_case(p, n):
    sqrtp = compute_sqrt(p)
    smaller = compute_smaller_initial(sqrtp)
    larger = compute_larger_initial(sqrtp)
    for numerator in loop_numerator_range(sqrtp, n):
        denom_smaller = compute_denom_smaller(numerator, sqrtp)
        denom_larger = compute_denom_larger(numerator, sqrtp)
        if check_smaller_condition(numerator, denom_smaller, smaller, sqrtp):
            smaller = update_smaller(smaller, numerator, denom_smaller)
        if check_larger_condition(numerator, denom_larger, larger, sqrtp):
            larger = update_larger(larger, numerator, denom_larger)
    print_result(larger, smaller)

def main():
    while True:
        p, n = read_input()
        if should_terminate(p):
            break
        else:
            process_case(p, n)

main()