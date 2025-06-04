def update_cnt_and_find_brackets(i, l, r, S, cnt, left, right):
    if S[i] == '(':
        cnt += 1
    elif S[i] == ')':
        cnt -= 1
    elif cnt == 0:
        left, right = find_bracket_indices(S, i, left, right)
    return cnt, left, right

def find_bracket_indices(S, i, left, right):
    if S[i] == "[":
        left = i
    elif S[i] == "]":
        right = i
    return left, right

def parse_node_loop(l, r, S):
    left, right = 0, 0
    cnt = 0
    for i in range(l, r + 1):
        cnt, left, right = update_cnt_and_find_brackets(i, l, r, S, cnt, left, right)
    return left, right

def extract_node_indices(l, r, S):
    return parse_node_loop(l, r, S)

def get_substring(S, start, end):
    return S[start:end]

def get_num_from_brackets(S, left, right):
    return int(S[left + 1:right])

def make_sum_node(val1, val2):
    return "[{}]".format(val1 + val2)

def get_left_range(l1, n1_l, l2, n2_l):
    return l1 + 1, n1_l - 2, l2 + 1, n2_l - 2

def get_right_range(n1_r, r1, n2_r, r2):
    return n1_r + 2, r1 - 1, n2_r + 2, r2 - 1

def is_empty_node(n1_l, l1, n2_l, l2):
    return min(n1_l - l1, n2_l - l2) <= 2

def is_empty_right(r1, n1_r, r2, n2_r):
    return min(r1 - n1_r, r2 - n2_r) <= 2

def wrap_paren(s):
    return "({})".format(s)

def parser(l1, r1, l2, r2):
    n1_l, n1_r = extract_node_indices(l1, r1, S1)
    n2_l, n2_r = extract_node_indices(l2, r2, S2)
    val1 = get_num_from_brackets(S1, n1_l, n1_r)
    val2 = get_num_from_brackets(S2, n2_l, n2_r)
    node = make_sum_node(val1, val2)
    left_str = get_left_string(l1, n1_l, l2, n2_l, r1, r2)
    right_str = get_right_string(r1, n1_r, r2, n2_r, n1_l, n1_r, n2_l, n2_r)
    return left_str + node + right_str

def get_left_string(l1, n1_l, l2, n2_l, r1, r2):
    if is_empty_node(n1_l, l1, n2_l, l2):
        return wrap_paren("")
    else:
        new_l1, new_r1, new_l2, new_r2 = get_left_range(l1, n1_l, l2, n2_l)
        return wrap_paren(parser(new_l1, new_r1, new_l2, new_r2))

def get_right_string(r1, n1_r, r2, n2_r, n1_l, n1_r, n2_l, n2_r):
    if is_empty_right(r1, n1_r, r2, n2_r):
        return wrap_paren("")
    else:
        new_l1, new_r1, new_l2, new_r2 = get_right_range(n1_r, r1, n2_r, r2)
        return wrap_paren(parser(new_l1, new_r1, new_l2, new_r2))

def main():
    global S1, S2
    S1 = input()
    S2 = input()
    result = parser(0, len(S1) - 1, 0, len(S2) - 1)
    print(result)

main()