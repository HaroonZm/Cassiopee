def main():
    s1 = input()
    s2 = input()
    t1 = convert(s1)
    t2 = convert(s2)
    result = dfs(t1, t2)
    output_str = stringify(result)
    print(output_str)

def convert(S):
    cur = [0]
    return _parse(S, cur)

def _parse(S, cur):
    if _is_close_paren(S, cur):
        return _empty_tuple()
    _increment(cur, 1)
    left = _parse(S, cur)
    _increment(cur, 2)
    num = _parse_number(S, cur)
    _increment(cur, 2)
    right = _parse(S, cur)
    _increment(cur, 1)
    return _make_tuple(left, num, right)

def _is_close_paren(S, cur):
    return S[cur[0]] == ')'

def _empty_tuple():
    return ()

def _increment(cur, amount):
    cur[0] += amount

def _parse_number(S, cur):
    num = 0
    while not _is_close_bracket(S, cur):
        num = _aggregate_number(num, S, cur)
        _increment(cur, 1)
    return num

def _is_close_bracket(S, cur):
    return S[cur[0]] == ']'

def _aggregate_number(num, S, cur):
    return 10 * num + int(S[cur[0]])

def _make_tuple(left, num, right):
    return (left, num, right)

def dfs(A, B):
    if _is_empty_node(A) or _is_empty_node(B):
        return _empty_tuple()
    left = dfs(_get_left(A), _get_left(B))
    val = [_get_value(A) + _get_value(B)]
    right = dfs(_get_right(A), _get_right(B))
    return _compose_node(left, val, right)

def _is_empty_node(node):
    return not node

def _get_left(node):
    return node[0]

def _get_value(node):
    return node[1]

def _get_right(node):
    return node[2]

def _compose_node(left, val, right):
    return (left, val, right)

def stringify(node):
    s = _node_to_str(node)
    s = _remove_commas(s)
    s = _trim_brackets(s)
    return s

def _node_to_str(node):
    return str(node)

def _remove_commas(s):
    return s.replace(", ","")

def _trim_brackets(s):
    return s[1:-1]

main()