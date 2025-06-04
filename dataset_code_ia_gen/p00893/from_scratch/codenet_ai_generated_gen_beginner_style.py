M = 32768

import sys
sys.setrecursionlimit(10**7)

def mat_size(A):
    if isinstance(A, int):
        return 1,1
    return len(A), len(A[0])

def is_scalar(A):
    return isinstance(A, int) or (len(A) == 1 and len(A[0]) == 1)

def to_scalar(A):
    if isinstance(A,int):
        return A%M
    if len(A)==1 and len(A[0])==1:
        return A[0][0]%M
    return None

def scalar_to_mat(x,m,n):
    x = x % M
    return [[x]*n for _ in range(m)]

def mat_add(A,B):
    m,n = mat_size(A)
    C = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = (A[i][j]+B[i][j])%M
    return C

def mat_sub(A,B):
    m,n = mat_size(A)
    C = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = (A[i][j]-B[i][j])%M
    return C

def mat_neg(A):
    if isinstance(A,int):
        return (-A)%M
    m,n = mat_size(A)
    C = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = (-A[i][j])%M
    return C

def mat_transpose(A):
    m,n = mat_size(A)
    C = [[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]%M
    return C

def mat_mul(A,B):
    if isinstance(A,int) and isinstance(B,int):
        return (A*B)%M
    if isinstance(A,int):
        # scalar * matrix
        m,n = mat_size(B)
        x = A%M
        C = [[(x*B[i][j])%M for j in range(n)] for i in range(m)]
        return C
    if isinstance(B,int):
        m,n = mat_size(A)
        x = B%M
        C = [[(A[i][j]*x)%M for j in range(n)] for i in range(m)]
        return C
    mA,nA = mat_size(A)
    mB,nB = mat_size(B)
    # 1x1 matrix as scalar
    if mA==1 and nA==1:
        x = A[0][0]%M
        return mat_mul(x,B)
    if mB==1 and nB==1:
        x = B[0][0]%M
        return mat_mul(A,x)
    C = [[0]*nB for _ in range(mA)]
    for i in range(mA):
        for j in range(nB):
            s = 0
            for k in range(nA):
                s += A[i][k]*B[k][j]
            C[i][j] = s%M
    return C

def flatten_expr_to_matrix(expr):
    # expr is either int or [rows]
    # rows: list of rows, each row list of expr
    # flatten nested matrices:
    # if expr is int: return [[int]]
    # if expr is [[...], [...]]: merge rows
    if isinstance(expr,int):
        return [[expr%M]]
    # expr is list of rows, each row list of expr
    rows = []  # final rows (list of list of int)
    # Each row in expr can contain nested matrices, need to flatten horizontally
    for row in expr:
        # Each element of row can be int or nested matrix (list)
        # For each element, get flatten 2D matrix
        matrices = []
        for e in row:
            m = flatten_expr_to_matrix(e)
            matrices.append(m)
        # matrices is list of 2D matrices
        # check number of rows same
        rcount = None
        for mat in matrices:
            if rcount is None:
                rcount = len(mat)
            elif rcount != len(mat):
                # not consistent
                # but problem guarantees no semantic errors
                pass
        # For each row 0..rcount-1, concatenate horizontally
        for i in range(rcount):
            if len(rows)<=i:
                rows.append([])
            for mat in matrices:
                rows[i].extend(mat[i])
    return rows

def parse_int(token):
    return int(token)

class Parser:
    def __init__(self,text,vars):
        self.text = text
        self.pos = 0
        self.len = len(text)
        self.vars = vars

    def skip_ws(self):
        while self.pos<self.len and self.text[self.pos] in " \t\n\r":
            self.pos+=1

    def peek(self):
        self.skip_ws()
        if self.pos<self.len:
            return self.text[self.pos]
        return ''

    def get(self):
        self.skip_ws()
        if self.pos<self.len:
            ch = self.text[self.pos]
            self.pos+=1
            return ch
        return ''

    def parse_var(self):
        self.skip_ws()
        if self.pos<self.len:
            c = self.text[self.pos]
            if c.isupper():
                self.pos+=1
                return c
        return None

    def parse_number(self):
        self.skip_ws()
        start = self.pos
        while self.pos<self.len and self.text[self.pos].isdigit():
            self.pos+=1
        if start==self.pos:
            return None
        num = int(self.text[start:self.pos])
        return num

    def parse_factor(self):
        self.skip_ws()
        ch = self.peek()
        if ch == '-':
            self.get()
            f = self.parse_factor()
            return ('neg', f)
        else:
            return self.parse_primary()

    def parse_term(self):
        left = self.parse_factor()
        while True:
            self.skip_ws()
            c = self.peek()
            if c == '*':
                self.get()
                right = self.parse_factor()
                left = ('mul', left, right)
            else:
                break
        return left

    def parse_expr(self):
        left = self.parse_term()
        while True:
            self.skip_ws()
            c = self.peek()
            if c == '+':
                self.get()
                right = self.parse_term()
                left = ('add', left, right)
            elif c == '-':
                self.get()
                right = self.parse_term()
                left = ('sub', left, right)
            else:
                break
        return left

    def parse_index(self):
        # parse index like ([1 2],[3 4])
        self.skip_ws()
        if self.peek() != '(':
            return None
        self.get()
        ind1 = self.parse_index_matrix()
        self.skip_ws()
        if self.get() != ',':
            return None
        ind2 = self.parse_index_matrix()
        self.skip_ws()
        if self.get() != ')':
            return None
        return (ind1, ind2)

    def parse_index_matrix(self):
        # parse 1 x k matrix in parentheses or just parentheses with numbers
        self.skip_ws()
        if self.peek() == '[':
            mat = self.parse_matrix()
            rows = len(mat)
            cols = len(mat[0]) if rows>0 else 0
            if rows!=1:
                # must be 1-row matrix
                pass
            return mat[0]
        else:
            # parse numbers separated by spaces inside parentheses
            res = []
            while True:
                self.skip_ws()
                num = self.parse_number()
                if num is None:
                    break
                res.append(num)
            return res

    def parse_primary(self):
        self.skip_ws()
        c = self.peek()
        if c=='(':
            self.get()
            e = self.parse_expr()
            self.skip_ws()
            if self.get() != ')':
                pass
            # check indexed primary next
            lookahead = self.peek()
            if lookahead == '(':
                idx = self.parse_index()
                e = ('idx', e, idx)
            # possible transpose
            e = self.parse_transpose(e)
            return e
        elif c=='[':
            mat = self.parse_matrix()
            # convert matrix int/int exprs to AST of int or so
            return mat
        elif c.isdigit():
            num = self.parse_number()
            e = num
            e = self.parse_transpose(e)
            # check indexed primary
            if self.peek() == '(':
                idx = self.parse_index()
                e = ('idx', e, idx)
            return e
        elif c.isupper():
            var = self.parse_var()
            e = ('var', var)
            # check transpose chain
            e = self.parse_transpose(e)
            # check indexed primary
            if self.peek() == '(':
                idx = self.parse_index()
                e = ('idx', e, idx)
            return e
        else:
            # error
            return None

    def parse_transpose(self,e):
        # parse one or more '
        while True:
            self.skip_ws()
            if self.peek() == "'":
                self.get()
                e = ('trans', e)
            else:
                break
        return e

    def parse_matrix(self):
        self.skip_ws()
        if self.get() != '[':
            return None
        rows = []
        row = []
        while True:
            self.skip_ws()
            c = self.peek()
            if c == ']':
                if row:
                    rows.append(row)
                    row = []
                self.get()
                break
            elif c == ';':
                # end of row
                if row:
                    rows.append(row)
                    row=[]
                self.get()
            elif c == '[':
                # nested matrix
                m = self.parse_matrix()
                row.append(m)
            elif c == ',':
                self.get() # comma not expected in syntax, ignore
            else:
                # expect expression
                # parse expr inside row (complex expression allowed)
                # But in problem, reserved spaces separate expr in row,
                # So parse a number or nested matrix
                # To keep it simple, parse factor or expr not feasible here,
                # so parse number or nested matrix only
                if c == '-':
                    # parse unary minus number
                    self.get()
                    n = self.parse_number()
                    if n is None:
                        n=0
                    row.append((-n)%M)
                elif c.isdigit():
                    n = self.parse_number()
                    row.append(n%M)
                elif c.isupper():
                    v = self.parse_var()
                    row.append(('var',v))
                else:
                    # unexpected char in matrix row, maybe space
                    self.get()
            # skip spaces between elements
            self.skip_ws()
        # rows is list of rows each is list of components (int or matrix or var tuples)
        # We must parse matrix row elements as expressions not only simple ints
        # But given the problem statement, elements in rows are exprs and may be matrices
        # We'll return rows as list of list of exprs (tree format)
        return rows

def eval_expr(e,vars):
    if isinstance(e,int):
        return e%M
    if isinstance(e,list):
        # matrix (list of rows, each row list of exprs)
        # each expr in rows may be int or nested list
        # we flatten to 2D matrix of int
        val = flatten_expr_to_matrix(e)
        return val
    if isinstance(e,tuple):
        if e[0] == 'neg':
            f = eval_expr(e[1], vars)
            return mat_neg(f)
        if e[0] == 'add':
            A = eval_expr(e[1], vars)
            B = eval_expr(e[2], vars)
            if is_scalar(A) and is_scalar(B):
                return (to_scalar(A)+to_scalar(B))%M
            if is_scalar(A) and not is_scalar(B):
                A = scalar_to_mat(to_scalar(A), len(B), len(B[0]))
            if not is_scalar(A) and is_scalar(B):
                B = scalar_to_mat(to_scalar(B), len(A), len(A[0]))
            return mat_add(A,B)
        if e[0] == 'sub':
            A = eval_expr(e[1], vars)
            B = eval_expr(e[2], vars)
            if is_scalar(A) and is_scalar(B):
                return (to_scalar(A)-to_scalar(B))%M
            if is_scalar(A) and not is_scalar(B):
                A = scalar_to_mat(to_scalar(A), len(B), len(B[0]))
            if not is_scalar(A) and is_scalar(B):
                B = scalar_to_mat(to_scalar(B), len(A), len(A[0]))
            return mat_sub(A,B)
        if e[0] == 'mul':
            A = eval_expr(e[1], vars)
            B = eval_expr(e[2], vars)
            return mat_mul(A,B)
        if e[0] == 'var':
            v = e[1]
            return vars[v]
        if e[0] == 'trans':
            A = eval_expr(e[1], vars)
            return mat_transpose(A)
        if e[0] == 'idx':
            A = eval_expr(e[1], vars)
            indices = e[2]
            rinds = indices[0]
            cinds = indices[1]
            # A is matrix or scalar
            if is_scalar(A):
                # scalar matrix 1x1
                scalarval = to_scalar(A)
                # indexing returns scalar matrix sized len(rinds)xlen(cinds) filled with scalarval
                m = len(rinds)
                n = len(cinds)
                return scalar_to_mat(scalarval,m,n)
            mA,nA = mat_size(A)
            # rinds,cinds are list of integers one-origin
            # values out of range not considered given problem statement
            # build submatrix sized len(rinds)*len(cinds)
            res = [[0]*len(cinds) for _ in range(len(rinds))]
            for i,r in enumerate(rinds):
                for j,c in enumerate(cinds):
                    res[i][j] = A[r-1][c-1]%M
            return res
    return e

def main():
    import sys
    inputlines = []
    for line in sys.stdin:
        inputlines.append(line.rstrip('\n'))
    idx=0
    while True:
        if idx>=len(inputlines):
            break
        nline = inputlines[idx].strip()
        idx+=1
        if nline=='0':
            break
        n = int(nline)
        vars = {}
        for _ in range(n):
            statement = ''
            while True:
                if idx>=len(inputlines):
                    break
                sline = inputlines[idx]
                idx+=1
                statement += sline
                if statement.endswith('.'):
                    break
            # parse statement like A=expr.
            statement=statement.rstrip('.')
            # parse var before =
            eqpos = statement.find('=')
            var = statement[:eqpos].strip()
            expr_text = statement[eqpos+1:].strip()
            p = Parser(expr_text, vars)
            expr = p.parse_expr()
            val = eval_expr(expr, vars)
            vars[var] = val
            # print val
            if isinstance(val,int):
                print(val%M)
            else:
                m,n = mat_size(val)
                for i in range(m):
                    print(' '.join(str(val[i][j]%M) for j in range(n)))
        print('-----')

main()