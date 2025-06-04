def get_input():
    return map(int, raw_input().split())

def is_end_condition(m, f, r):
    return m == -1 and f == -1 and r == -1

def has_missing_scores(m, f):
    return m == -1 or f == -1

def get_total_score(m, f):
    return m + f

def is_grade_A(total):
    return total >= 80

def is_grade_B(total):
    return total >= 65

def is_grade_C(total):
    return total >= 50

def is_grade_D_or_C(total):
    return total >= 30

def is_reexam_sufficient(r):
    return r >= 50

def decide_grade(m, f, r):
    if has_missing_scores(m, f):
        return 'F'
    total = get_total_score(m, f)
    if is_grade_A(total):
        return 'A'
    elif is_grade_B(total):
        return 'B'
    elif is_grade_C(total):
        return 'C'
    elif is_grade_D_or_C(total):
        if is_reexam_sufficient(r):
            return 'C'
        else:
            return 'D'
    else:
        return 'F'

def process_grading():
    while True:
        m, f, r = get_input()
        if is_end_condition(m, f, r):
            break
        grade = decide_grade(m, f, r)
        print grade

process_grading()