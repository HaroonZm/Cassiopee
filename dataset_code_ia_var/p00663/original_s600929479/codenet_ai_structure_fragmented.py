def is_end_command(command):
    return command == "#"

def read_input():
    return raw_input()

def split_expression(line):
    return line.split("|")

def process_all_clauses(clauses):
    return [process_single_clause(clause) for clause in clauses]

def process_single_clause(clause):
    inside = extract_inside_parentheses(clause)
    return clause_to_python_expr(inside)

def extract_inside_parentheses(clause):
    return list(clause)[1:-1]

def clause_to_python_expr(clause_chars):
    var_list = []
    result = []
    for char in clause_chars:
        result.append(process_char(char, var_list))
    return " ".join(map(str, result))

def process_char(char, var_list):
    if char == '&':
        return "and"
    elif char == '~':
        return "not"
    else:
        return replace_var_with_torf(char, var_list)

def replace_var_with_torf(char, var_list):
    if char not in var_list:
        var_list.append(char)
        return "torf[" + str(len(var_list) - 1) + "]"
    else:
        return "torf[" + str(var_list.index(char)) + "]"

def any_clause_satisfiable(all_clauses):
    for clause in all_clauses:
        if is_clause_satisfiable(clause):
            return True
    return False

def is_clause_satisfiable(clause):
    return recursive_check(clause, [], 0)

def recursive_check(expr, torf, idx):
    if is_final_variable(idx):
        return evaluate_expr(expr, torf)
    else:
        return try_all_boolean_combinations(expr, torf, idx)

def is_final_variable(idx):
    return idx == 3

def evaluate_expr(expr, torf):
    return eval(expr)

def try_all_boolean_combinations(expr, torf, idx):
    return (recursive_check(expr, torf + [True], idx + 1) or 
            recursive_check(expr, torf + [False], idx + 1))

def print_result(is_satisfiable):
    if is_satisfiable:
        print "yes"
    else:
        print "no"

def main():
    while True:
        line = read_input()
        clauses = split_expression(line)
        if is_end_command(clauses[0]):
            break
        processed_clauses = process_all_clauses(clauses)
        result = any_clause_satisfiable(processed_clauses)
        print_result(result)

main()