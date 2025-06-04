def read_input():
    return str(input())

def to_char_list(src):
    return list(src)

def is_not_space(tok):
    return tok != " "

def filter_spaces(src_chars):
    return [tok for tok in src_chars if is_not_space(tok)]

def append_eof(tokens):
    tokens.append("")
    return tokens

def initial_position():
    return 0

def update_position(val):
    return val

def is_token_or(tok):
    return tok == "|"

def is_token_and(tok):
    return tok == "&"

def is_token_question(tok):
    return tok == "?"

def is_token_left_paren(tok):
    return tok == "("

def is_token_right_paren(tok):
    return tok == ")"

def get_token(tokens, cur):
    return tokens[cur]

def token_is_eof(tok):
    return tok == ""

def min_value(a, b):
    return min(a,b)

def lhs_plus_rhs(lhs, rhs, idx):
    return lhs[idx] + rhs[idx]

def calculate_or(lhs, rhs):
    zero = lhs[0] + rhs[0]
    one = min_value(lhs[1], lhs[0] + rhs[1])
    return (zero, one)

def calculate_and(lhs, rhs):
    zero = min_value(lhs[0], lhs[1] + rhs[0])
    one = lhs[1] + rhs[1]
    return (zero, one)

def make_one_list():
    return [1,1]

def raise_not_closed():
    raise Exception("not closed")

def check_right_paren(tokens, cur):
    if not is_token_right_paren(get_token(tokens, cur)):
        raise_not_closed()
    return cur + 1

def parse_formula(tokens, cur):
    return parse_or(tokens, cur)

def parse_or(tokens, cur):
    lhs, cur = parse_and(tokens, cur)
    if is_token_or(get_token(tokens, cur)):
        cur = update_position(cur + 1)
        rhs, cur = parse_or(tokens, cur)
        result = calculate_or(lhs, rhs)
        return result, cur
    return lhs, cur

def parse_and(tokens, cur):
    lhs, cur = parse_term(tokens, cur)
    if is_token_and(get_token(tokens, cur)):
        cur = update_position(cur + 1)
        rhs, cur = parse_and(tokens, cur)
        result = calculate_and(lhs, rhs)
        return result, cur
    return lhs, cur

def parse_term(tokens, cur):
    tok = get_token(tokens, cur)
    if is_token_question(tok):
        cur = update_position(cur + 1)
        return make_one_list(), cur
    elif is_token_left_paren(tok):
        cur = update_position(cur + 1)
        res, cur = parse_or(tokens, cur)
        cur = check_right_paren(tokens, cur)
        return res, cur
    else:
        return None, cur

def print_result(ans):
    print(ans[0], ans[1])

def program():
    src_str = read_input()
    src_chars = to_char_list(src_str)
    tokens = filter_spaces(src_chars)
    tokens = append_eof(tokens)
    cur = initial_position()
    ans, _ = parse_formula(tokens, cur)
    print_result(ans)

program()