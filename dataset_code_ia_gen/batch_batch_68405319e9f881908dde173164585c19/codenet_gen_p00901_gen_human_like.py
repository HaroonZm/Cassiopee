import sys
sys.setrecursionlimit(10000)

MOD = 2011

def modinv(a, m=MOD):
    # Fermat's little theorem since MOD is prime
    return pow(a, m - 2, m)

class Cell:
    def __init__(self, lines, top):
        self.lines = lines
        self.top = top
        self.height = len(lines)
        self.width = len(lines[0])
        self.bottom = top + self.height - 1

def trim(cell_lines):
    # remove empty rows and columns (only '.' allowed)
    rows = cell_lines
    # remove empty rows top
    while rows and all(c == '.' for c in rows[0]):
        rows = rows[1:]
    # remove empty rows bottom
    while rows and all(c == '.' for c in rows[-1]):
        rows = rows[:-1]
    if not rows:
        return []
    w = len(rows[0])
    left = 0
    right = w - 1
    # remove empty cols left
    while left <= right and all(row[left] == '.' for row in rows):
        left += 1
    # remove empty cols right
    while right >= left and all(row[right] == '.' for row in rows):
        right -= 1
    if left > right:
        return []
    trimmed = [row[left:right+1] for row in rows]
    return trimmed

def is_digit(c):
    return '0' <= c <= '9'

def parse_lines(lines):
    n = len(lines)
    w = len(lines[0])
    return [list(line) for line in lines]

