import sys

def parse_expr(expr, arrays, assigned, line_num):
    # expr can be a number or array access: array_name[expr]
    if expr.isdigit():
        return int(expr), None
    # else array access
    # find array name and inner expr
    i = expr.find('[')
    arr_name = expr[:i]
    inner_expr = expr[i+1:-1]
    val, bug = parse_expr(inner_expr, arrays, assigned, line_num)
    if bug is not None:
        return None, bug
    # check index validity
    if arr_name not in arrays:
        # should not happen as per problem statement (arrays always declared before use)
        return None, line_num
    size = arrays[arr_name]
    if val < 0 or val >= size:
        return None, line_num
    # check if assigned
    if (arr_name, val) not in assigned:
        return None, line_num
    return assigned[(arr_name, val)], None


def main():
    lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(lines):
            break
        # read one dataset
        dataset_lines = []
        while idx < len(lines) and lines[idx] != '.':
            dataset_lines.append(lines[idx])
            idx += 1
        idx += 1  # skip the period line
        if len(dataset_lines) == 0:
            break
        # parse dataset
        arrays = {}
        assigned = {}
        bug_line = 0
        # line count for assignment lines
        assign_line_num = 0
        for i, line in enumerate(dataset_lines):
            line = line.strip()
            if '=' not in line:
                # declaration
                # format: name[size]
                arr_name = line[:line.index('[')]
                size = int(line[line.index('[')+1:-1])
                arrays[arr_name] = size
            else:
                # assignment
                assign_line_num += 1
                lhs, rhs = line.split('=')
                lhs = lhs.strip()
                rhs = rhs.strip()
                # parse lhs array access
                i1 = lhs.find('[')
                lhs_arr = lhs[:i1]
                lhs_expr = lhs[i1+1:-1]
                # get lhs index
                idx_val, bug = parse_expr(lhs_expr, arrays, assigned, assign_line_num)
                if bug is not None:
                    bug_line = assign_line_num
                    break
                # check lhs index validity
                if lhs_arr not in arrays:
                    bug_line = assign_line_num
                    break
                if idx_val < 0 or idx_val >= arrays[lhs_arr]:
                    bug_line = assign_line_num
                    break
                # parse rhs expression
                val, bug = parse_expr(rhs, arrays, assigned, assign_line_num)
                if bug is not None:
                    bug_line = assign_line_num
                    break
                # assign value
                assigned[(lhs_arr, idx_val)] = val
        print(bug_line)

if __name__ == '__main__':
    main()