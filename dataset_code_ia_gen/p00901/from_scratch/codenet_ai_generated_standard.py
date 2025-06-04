import sys
sys.setrecursionlimit(10**7)

MOD = 2011

def mod_inv(a, m=MOD):
    # Fermat's little theorem since MOD is prime
    return pow(a, m - 2, m)

class Cell:
    __slots__ = ['top','bot','h','w','data','base']
    def __init__(self, data, base):
        self.data = data
        self.h = len(data)
        self.w = len(data[0]) if self.h > 0 else 0
        self.top = 0
        self.bot = self.h - 1
        self.base = base

def trim(data):
    # trim rows and columns all '.' from top,bottom,left,right
    top = 0
    while top < len(data) and all(c == '.' for c in data[top]):
        top += 1
    if top == len(data):
        return ['']
    bot = len(data) - 1
    while bot >= 0 and all(c == '.' for c in data[bot]):
        bot -= 1
    data = data[top:bot+1]
    left = 0
    while left < len(data[0]) and all(row[left] == '.' for row in data):
        left += 1
    right = len(data[0]) - 1
    while right >= 0 and all(row[right] == '.' for row in data):
        right -= 1
    new_data = [row[left:right+1] for row in data]
    return new_data

def split_cells(line):
    # split line into cells by spaces (periods represent spaces)
    cells = []
    start = None
    for i,c in enumerate(line):
        if c != '.':
            if start is None:
                start = i
        else:
            if start is not None:
                cells.append((start,i-1))
                start = None
    if start is not None:
        cells.append((start,len(line)-1))
    return cells

def find_vinculum(lines):
    # find a line with >=3 consecutive hyphens: return line index and start,end col inclusive
    for i,line in enumerate(lines):
        run_len = 0
        start = None
        for j,ch in enumerate(line):
            if ch == '-':
                if run_len == 0:
                    start = j
                run_len += 1
            else:
                if run_len >= 3:
                    return i,start,j-1
                run_len = 0
        if run_len >=3:
            return i,start,len(line)-1
    return None

