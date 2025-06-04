def get_input():
    return input()

def is_end_of_input(p):
    return p == '#'

def split_expression(p):
    return list(p.split('|'))

def get_subexpression(e):
    return e[1:-1]

def is_negation(x):
    return x[0] == '~'

def get_literal(x):
    if is_negation(x):
        return -1, x[1]
    else:
        return 1, x[0]

def update_dictionary(dic, t, pm):
    dic[t] = pm

def has_contradiction(dic, t, pm):
    return t in dic and dic[t] + pm == 0

def check_clause(e):
    valid = True
    dic = {}
    f = e.split('&')
    for x in f:
        pm, t = get_literal(x)
        if has_contradiction(dic, t, pm):
            valid = False
        update_dictionary(dic, t, pm)
    return valid

def process_expression(exp):
    for e in exp:
        sub = get_subexpression(e)
        if check_clause(sub):
            return True
    return False

def print_result(ans):
    print("yes" if ans else "no")

def main():
    while True:
        p = get_input()
        if is_end_of_input(p):
            break
        exp = split_expression(p)
        ans = process_expression(exp)
        print_result(ans)

main()