import sys

def solve_program(lines):
    arrays = {}
    assigned = {}
    def eval_expr(expr):
        # expr is either a number or array access like name[expr]
        if expr.isdigit():
            return int(expr)
        else:
            # array access: name[expr]
            i = expr.find('[')
            name = expr[:i]
            inside = expr[i+1:-1]
            idx = eval_expr(inside)
            if name not in arrays:
                return None, 'undeclared'
            size = arrays[name]
            if idx < 0 or idx >= size:
                return None, 'index'
            if (name, idx) not in assigned:
                return None, 'unset'
            return assigned[(name, idx)], None

    line_no = 0
    for line in lines:
        line_no += 1
        line = line.strip()
        if not line:
            continue
        if '=' not in line:
            # Declaration: a[n]
            i1 = line.find('[')
            i2 = line.find(']')
            name = line[:i1]
            n = int(line[i1+1:i2])
            arrays[name] = n
        else:
            # Assignment: lhs=rhs
            lhs, rhs = line.split('=')
            lhs = lhs.strip()
            rhs = rhs.strip()
            # parse lhs: name[expr]
            i1 = lhs.find('[')
            i2 = lhs.find(']')
            lhs_name = lhs[:i1]
            lhs_expr = lhs[i1+1:i2]
            # eval lhs index
            idx, err = None, None
            if lhs_expr.isdigit():
                idx = int(lhs_expr)
            else:
                ret, err = eval_expr(lhs_expr)
                idx = ret
            if lhs_name not in arrays:
                return line_no
            size = arrays[lhs_name]
            if idx is None or idx < 0 or idx >= size:
                return line_no
            if err is not None:
                return line_no
            # eval rhs value
            if rhs.isdigit():
                val = int(rhs)
            else:
                val, err = eval_expr(rhs)
                if err is not None or val is None:
                    return line_no
            assigned[(lhs_name, idx)] = val
    return 0

def main():
    lines = []
    for line in sys.stdin:
        line=line.rstrip('\n')
        if line == '.':
            if lines:
                print(solve_program(lines))
                lines = []
            else:
                break
        else:
            lines.append(line)

if __name__ == "__main__":
    main()