def parse_cell(lines, base_line):
    lines = trim(lines)
    if len(lines) == 0 or all(line == '' for line in lines):
        return None,None
    h = len(lines)
    w = len(lines[0])
    # If single character cell (terminal)
    if h == 1 and w == 1:
        ch = lines[0][0]
        if ch in '0123456789+-*().':
            return Cell(lines,base_line), ch
        # Unknown single char - still treat as terminal
        return Cell(lines,base_line), ch

    # Check fraction pattern (rule VI)
    vinc = find_vinculum(lines)
    if vinc is not None:
        # fraction: vinculum line and col
        i, s, e = vinc
        width = e - s + 1
        # get top expr (dividend)
        top_lines = lines[:i]
        # get bottom expr (divisor)
        bottom_lines = lines[i+1:]
        # Trim top_lines and bottom_lines horizontally centered on vinculum
        # find left/right spaces to pad for dividend and divisor per spec
        # dividend and divisor widths w1,w2 <= width-2; w1 = max width of dividend cell; w2 similarly divisor

        # They may have trailing spaces or dots, trim horizontally
        top_lines = [line[s:e+1] for line in top_lines]
        bottom_lines = [line[s:e+1] for line in bottom_lines]
        # Remove leading/trailing dots vertically for dividend top_lines
        top_trim = trim(top_lines)
        bottom_trim = trim(bottom_lines)
        # base line of fraction is vinculum line i relative in global cell height -> for dividend and divisor shifted accordingly

        dividend_cell, dividend_val = parse_cell(top_trim, len(top_trim)-1)
        divisor_cell, divisor_val = parse_cell(bottom_trim, 0)
        # Return fraction cell: base line is vinculum line i
        class FractionCell(Cell):
            __slots__ = ['dividend','divisor']
            def __init__(self, dividend, divisor, base):
                self.dividend = dividend
                self.divisor = divisor
                # data is combined lines with vinculum and spaces - not needed for evaluation
                # set h,w and base from arguments
                self.base = base
            def __repr__(self):
                return f"Fraction({self.dividend},{self.divisor})"
        fr_cell = FractionCell(dividend_cell, divisor_cell, base_line)
        return fr_cell, ('fraction', dividend_val, divisor_val)

    # Check powexpr (rule V)
    # Definition: powexpr = primary + optional digit at 1 line above base_line horizontally adjacent right
    # So find if one line above base_line there is a digit adjacent right to some primary cell

    # Find all connected cells horizontally on base_line
    # First split lines by spaces ('.'), parse children and align base lines

    # We parse with composing expr -> term -> factor etc, based on top lines and rules.
    # Here we use a top-down approach per spec:

    # try parse digit at base_line-1 line, right adjacent
    if base_line > 0:
        # Try parse primary below and digit above
        # leftmost non-dot cell in base_line line
        # find ranges of non-dot in base_line line
        line_base = lines[base_line]
        cells_at_base = split_cells(line_base)
        for idx,(l,r) in enumerate(cells_at_base):
            # for primary candidate
            primary_part = [line_base[l:r+1]]
            # get lines between base_line and next base line if needed

            # this primary candidate cell coords in all lines
            primary_lines = []
            for row in range(len(lines)):
                if row == base_line or (l<=len(lines[row])-1<r) or (r < len(lines[row]) and lines[row][r] != '.'):
                    # take substring from l to r for all lines in cell height
                    if len(lines[row])>=r+1:
                        primary_lines.append(lines[row][l:r+1])
                    else:
                        primary_lines.append('.'*(r-l+1))
                else:
                    primary_lines.append('.'*(r-l+1))
            # they are left aligned -- so just trim the block
            primary_lines = trim(primary_lines)
            primary_cell, primary_val = parse_cell(primary_lines, base_line)
            if primary_cell is None:
                continue

            # check if line above base_line has a digit cell right adjacent to primary cell
            above_line = lines[base_line-1] if base_line-1>=0 else ''
            if above_line and r+1 < len(above_line):
                if above_line[r+1] in '0123456789':
                    pow_digit = above_line[r+1]
                    # Make powexpr cell
                    class PowExprCell(Cell):
                        __slots__ = ['primary', 'digit']
                        def __init__(self, primary, digit, base):
                            self.primary = primary
                            self.digit = digit
                            self.base = base
                        def __repr__(self):
                            return f"PowExpr({self.primary},{self.digit})"
                    pow_cell = PowExprCell(primary_cell, pow_digit, base_line)
                    return pow_cell, ('powexpr', primary_val, pow_digit)

    # parse digits, terminals (single char)
    # parenthesis or expressions with terms and factors separated by + - *

    # If entire lines is single line and single digit
    if h == 1:
        s = ''.join(lines[0])
        if len(s) == 1 and s[0] in '0123456789+-*().':
            return Cell(lines,base_line), s[0]

    # Remove external parentheses wrapping all if any
    # Check if first char '(' last char ')' for entire lines
    if lines[base_line][0] == '(' and lines[base_line][-1] == ')':
        # check if matching parentheses - naive since BNF
        # Just remove them and parse inside
        new_lines = []
        for row in range(h):
            new_lines.append(lines[row][1:-1])
        new_lines = trim(new_lines)
        res_cell, res_val = parse_cell(new_lines, base_line)
        if res_cell is not None:
            return res_cell, res_val

    # Now split by top-level + and - (not counting inside parentheses)
    # Also support * with higher precedence

    # Build string and parse with minimal precedence + and - at top-level
    # Construct a string per col from base line to do token scan for operators outside parentheses

    def to_str(lines):
        return [''.join(row) for row in lines]

    s_lines = to_str(lines)
    s = s_lines[base_line]
    # find plus or minus at base_line line where not in parentheses
    def find_op_outside_paren(s, ops):
        res = []
        depth=0
        for i,ch in enumerate(s):
            if ch == '(':
                depth+=1
            elif ch == ')':
                depth-=1
            elif depth == 0 and ch in ops:
                res.append((i,ch))
        return res

    ops = find_op_outside_paren(s, '+-')
    # If + or - found at top level, split expression on these ops and parse parts recursively (left to right)
    if ops:
        cells = []
        vals = []
        last = 0
        last_op = None
        for pos,ch in ops:
            # parse substring lines of region last -> pos-1
            sub_lines = []
            for row in range(h):
                sub_lines.append(lines[row][last:pos])
            sub_lines = trim(sub_lines)
            c,v = parse_cell(sub_lines, base_line)
            if c is None:
                continue
            cells.append((c,v))
            vals.append(v)
            cells.append(ch)
            last = pos+1
        # last segment
        sub_lines = []
        for row in range(h):
            sub_lines.append(lines[row][last:])
        sub_lines = trim(sub_lines)
        c,v = parse_cell(sub_lines, base_line)
        if c is not None:
            cells.append((c,v))
            vals.append(v)

        # Evaluate left to right for + and -
        def eval_nodes(nodes):
            val = eval_expr(nodes[0][1])
            i = 1
            while i < len(nodes):
                op = nodes[i]
                v2 = eval_expr(nodes[i+1][1])
                if op == '+':
                    val = (val + v2) % MOD
                elif op == '-':
                    val = (val - v2) % MOD
                i += 2
            return val
        # for evaluation only
        return Cell(lines,base_line), ('expr', cells)

    # Else split by * operators (higher precedence)
    ops = find_op_outside_paren(s, '*')
    if ops:
        cells = []
        vals = []
        last = 0
        last_op = None
        for pos,ch in ops:
            sub_lines = []
            for row in range(h):
                sub_lines.append(lines[row][last:pos])
            sub_lines = trim(sub_lines)
            c,v = parse_cell(sub_lines, base_line)
            if c is None:
                continue
            cells.append((c,v))
            cells.append(ch)
            last = pos+1
        sub_lines = []
        for row in range(h):
            sub_lines.append(lines[row][last:])
        sub_lines = trim(sub_lines)
        c,v = parse_cell(sub_lines, base_line)
        if c is not None:
            cells.append((c,v))
        return Cell(lines,base_line), ('term', cells)

    # unary minus and plus
    if s and s[0] in '+-':
        # parse unary op + operand recursively
        sign = s[0]
        sub_lines = []
        for row in range(h):
            sub_lines.append(lines[row][1:])
        sub_lines = trim(sub_lines)
        c,v = parse_cell(sub_lines, base_line)
        if c is not None:
            return Cell(lines,base_line), ('factor', [sign,v])
    # digits or parentheses just return
    if h == 1:
        val = s.strip('.')
        if val.isdigit():
            return Cell(lines,base_line), val
        # just return
        return Cell(lines,base_line), s

    # default return as is
    return Cell(lines,base_line), s

