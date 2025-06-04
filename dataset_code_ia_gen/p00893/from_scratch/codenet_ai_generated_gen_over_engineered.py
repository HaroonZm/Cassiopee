import sys
import re
from collections import deque
from typing import List, Tuple, Union

M = 32768  # modulo

# Define Abstract Syntax Tree Nodes for better extensibility

class MatrixValue:
    def __init__(self, rows: List[List[int]]):
        # rows: list of list of int
        self.rows = rows
        self.m = len(rows)
        self.n = len(rows[0]) if self.m > 0 else 0

    @staticmethod
    def from_scalar(x: int) -> 'MatrixValue':
        return MatrixValue([[x % M]])

    def is_scalar(self) -> bool:
        return self.m == 1 and self.n == 1

    def get_scalar(self) -> int:
        if self.is_scalar():
            return self.rows[0][0]
        raise ValueError("Not a scalar")

    def __add__(self, other: 'MatrixValue') -> 'MatrixValue':
        if self.m != other.m or self.n != other.n:
            raise ValueError("Dimension mismatch addition")
        result_rows = []
        for i in range(self.m):
            row = [(self.rows[i][j] + other.rows[i][j]) % M for j in range(self.n)]
            result_rows.append(row)
        return MatrixValue(result_rows)

    def __sub__(self, other: 'MatrixValue') -> 'MatrixValue':
        if self.m != other.m or self.n != other.n:
            raise ValueError("Dimension mismatch subtraction")
        result_rows = []
        for i in range(self.m):
            row = [(self.rows[i][j] - other.rows[i][j]) % M for j in range(self.n)]
            result_rows.append(row)
        return MatrixValue(result_rows)

    def __mul__(self, other: 'MatrixValue') -> 'MatrixValue':
        # Scalar * Matrix or Matrix * Scalar or Matrix * Matrix
        if self.is_scalar():
            # self scalar
            x = self.get_scalar()
            result_rows = []
            for r in other.rows:
                row = [(x * v) % M for v in r]
                result_rows.append(row)
            return MatrixValue(result_rows)
        if other.is_scalar():
            y = other.get_scalar()
            result_rows = []
            for r in self.rows:
                row = [(v * y) % M for v in r]
                result_rows.append(row)
            return MatrixValue(result_rows)
        if self.n != other.m:
            raise ValueError("Dimension mismatch multiplication")
        result_rows = []
        for i in range(self.m):
            row = []
            for j in range(other.n):
                s = 0
                for k in range(self.n):
                    s += self.rows[i][k] * other.rows[k][j]
                row.append(s % M)
            result_rows.append(row)
        return MatrixValue(result_rows)

    def __neg__(self):
        result_rows = []
        for r in self.rows:
            row = [(-v) % M for v in r]
            result_rows.append(row)
        return MatrixValue(result_rows)

    def transpose(self) -> 'MatrixValue':
        if self.m == 0:
            return MatrixValue([])
        transposed_rows = []
        for j in range(self.n):
            row = [self.rows[i][j] for i in range(self.m)]
            transposed_rows.append(row)
        return MatrixValue(transposed_rows)

    def submatrix(self, iidx: 'MatrixValue', jidx: 'MatrixValue') -> 'MatrixValue':
        # iidx, jidx are 1 x k and 1 x l matrices, k,l = number of rows/columns desired
        ki = iidx.n  # iidx is 1 x k
        lj = jidx.n  # jidx is 1 x l
        # checking size:
        if iidx.m != 1 or jidx.m != 1:
            raise ValueError("Index matrices must be 1-row matrices")
        # 1-based indices for extraction:
        result_rows = []
        for a in range(ki):
            r = []
            i_ = iidx.rows[0][a] - 1
            if i_ < 0 or i_ >= self.m:
                raise IndexError("Index i out of range")
            for b in range(lj):
                j_ = jidx.rows[0][b] - 1
                if j_ < 0 or j_ >= self.n:
                    raise IndexError("Index j out of range")
                r.append(self.rows[i_][j_])
            result_rows.append(r)
        return MatrixValue(result_rows)

    def __str__(self):
        # as per output spec: each row on its own line, space separated ints
        return '\n'.join(' '.join(str(x) for x in row) for row in self.rows)

# Tokenizer for the matrix expression language

TokType = str

