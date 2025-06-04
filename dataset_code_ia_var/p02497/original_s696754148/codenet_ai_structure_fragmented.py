#!/usr/bin/env python

def read_input():
    return raw_input()

def is_end_input(param):
    return param == "-1 -1 -1"

def parse_scores(param):
    return [int(x) for x in param.split(" ")]

def has_missing_score(m, f):
    return (m == -1) or (f == -1)

def total_score(m, f):
    return m + f

def score_is_a(total):
    return total >= 80

def score_is_b(total):
    return total >= 65

def score_is_c(total):
    return total >= 50

def score_is_d_condition(total):
    return total >= 30

def can_upgrade_to_c(r):
    return r >= 50

def print_grade(grade):
    print grade

def process_scores(m, f, r):
    t = total_score(m, f)
    if has_missing_score(m, f):
        print_grade("F")
    elif score_is_a(t):
        print_grade("A")
    elif score_is_b(t):
        print_grade("B")
    elif score_is_c(t):
        print_grade("C")
    elif score_is_d_condition(t):
        if can_upgrade_to_c(r):
            print_grade("C")
        else:
            print_grade("D")
    else:
        print_grade("F")

def main_loop():
    while True:
        param = read_input()
        if is_end_input(param):
            break
        m, f, r = parse_scores(param)
        process_scores(m, f, r)

def main():
    main_loop()

if __name__ == '__main__':
    main()