def eval_expr(ast):
    if isinstance(ast, str):
        if ast.isdigit():
            return int(ast) % MOD
        if ast in '+-':
            # unary plus/minus without number return 0 or something
            return 0
        return 0
    if isinstance(ast, tuple):
        kind = ast[0]
        if kind == 'fraction':
            _, num_ast, den_ast = ast
            x = eval_expr(num_ast)
            y = eval_expr(den_ast)
            y_inv = mod_inv(y)
            return (x * y_inv) % MOD
        if kind == 'powexpr':
            _, base_ast, digit = ast
            base = eval_expr(base_ast)
            e = int(digit)
            if e == 0:
                return 1
            return pow(base, e, MOD)
        if kind == 'expr':
            nodes = ast[1]
            val = eval_expr(nodes[0][1])
            i = 1
            while i < len(nodes):
                op = nodes[i]
                v2 = eval_expr(nodes[i+1][1])
                if op == '+':
                    val = (val + v2) % MOD
                elif op == '-':
                    val = (val - v2) % MOD
                i += 2
            return val
        if kind == 'term':
            nodes = ast[1]
            val = 1
            for node in nodes:
                if isinstance(node, tuple):
                    val = (val * eval_expr(node[1])) % MOD
            return val
        if kind == 'factor':
            sign, val_ast = ast[1]
            val = eval_expr(val_ast)
            if sign == '-':
                val = (-val) % MOD
            return val
    if isinstance(ast, list):
        # product or sum list
        val = 0
        for a in ast:
            val += eval_expr(a)
        return val % MOD
    # else default fallback
    return 0

def main():
    lines_iter = iter(sys.stdin.read().rstrip('\n').split('\n'))
    while True:
        try:
            n_line = next(lines_iter)
        except StopIteration:
            break
        if n_line == '0':
            break
        n = int(n_line)
        data = [next(lines_iter).replace(' ', '.') for _ in range(n)]
        # parse root cell, baseline is set to the line containing the main line (heuristic)
        base_line = n//2
        root_cell, ast = parse_cell(data, base_line)
        res = eval_expr(ast)
        print(res % MOD)

if __name__ == '__main__':
    main()