def read_input():
    try:
        line = input()
        return line
    except:
        return None

def split_line(line):
    try:
        return line.split()
    except:
        return None

def convert_to_floats(strs):
    try:
        return list(map(float, strs))
    except:
        return None

def multiply_by_100(values):
    return [v * 100 for v in values]

def to_ints(values):
    return [int(v) for v in values]

def process_input():
    line = read_input()
    if line is None:
        return None
    strs = split_line(line)
    if strs is None or not strs:
        return None
    floats = convert_to_floats(strs)
    if floats is None or len(floats) != 2:
        return None
    mult = multiply_by_100(floats)
    ints = to_ints(mult)
    return ints

def check_aaa(t1, t2):
    return t1 < 3550 and t2 < 7100

def check_aa(t1, t2):
    return t1 < 3750 and t2 < 7700

def check_a(t1, t2):
    return t1 < 4000 and t2 < 8300

def check_b(t1, t2):
    return t1 < 4300 and t2 < 8900

def check_c(t1, t2):
    return t1 < 5000 and t2 < 10500

def check_d(t1, t2):
    return t1 < 5500 and t2 < 11600

def check_e(t1, t2):
    return t1 < 7000 and t2 < 14800

def get_grade(t1, t2):
    if check_aaa(t1, t2):
        return "AAA"
    elif check_aa(t1, t2):
        return "AA"
    elif check_a(t1, t2):
        return "A"
    elif check_b(t1, t2):
        return "B"
    elif check_c(t1, t2):
        return "C"
    elif check_d(t1, t2):
        return "D"
    elif check_e(t1, t2):
        return "E"
    else:
        return "NA"

def main_loop():
    while True:
        ints = process_input()
        if ints is None:
            break
        t1, t2 = ints[0], ints[1]
        grade = get_grade(t1, t2)
        print(grade)

main_loop()