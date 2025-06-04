def main_loop():
    while True:
        s = get_input()
        if is_terminator(s):
            break
        process_line(s)

def get_input():
    return input().strip()

def is_terminator(s):
    return s == '#'

def process_line(s):
    clauses = split_clauses(s)
    for clause in clauses:
        if process_clause(clause):
            print_yes()
            break
    else:
        print_no()

def split_clauses(s):
    return s.split('|')

def process_clause(clause):
    literals = extract_literals(clause)
    ntil = count_not_signs(clause)
    if case_ntil_0_or_3(ntil):
        return True
    if case_ntil_1(ntil, clause, literals):
        return True
    if case_ntil_2(ntil, clause, literals):
        return True
    return False

def extract_literals(clause):
    return clause[1:-1].split('&')

def count_not_signs(clause):
    return clause.count('~')

def case_ntil_0_or_3(ntil):
    return ntil == 0 or ntil == 3

def case_ntil_1(ntil, clause, literals):
    if ntil == 1:
        x = find_single_negated_literal(literals)
        if x is not None and count_var(clause, x) == 1:
            return True
    return False

def find_single_negated_literal(literals):
    candidates = [v[1] for v in literals if v and v[0] == '~']
    return candidates[0] if candidates else None

def count_var(s, x):
    return s.count(x)

def case_ntil_2(ntil, clause, literals):
    if ntil == 2:
        x = find_single_positive_literal(literals)
        if x is not None and count_var(clause, x) == 1:
            return True
    return False

def find_single_positive_literal(literals):
    candidates = [v for v in literals if len(v) == 1]
    return candidates[0] if candidates else None

def print_yes():
    print('yes')

def print_no():
    print('no')

main_loop()