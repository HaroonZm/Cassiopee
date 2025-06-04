def get_empty_ans_list():
    return []

def get_sc_max():
    return 0

def get_sc_min():
    return 500

def get_input():
    return input()

def check_exit_condition(n):
    return n == 0

def get_range_n(n):
    return range(n)

def parse_scores():
    return list(map(int, raw_input().split()))

def sum_scores(scores):
    return sum(scores)

def is_greater(a, b):
    return a > b

def is_less(a, b):
    return a < b

def to_str(a):
    return str(a)

def make_ans_entry(scMax, scMin):
    return to_str(scMax) + ' ' + to_str(scMin)

def append_ans(ans, entry):
    ans.append(entry)

def print_ans_entry(entry):
    print entry

def process_batch(n):
    scMax = get_sc_max()
    scMin = get_sc_min()
    for i in get_range_n(n):
        scores = parse_scores()
        score = sum_scores(scores)
        if is_greater(score, scMax):
            scMax = score
        if is_less(score, scMin):
            scMin = score
    return (scMax, scMin)

def main_loop():
    ans = get_empty_ans_list()
    while True:
        n = get_input()
        if check_exit_condition(n):
            break
        scMax, scMin = process_batch(n)
        entry = make_ans_entry(scMax, scMin)
        append_ans(ans, entry)
    for entry in ans:
        print_ans_entry(entry)

main_loop()