class Token:
    def __init__(self, type_: TokType, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type},{self.value})"

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = text[0] if text else None

    def error(self):
        raise Exception('Invalid character in input')

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos >= len(self.text):
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char in ' \t\n\r':
            self.advance()

    def number(self):
        # non-negative integer less than M
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        val = int(result)
        if val >= M:
            raise Exception('Number exceeds modulo M')
        return Token('NUM', val)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char in ' \t\n\r':
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return self.number()
            if self.current_char == '+':
                self.advance()
                return Token('PLUS')
            if self.current_char == '-':
                self.advance()
                return Token('MINUS')
            if self.current_char == '*':
                self.advance()
                return Token('MUL')
            if self.current_char == '=':
                self.advance()
                return Token('EQUAL')
            if self.current_char == '[':
                # matrix start
                self.advance()
                return Token('LBRACKET')
            if self.current_char == ']':
                self.advance()
                return Token('RBRACKET')
            if self.current_char == '(':
                self.advance()
                return Token('LPAREN')
            if self.current_char == ')':
                self.advance()
                return Token('RPAREN')
            if self.current_char == ';':
                self.advance()
                return Token('SEMI')
            if self.current_char == ',':
                self.advance()
                return Token('COMMA')
            if self.current_char == '.':
                self.advance()
                return Token('DOT')
            if self.current_char == "'":
                self.advance()
                return Token('QUOTE')
            if self.current_char == '_':
                # not used but reserved if needed later
                self.advance()
                return Token('UNDERSCORE')
            if 'A' <= self.current_char <= 'Z':
                # variable
                v = self.current_char
                self.advance()
                return Token('VAR', v)
            # Unknown char
            self.error()
        return Token('EOF')

# Parsing with recursive descent + operator precedence for left associative +,-,*

class AST:
    pass

class BinOp(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.token = op
        self.op = op.type
        self.right = right

class UnaryOp(AST):
    def __init__(self, op: Token, expr: AST):
        self.token = op
        self.op = op.type
        self.expr = expr

class Var(AST):
    def __init__(self, name: str):
        self.name = name

class Num(AST):
    def __init__(self, value: int):
        self.value = value

class Matrix(AST):
    def __init__(self, rows: List[List[AST]]):
        # rows: list of list of AST expr
        # rows and cols must fit with nested rules, but this is checked later when evaluating
        self.rows = rows

class Indices(AST):
    def __init__(self, primary: AST, iindex: AST, jindex: AST):
        self.primary = primary
        self.iindex = iindex
        self.jindex = jindex

class Transpose(AST):
    def __init__(self, primary: AST, count: int):
        self.primary = primary
        self.count = count  # number of continuous quotes ' to apply

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, expected=''):
        raise Exception(f'Syntax error: expected {expected} found {self.current_token.type} {self.current_token.value}')

    def eat(self, token_type: TokType):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(token_type)

    # program := assignment+
    # assignment := var '=' expr '.' NL
    # expr := term (( '+' | '-' ) term )*
    # term := factor ( '*' factor )*
    # factor := '-' factor | primary
    # primary := var | num | matrix | '(' expr ')' (indices | transpose)?
    # indices := '(' expr ',' expr ')'
    # transpose := one or more ' after primary

    def parse_program(self) -> List[Tuple[str, AST]]:
        assignments = []
        # no explicit delimiter other than line count read outside
        # here we parse one assignment and return list
        # since input lines are joined, parsing multiple assignments until EOF or completed lines outside
        # In this implementation, one parse_program call is done per assignment line outside
        assignment = self.parse_assignment()
        assignments.append(assignment)
        return assignments

    def parse_assignment(self) -> Tuple[str, AST]:
        # var '=' expr '.'
        if self.current_token.type != 'VAR':
            self.error('VAR')
        var_name = self.current_token.value
        self.eat('VAR')
        self.eat('EQUAL')
        expr_node = self.expr()
        self.eat('DOT')
        # no explicit newline token, parsing line by line outside
        return (var_name, expr_node)

    def expr(self) -> AST:
        node = self.term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            else:
                self.eat('MINUS')
            right = self.term()
            node = BinOp(left=node, op=token, right=right)
        return node

    def term(self) -> AST:
        node = self.factor()
        while self.current_token.type == 'MUL':
            token = self.current_token
            self.eat('MUL')
            right = self.factor()
            node = BinOp(left=node, op=token, right=right)
        return node

    def factor(self) -> AST:
        token = self.current_token
        if token.type == 'MINUS':
            self.eat('MINUS')
            node = UnaryOp(token, self.factor())
            return node
        return self.primary()

    def primary(self) -> AST:
        token = self.current_token
        if token.type == 'VAR':
            node = Var(token.value)
            self.eat('VAR')
            node = self.parse_postfix(node)
            return node
        elif token.type == 'NUM':
            node = Num(token.value)
            self.eat('NUM')
            node = self.parse_postfix(node)
            return node
        elif token.type == 'LBRACKET':
            node = self.matrix()
            node = self.parse_postfix(node)
            return node
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            node = self.parse_postfix(node)
            return node
        else:
            self.error('VAR or NUM or LBRACKET or LPAREN')

    def parse_postfix(self, node: AST) -> AST:
        # parse indexed-primary or transposed-primary
        # indexed-primary := primary ( '(' expr ',' expr ')' )
        # transposed-primary := primary (')+ (one or more quotes)
        # both can be combined and repeated as in sample (#87).
        # Also chained multiple quotes is supported.
        while True:
            token = self.current_token
            if token.type == 'LPAREN':
                # indexed-primary
                self.eat('LPAREN')
                iindex = self.expr()
                self.eat('COMMA')
                jindex = self.expr()
                self.eat('RPAREN')
                node = Indices(node, iindex, jindex)
                continue
            if token.type == 'QUOTE':
                qcount = 0
                while self.current_token.type == 'QUOTE':
                    self.eat('QUOTE')
                    qcount += 1
                node = Transpose(node, qcount)
                continue
            break
        return node

    def matrix(self) -> AST:
        # matrix := '[' row_seq ']'
        self.eat('LBRACKET')
        rows = self.row_seq()
        self.eat('RBRACKET')
        return Matrix(rows)

    def row_seq(self) -> List[List[AST]]:
        # row_seq := row (';' row)*
        rows = [self.row()]
        while self.current_token.type == 'SEMI':
            self.eat('SEMI')
            rows.append(self.row())
        return rows

    def row(self) -> List[AST]:
        # row := expr (space expr)*
        # Spaces matters to separate adjacent expr in row
        # Our lexer skips whitespace, so this should be taken care in parser by consuming next expr tokens until meeting SEMI or RBRACKET
        # But as spaces are consumed by lexer outside of special tokens,
        # we try consume expr until next token is SEMI, RBRACKET or ')', or token that can not start an expr
        elements = []
        # must have at least one expr in row
        elements.append(self.expr())
        while True:
            # peek the next raw char is impossible, we rely on current_token and heuristics
            # if next token appears to start expr => keep reading
            if self.current_token.type in ('NUM', 'VAR', 'LBRACKET', 'LPAREN', 'MINUS'):
                # starting expr token
                elements.append(self.expr())
            else:
                # if next token is SEMI or RBRACKET or EOF or COMMA or RPAREN etc, end row
                break
        return elements

