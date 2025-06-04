def main_loop():
    while True:
        n = get_input()
        if is_zero(n):
            break
        process_cases(n)

def get_input():
    return input_to_int(input())

def input_to_int(val):
    return int(val)

def is_zero(value):
    return value == 0

def process_cases(n):
    for i in range(n):
        pm, pe, pj = get_scores()
        ave = calculate_average(pm, pe, pj)
        grade = determine_grade(pm, pe, pj, ave)
        print_grade(grade)

def get_scores():
    return parse_scores(raw_input().split())

def parse_scores(score_list):
    return tuple(map(int, score_list))

def calculate_average(pm, pe, pj):
    return (pm + pe + pj) / 3.0

def determine_grade(pm, pe, pj, ave):
    if has_hundred(pm, pe, pj):
        return "A"
    if math_and_eng_high(pm, pe):
        return "A"
    if average_high(ave):
        return "A"
    if average_mid(ave):
        return "B"
    if average_borderline(ave) and any_subject_above_80(pm, pe):
        return "B"
    return "C"

def has_hundred(pm, pe, pj):
    return 100 in (pm, pe, pj)

def math_and_eng_high(pm, pe):
    return (pm + pe) / 2 >= 90

def average_high(ave):
    return ave >= 80

def average_mid(ave):
    return ave >= 70

def average_borderline(ave):
    return ave >= 50

def any_subject_above_80(pm, pe):
    return pm >= 80 or pe >= 80

def print_grade(grade):
    print grade

main_loop()