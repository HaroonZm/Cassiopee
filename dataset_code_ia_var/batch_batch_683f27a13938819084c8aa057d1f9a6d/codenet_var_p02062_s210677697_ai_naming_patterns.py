input_char_list = list(str(input()))
token_list = [character for character in input_char_list if character != " "]
token_list.append("")
token_index = 0

def parse_expression():
    return parse_or_expression()

def parse_or_expression():
    global token_index
    left_expr = parse_and_expression()
    if token_list[token_index] == "|":
        token_index += 1
        right_expr = parse_or_expression()
        or_zero = left_expr[0] + right_expr[0]
        or_one = min(left_expr[1], left_expr[0] + right_expr[1])
        return (or_zero, or_one)
    return left_expr

def parse_and_expression():
    global token_index
    left_expr = parse_primary()
    if token_list[token_index] == "&":
        token_index += 1
        right_expr = parse_and_expression()
        and_zero = min(left_expr[0], left_expr[1] + right_expr[0])
        and_one = left_expr[1] + right_expr[1]
        return (and_zero, and_one)
    return left_expr

def parse_primary():
    global token_index
    if token_list[token_index] == "?":
        token_index += 1
        return [1, 1]
    elif token_list[token_index] == "(":
        token_index += 1
        inner_expr = parse_or_expression()
        if token_list[token_index] != ")":
            raise Exception("Parenthesis not closed")
        token_index += 1
        return inner_expr

result_tuple = parse_expression()
print(result_tuple[0], result_tuple[1])