# Evaluation with environment for variables

class Environment:
    def __init__(self):
        self.vars = {}

    def set_var(self, varname: str, value: MatrixValue):
        self.vars[varname] = value

    def get_var(self, varname: str) -> MatrixValue:
        if varname not in self.vars:
            raise Exception(f'Variable {varname} undefined')
        return self.vars[varname]

# Evaluator defined in separate class for extensibility

class Evaluator:
    def __init__(self, env: Environment):
        self.env = env

    def eval(self, node: AST) -> MatrixValue:
        if isinstance(node, Num):
            return MatrixValue.from_scalar(node.value)
        elif isinstance(node, Var):
            return self.env.get_var(node.name)
        elif isinstance(node, BinOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == 'PLUS':
                return left + right
            elif node.op == 'MINUS':
                return left - right
            elif node.op == 'MUL':
                return left * right
            else:
                raise Exception(f'Unsupported BinOp {node.op}')
        elif isinstance(node, UnaryOp):
            exprv = self.eval(node.expr)
            if node.op == 'MINUS':
                return -exprv
            else:
                raise Exception(f'Unsupported UnaryOp {node.op}')
        elif isinstance(node, Matrix):
            return self.eval_matrix(node)
        elif isinstance(node, Indices):
            p_val = self.eval(node.primary)
            iidx_val = self.eval(node.iindex)
            jidx_val = self.eval(node.jindex)
            return p_val.submatrix(iidx_val, jidx_val)
        elif isinstance(node, Transpose):
            prim_val = self.eval(node.primary)
            # apply transpose count-times
            count = node.count % 2
            if count == 0:
                return prim_val
            else:
                return prim_val.transpose()
        else:
            raise Exception('Unknown AST node')

    def eval_matrix(self, node: Matrix) -> MatrixValue:
        # node.rows is List[List[AST]]
        # This may be nested matrixes by recursive evaluation
        # Each element in row is an expr -> evaluated to MatrixValue
        # Gather all rows
        # Check dimension consistency:
        # (1) number of rows = len(node.rows)
        # (2) number of columns in each row == the sum of widths of each element in that row
        # Also each element is a matrix with size (mi, ni)
        # So total columns = sum of ni over elements in one row
        # Total rows = sum of mi over rows
        # Rows must be consistent in height:
        # - For row-seq, sum of mi for each row must be the same for all rows
        # Columns consistent:
        # - for each row, sum ni of elements in it are consistent in that row
        # Also nested matrices elements may be matrix themselves, so composition needs concatenation by rows and cols.
        
        # Evaluate each element expr in matrix
        evaluated_rows = []
        # We'll gather for each row a list of MatrixValue elements
        for row_exprs in node.rows:
            row_elems = [self.eval(expr) for expr in row_exprs]
            # Validate all have same number of rows, for elements aligned vertically
            heights = [e.m for e in row_elems]
            if len(set(heights)) != 1:
                raise Exception("Inconsistent number of rows in matrix row elements")
            evaluated_rows.append(row_elems)

        # Now the number of rows in whole matrix = sum over evaluated_rows of height = sum of mi over rows ?
        # Actually matrix rows are horizontal concaten