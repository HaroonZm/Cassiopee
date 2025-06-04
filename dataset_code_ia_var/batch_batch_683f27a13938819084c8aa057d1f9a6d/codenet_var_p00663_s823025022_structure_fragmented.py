def get_user_input():
    return raw_input()

def is_break_command(ex):
    return ex[0] == "#"

def split_clauses(input_line):
    return input_line.split("|")

def preprocess_all_clauses(ex):
    return [preprocess_clause(clause) for clause in ex]

def preprocess_clause(clause):
    variables = []
    tokens = clause_to_tokens(clause)
    replaced_tokens = [replace_token(token, variables) for token in tokens]
    return join_tokens(replaced_tokens)

def clause_to_tokens(clause):
    return list(clause)[1:-1]

def replace_token(token, variables):
    if token == "&":
        return "and"
    elif token == "~":
        return "not"
    else:
        return replace_variable_token(token, variables)

def replace_variable_token(token, variables):
    if token not in variables:
        variables.append(token)
        return "torf[" + str(len(variables)-1) + "]"
    else:
        return "torf[" + str(variables.index(token)) + "]"

def join_tokens(tokens):
    return " ".join(map(str, tokens))

def evaluate_clauses(clauses):
    for clause in clauses:
        if evaluate_clause(clause):
            print "yes"
            return
    print "no"

def evaluate_clause(clause):
    return judge(clause, [], 0)

def judge(expr, torf, i):
    if is_base_case(i):
        return evaluate_expression(expr, torf)
    else:
        return recursive_true(expr, torf, i) or recursive_false(expr, torf, i)

def is_base_case(i):
    return i == 3

def evaluate_expression(expr, torf):
    return eval(expr)

def recursive_true(expr, torf, i):
    return judge(expr, torf + [True], i+1)

def recursive_false(expr, torf, i):
    return judge(expr, torf + [False], i+1)

def main_loop():
    while True:
        input_line = get_user_input()
        ex = split_clauses(input_line)
        if is_break_command(ex):
            break
        processed_clauses = preprocess_all_clauses(ex)
        evaluate_clauses(processed_clauses)

main_loop()