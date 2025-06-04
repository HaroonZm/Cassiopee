import sys

def get_grades():
    return ["AAA","AA","A","B","C","D","E","NA"]

def parse_input_line(line):
    parts = line.split()
    t1 = float(parts[0])
    t2 = float(parts[1])
    return t1, t2

def get_t5_base(t1):
    if t1 < 35.5:
        return 0
    return None

def get_t5_next1(t1):
    if t1 < 37.5:
        return 1
    return None

def get_t5_next2(t1):
    if t1 < 40:
        return 2
    return None

def get_t5_next3(t1):
    if t1 < 43:
        return 3
    return None

def get_t5_next4(t1):
    if t1 < 50:
        return 4
    return None

def get_t5_next5(t1):
    if t1 < 55:
        return 5
    return None

def get_t5_next6(t1):
    if t1 < 70:
        return 6
    return None

def get_t5_fallback():
    return 7

def calc_t5(t1):
    res = get_t5_base(t1)
    if res is not None:
        return res
    res = get_t5_next1(t1)
    if res is not None:
        return res
    res = get_t5_next2(t1)
    if res is not None:
        return res
    res = get_t5_next3(t1)
    if res is not None:
        return res
    res = get_t5_next4(t1)
    if res is not None:
        return res
    res = get_t5_next5(t1)
    if res is not None:
        return res
    res = get_t5_next6(t1)
    if res is not None:
        return res
    return get_t5_fallback()

def get_t10_base(t2):
    if t2 < 71:
        return 0
    return None

def get_t10_next1(t2):
    if t2 < 77:
        return 1
    return None

def get_t10_next2(t2):
    if t2 < 83:
        return 2
    return None

def get_t10_next3(t2):
    if t2 < 89:
        return 3
    return None

def get_t10_next4(t2):
    if t2 < 105:
        return 4
    return None

def get_t10_next5(t2):
    if t2 < 116:
        return 5
    return None

def get_t10_next6(t2):
    if t2 < 148:
        return 6
    return None

def get_t10_fallback():
    return 7

def calc_t10(t2):
    res = get_t10_base(t2)
    if res is not None:
        return res
    res = get_t10_next1(t2)
    if res is not None:
        return res
    res = get_t10_next2(t2)
    if res is not None:
        return res
    res = get_t10_next3(t2)
    if res is not None:
        return res
    res = get_t10_next4(t2)
    if res is not None:
        return res
    res = get_t10_next5(t2)
    if res is not None:
        return res
    res = get_t10_next6(t2)
    if res is not None:
        return res
    return get_t10_fallback()

def determine_index(t5, t10):
    return max(t5, t10)

def print_result(idx, grades):
    print(grades[idx])

def process_line(line, grades):
    t1, t2 = parse_input_line(line)
    t5 = calc_t5(t1)
    t10 = calc_t10(t2)
    idx = determine_index(t5, t10)
    print_result(idx, grades)

def main():
    grades = get_grades()
    for line in sys.stdin:
        process_line(line, grades)

main()