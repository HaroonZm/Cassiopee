import sys
import operator
import functools

def deref(d, expr):
    """
    Advanced version using functools.reduce and operator.getitem for deep access
    Parses nested expressions like 'A[B[C]]' and resolves them recursively.
    """
    # Remove all ']' and split at '['
    tokens = expr.replace(']', '').split('[')
    # If there's only one token, it's either a variable or a literal
    if len(tokens) == 1:
        return tokens[0].isdigit() and tokens[0] or tokens[0]
    # Resolve indices recursively from innermost to outermost
    while len(tokens) > 1:
        key, idx = tokens[-2], tokens[-1]
        idx_resolved = deref(d, idx)
        value = d.get(key, {}).get(idx_resolved)
        if value is None:
            return None
        tokens = tokens[:-2] + [value]
    return tokens[0]

def check(stmts):
    d, capacity = {}, {}
    for i, stmt in enumerate(stmts, 1):
        if '=' not in stmt:
            var, idx = stmt[0], stmt[2:-1]
            d[var] = {}
            capacity[var] = int(idx)
            continue

        lhs, rhs = map(str.strip, stmt.split('='))
        var, idx_expr = lhs[0], lhs[2:-1]
        idx_val = deref(d, idx_expr)
        rhs_val = deref(d, rhs)
        if (idx_val is None or rhs_val is None or
            not idx_val.isdigit() or int(idx_val) >= capacity[var]):
            print(i)
            return
        d[var][idx_val] = rhs_val
    print(0)

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    batches = []
    batch = []
    for line in lines:
        if line == '.':
            if batch:
                batches.append(batch)
                batch = []
        else:
            batch.append(line)
    if batch:  # In case the last batch isn't followed by '.'
        batches.append(batch)
    for batch in batches:
        check(batch)

if __name__ == '__main__':
    main()