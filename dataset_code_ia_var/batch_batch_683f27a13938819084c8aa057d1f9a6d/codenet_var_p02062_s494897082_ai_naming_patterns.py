import sys
sys.setrecursionlimit(2 * 10 ** 5)

TOKEN_QUESTION = 1
TOKEN_AND = -1
TOKEN_OR = -2
TOKEN_LEFT_PAREN = -3
TOKEN_RIGHT_PAREN = -4

TOKEN_MAP = {'?': TOKEN_QUESTION, '&': TOKEN_AND, '|': TOKEN_OR, '(': TOKEN_LEFT_PAREN, ')': TOKEN_RIGHT_PAREN}

def evaluate_or(node_list):
    if len(node_list) == 1:
        return node_list[0]
    res_min, res_max = node_list[0]
    for idx in range(1, len(node_list)):
        cur_min, cur_max = node_list[idx]
        res_min, res_max = res_min + cur_min, min(res_max, res_min + cur_max)
    return (res_min, res_max)

def stack_push(stack, value_tuple):
    if stack and stack[-1] == (TOKEN_AND, TOKEN_AND):
        stack.pop()
        prev_tuple = stack.pop()
        return stack_push(stack, evaluate_and(prev_tuple, value_tuple))
    else:
        stack.append(value_tuple)
        return stack

def evaluate_and(tuple_a, tuple_b):
    min_a, max_a = tuple_a
    min_b, max_b = tuple_b
    return (min(min_a, max_a + min_b), max_a + max_b)

input_tokens = [TOKEN_MAP[ch] for ch in input().strip()]
processing_stack = []

for token in input_tokens:
    if token == TOKEN_QUESTION:
        processing_stack = stack_push(processing_stack, (token, token))
    elif token == TOKEN_AND or token == TOKEN_LEFT_PAREN:
        processing_stack.append((token, token))
    elif token == TOKEN_RIGHT_PAREN:
        subexpr_nodes = []
        while processing_stack[-1] != (TOKEN_LEFT_PAREN, TOKEN_LEFT_PAREN):
            temp_tuple = processing_stack.pop()
            assert temp_tuple[0] > 0 and temp_tuple[1] > 0
            subexpr_nodes.append(temp_tuple)
        assert processing_stack.pop() == (TOKEN_LEFT_PAREN, TOKEN_LEFT_PAREN)
        stack_push(processing_stack, evaluate_or(subexpr_nodes[::-1]))

final_result = evaluate_or(processing_stack)
print(*final_result)