class Parser:
    def __init__(self, lines):
        self.lines_all = lines
        self.height = len(lines)
        self.width = len(lines[0])
        self.visited = set()
        # for parsing, store lines
        self.lines = lines
    
    def cell_at(self, top, left, h, w):
        # extract cell portion from self.lines
        # returns list of strings
        cell = [self.lines[top + i][left:left + w] for i in range(h)]
        return cell

    def is_empty_cell(self, cell):
        for row in cell:
            for ch in row:
                if ch != '.':
                    return False
        return True

    def cell_trim(self, top, left, h, w):
        # returns trimmed cell and new coordinates top', left'
        subcell = [self.lines[top+i][left:left+w] for i in range(h)]
        trimmed = trim(subcell)
        if not trimmed:
            return None,None,None,None
        ntop = 0
        for i in range(h):
            if all(x == '.' for x in self.lines[top+i][left:left+w]):
                ntop += 1
            else:
                break
        # count left trim
        nleft = 0
        lh = len(trimmed)
        lw = len(trimmed[0])
        for j in range(w):
            if all(self.lines[top+i][left+j] == '.' for i in range(h)):
                nleft += 1
            else:
                break
        return trimmed, top + ntop, left + nleft, len(trimmed), len(trimmed[0])

    def get_top_and_bottom_lines(self, cell_lines, top):
        # returns top line index, bottom line index
        return top, top + len(cell_lines) - 1

    def slice_region(self, top, bottom, left, right):
        # returns list of strings (lines from top to bottom, left to right)
        out = []
        for i in range(top, bottom + 1):
            out.append(self.lines[i][left:right + 1])
        return out

    def find_vinculum(self, top, bottom):
        # locate a row full of hyphens '-' (3 or more)
        for i in range(top, bottom + 1):
            row = self.lines[i]
            l = len(row)
            count = 0
            starts = []
            for j in range(l):
                if row[j] == '-':
                    count += 1
                else:
                    if count >= 3:
                        starts.append(j - count)
                    count = 0
            if count >= 3:
                starts.append(l - count)
            if starts:
                # return first occurrence start, length, line index
                for s in starts:
                    length = 0
                    while s + length < l and self.lines[i][s+length] == '-':
                        length += 1
                    if length >= 3:
                        return i, s, length
        return -1,-1,-1

    def find_top_bottom_dividend_and_divisor(self, vinc_top, vinc_line, vinc_len):
        # return dividend and divisor (top, height, left, width)
        # vinc_line - line index of vinculum
        # vinc_top - top line of whole cell
        # find dividend above vinc_line - region of consecutive lines centered around vinculum horizontally
        # and divisor below vinc_line similarly
        # find dividend: lines just above vinc_line that are non-empty
        # find divisor: lines just below vinc_line that are non-empty
        l = vinc_line
        col_start = vinc_top
        # The vinculum horizontal range is [vinc_line][vinc_s:vinc_s+vinc_len]
        # The vinculum is located at (vinc_line, vinc_s) horizontal span vinc_len
        # Need to find dividend region just above vinc_line that is centered horizontally wrt vinculum
        # and divisor region just below vinc_line similarly
        # But we have access to the whole expression splitted into lines, parser covers whole global cell
        # For dividends and divisors we must find their columns:
        # Each dividend and divisor has width w1, w2. vinc_len = 2 + max(w1, w2)
        # dividend and divisor are centered:
        # spaces left = ceil((vinc_len - wk)/2)
        # spaces right = floor((vinc_len - wk)/2)
        # So the dividend span horizontally goes from vinc_s + spaces_left to vinc_s + spaces_left + wk - 1
        # We find dividend and divisor by detecting their extents.
        return None

    def parse_expr(self, top, bottom, left, right):
        # expr := term { + term | - term }
        # parse left to right with + or -
        vals = []
        ops = []
        # parse term +/-
        pos = left
        # split at top line by tokens separated by '.'
        # expression is on base-line
        base_line = bottom
        tokens = []
        cur_token_left = None
        for i in range(left, right+1):
            c = self.lines[base_line][i]
            if c != '.':
                if cur_token_left is None:
                    cur_token_left = i
            else:
                if cur_token_left is not None:
                    tokens.append((cur_token_left, i-1))
                    cur_token_left = None
        if cur_token_left is not None:
            tokens.append((cur_token_left, right))
        # parse tokens as terms and operators
        # for each token recursively parse term
        res_vals = []
        res_ops = []
        for idx,(lft,rgt) in enumerate(tokens):
            # check if token is operator + or -
            if lft == rgt and self.lines[base_line][lft] in ['+', '-']:
                res_ops.append(self.lines[base_line][lft])
            else:
                val = self.parse_term(top, bottom, lft, rgt)
                res_vals.append(val)
        # now compute
        if not res_vals:
            return 0
        result = res_vals[0]
        for i,op in enumerate(res_ops):
            v = res_vals[i+1]
            if op == '+':
                result = (result + v) % MOD
            else:
                result = (result - v) % MOD
        return result

    def parse_term(self, top, bottom, left, right):
        # term := factor { * factor }
        # base-line pass is bottom line
        base_line = bottom
        # split by '*'
        splits = []
        cur_left = left
        i = left
        while i <= right:
            c = self.lines[base_line][i]
            if c == '*':
                if i > cur_left:
                    splits.append((cur_left, i-1))
                splits.append((i,i))  # operator
                cur_left = i+1
            i += 1
        if cur_left <= right:
            splits.append((cur_left,right))
        # parse factors and ops
        vals = []
        ops = []
        for sp in splits:
            lft,rgt = sp
            if lft == rgt and self.lines[base_line][lft] == '*':
                ops.append('*')
            else:
                val = self.parse_factor(top, bottom, lft, rgt)
                vals.append(val)
        if not vals:
            return 0
        result = vals[0]
        for i,op in enumerate(ops):
            v = vals[i+1]
            result = (result * v) % MOD
        return result

    def parse_factor(self, top, bottom, left, right):
        # factor := int | ( expr ) | fraction | unary minus factor | powexpr
        # check if unary minus
        base_line = bottom
        if left <= right and self.lines[base_line][left] == '-':
            # unary minus
            val = self.parse_factor(top, bottom, left+1, right)
            return (-val) % MOD

        # check fraction
        vinc_line, vinc_s, vinc_len = self.find_vinculum(top, bottom)
        if vinc_line != -1:
            # fraction must fit horizontally inside left,right (vinc_line in [top,bottom])
            if vinc_s >= left and vinc_s + vinc_len - 1 <= right and vinc_line >= top and vinc_line <= bottom:
                # get dividend and divisor cells horizontally centered with respect to vinculum
                max_w = vinc_len - 2
                # dividend above vinc_line
                above_top = top
                above_bottom = vinc_line - 1
                below_top = vinc_line + 1
                below_bottom = bottom
                # find dividend width by looking at lines above the vinculum, removing padding
                dividend_lines = self.lines[above_top:above_bottom + 1] if above_bottom >= above_top else []
                divisor_lines = self.lines[below_top:below_bottom + 1] if below_bottom >= below_top else []

                # Calculate width of dividend and divisor cells (roughly by counting max width non-empty region)
                def cell_dim(lines):
                    if not lines:
                        return 0,0
                    h = len(lines)
                    maxw = 0
                    for row in lines:
                        lfti = 0
                        while lfti < len(row) and row[lfti] == '.':
                            lfti += 1
                        rhti = len(row)-1
                        while rhti >= 0 and row[rhti] == '.':
                            rhti -= 1
                        if rhti >= lfti:
                            maxw = max(maxw, rhti - lfti + 1)
                    return h, maxw
                h_d, w_d = cell_dim(dividend_lines)
                h_v, w_v = cell_dim(divisor_lines)
                w_dividend = w_d
                w_divisor = w_v
                # vinc_len = 2 + max(w_dividend, w_divisor)
                # dividend left offset
                space_left_dividend = (vinc_len - w_dividend + 1)//2
                space_left_divisor = (vinc_len - w_divisor + 1)//2
                # get dividend cell coordinates relative to vinc_line
                div_left = vinc_s + space_left_dividend
                div_right = div_left + w_dividend - 1
                div_top = above_top
                div_bottom = above_bottom
                # get divisor cell coordinates
                div2_left = vinc_s + space_left_divisor
                div2_right = div2_left + w_divisor - 1
                div2_top = below_top
                div2_bottom = below_bottom

                if div_top > div_bottom:
                    # dividend missing means 0
                    numerator = 0
                else:
                    numerator = self.parse_expr(div_top, div_bottom, div_left, div_right)
                if div2_top > div2_bottom:
                    denominator = 1
                else:
                    denominator = self.parse_expr(div2_top, div2_bottom, div2_left, div2_right)
                inv_den = modinv(denominator)
                return (numerator * inv_den) % MOD
        
        # check parentheses: if expression surrounded by '(' and ')'
        if self.lines[bottom][left] == '(' and self.lines[bottom][right] == ')':
            # find matching ')', check inside parse expr inside
            return self.parse_expr(top, bottom, left+1, right-1)

        # check powexpr: primary + optional digit above base-line and to the right (adjacent)
        # Need to find primary base, and digit above, horizontally adjacent
        # base line is bottom
        # Try to find digit above bottom line, at position right+1 or so
        # check primary is cell inside [top:bottom, left:right]
        primary_val = self.parse_primary(top, bottom, left, right)
        # Try to find digit at line bottom-1, column right+1 if it exists
        if bottom > 0 and right + 1 < self.width:
            c = self.lines[bottom - 1][right + 1]
            if is_digit(c):
                digit_val = int(c)
                return pow(primary_val, digit_val, MOD)
        return primary_val

    def parse_primary(self, top, bottom, left, right):
        # primary := digit | ( expr )
        # check digit single char
        if top == bottom and left == right and is_digit(self.lines[top][left]):
            return int(self.lines[top][left])
        # parentheses
        if left < right and self.lines[bottom][left] == '(' and self.lines[bottom][right] == ')':
            return self.parse_expr(top, bottom, left+1, right-1)
        # unary minus in primary possible? No, unary minus applies in factor
        # otherwise parse expr inside
        return self.parse_expr(top, bottom, left, right)
    
    def solve(self):
        return self.parse_expr(0, self.height-1, 0, self.width-1)

def main():
    input = sys.stdin.read().rstrip('\n')
    lines = input.split('\n')
    idx = 0
    while True:
        if idx >= len(lines):
            break
        n = lines[idx].strip()
        idx += 1
        if n == '0':
            break
        n = int(n)
        expr_lines = []
        for _ in range(n):
            l = lines[idx]
            idx += 1
            # replace '.' with ' ' ?
            expr_lines.append(list(l))
        parser = Parser(expr_lines)
        res = parser.solve()
        print(res % MOD)

if __name__ == '__main__':
    main()