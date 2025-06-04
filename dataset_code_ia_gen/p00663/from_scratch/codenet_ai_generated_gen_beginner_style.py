import sys

def parse_expression(s):
    # parse expression like (clause)|(expr)
    # returns list of clauses
    # clause: x&y&z with optional ~ before variables
    # expression format: (clause) or (clause)|(expression)
    clauses = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '(':
            j = i + 1
            cnt = 1
            while j < n and cnt > 0:
                if s[j] == '(':
                    cnt += 1
                elif s[j] == ')':
                    cnt -= 1
                j += 1
            clause_str = s[i+1:j-1]
            clauses.append(clause_str)
            i = j
            if i < n and s[i] == '|':
                i += 1
        else:
            i += 1
    return clauses

def parse_clause(clause):
    # clause is literal&literal&literal
    # literal: var or ~var
    parts = clause.split('&')
    lits = []
    for p in parts:
        if p[0] == '~':
            lits.append(('~', p[1]))
        else:
            lits.append(('+', p[0]))
    return lits

def get_vars(clauses):
    vars_set = set()
    for c in clauses:
        for s,l in c:
            vars_set.add(l)
    return list(vars_set)

def eval_literal(val, sign):
    # val is boolean, sign '+' means var, '~' means negated var
    if sign == '+':
        return val
    else:
        return not val

def main():
    lines = []
    for line in sys.stdin:
        line=line.strip()
        if line == '#':
            break
        lines.append(line)

    for line in lines:
        clauses_str = parse_expression(line)
        clauses = []
        for cstr in clauses_str:
            clauses.append(parse_clause(cstr))
        vars_list = get_vars(clauses)
        vars_list.sort()

        found = False
        # try all assignments simple brute force
        for assignment in range(1 << len(vars_list)):
            var_values = {}
            for i,v in enumerate(vars_list):
                var_values[v] = (assignment >> i) & 1 == 1
            formula_val = False
            for clause in clauses:
                # clause is a conjunction of literals
                clause_val = True
                for sign,var in clause:
                    lit_val = eval_literal(var_values[var], sign)
                    if not lit_val:
                        clause_val = False
                        break
                if clause_val:
                    formula_val = True
                    break
            if formula_val:
                found = True
                break
        print("yes" if found else "no")

if __name__ == '__main__':
    main()