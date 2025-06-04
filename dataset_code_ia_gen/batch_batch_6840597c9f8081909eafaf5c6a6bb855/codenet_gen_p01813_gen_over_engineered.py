class Expression:
    def evaluate(self) -> int:
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

class Digit(Expression):
    def __init__(self, value: int):
        self.value = value

    def evaluate(self) -> int:
        return self.value

    def __str__(self):
        return str(self.value)

class BinaryOp(Expression):
    def __init__(self, left: Expression, op: str, right: Expression):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self) -> int:
        if self.op == '+':
            return self.left.evaluate() + self.right.evaluate()
        if self.op == '-':
            return self.left.evaluate() - self.right.evaluate()
        raise ValueError("Unsupported op")

    def __str__(self):
        return f"{str(self.left)}{self.op}{str(self.right)}"

class Bracket(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def evaluate(self) -> int:
        return self.expr.evaluate()

    def __str__(self):
        return f"({str(self.expr)})"

class Token:
    def __init__(self, type_: str, value: str):
        self.type = type_
        self.value = value

    def __str__(self):
        return f"Token({self.type},{self.value})"

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.len = len(text)

    def next_token(self):
        while self.pos < self.len and self.text[self.pos] == ' ':
            self.pos += 1
        if self.pos >= self.len:
            return Token("EOF","")
        c = self.text[self.pos]
        if c.isdigit():
            self.pos += 1
            return Token("DIGIT", c)
        if c in "+-()":
            self.pos += 1
            return Token(c,c)
        raise ValueError("Invalid char " + c)

    def tokenize(self):
        tokens = []
        while True:
            token = self.next_token()
            tokens.append(token)
            if token.type == "EOF":
                break
        return tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos]

    def eat(self, ttype):
        if self.current_token().type == ttype:
            self.pos += 1
        else:
            raise ValueError(f"Expected token {ttype} but got {self.current_token().type}")

    def parse(self) -> Expression:
        return self.expr()

    def expr(self) -> Expression:
        # <expr> ::= "(" <expr> ")"
        #          | <term> "+" <term>
        #          | <term> "-" <term>
        # <term> ::= <digit> | <expr>
        # We parse according to these rules, treating parentheses first.
        if self.current_token().type == '(':
            self.eat('(')
            inner = self.expr()
            self.eat(')')
            return Bracket(inner)
        # parse term
        left = self.term()
        # check if next is + or -
        if self.current_token().type in ['+', '-']:
            op = self.current_token().type
            self.eat(op)
            right = self.term()
            return BinaryOp(left, op, right)
        return left

    def term(self) -> Expression:
        if self.current_token().type == "DIGIT":
            val = int(self.current_token().value)
            self.eat("DIGIT")
            return Digit(val)
        if self.current_token().type == '(':
            return self.expr()
        raise ValueError(f"Unexpected token in term: {self.current_token().type}")

class MaxExpression:
    def __init__(self, text: str):
        self.text = text
        lexer = Lexer(text)
        self.tokens = lexer.tokenize()
        self.parser = Parser(self.tokens)
        self.ast = self.parser.parse()
        self.tokens_len = len(self.tokens)
        # We use a memoization over substrings for dp:
        # dp[l][r][state] = max value of a <expr> from tokens l to r directly, state indicates whether it's a complete expr.
        # Here state is boolean: True if exactly one <expr> found wrapped in the substring, else False
        # Actually we track two dp:
        # - max value formed by a valid expr fully covering tokens[l:r+1]
        # - max value formed by any possible insertion of parentheses in tokens[l:r+1], possibly multiple exprs combined by '+' and '-'
        # But given problem complexity and needs, we store:
        # dp[l][r] = max integer value of any expression that can be formed from tokens [l..r] by adding parentheses (including adding unnecessary pairs)
        # If no expression possible, dp[l][r] = None
        self.dp = [[None]*(self.tokens_len) for _ in range(self.tokens_len)]

    def is_digit_token(self, t: Token) -> bool:
        return t.type == "DIGIT"

    def is_op_token(self, t: Token) -> bool:
        return t.type in ['+', '-']

    def is_paren_token(self, t: Token) -> bool:
        return t.type in ['(',')']

    def solve(self) -> int:
        # We will build possible expressions from tokens[i:j+1].
        # We will consider that we can insert any number of '(' or ')' anywhere.
        # The problem reduces to checking partitions around '+' and '-' and putting parentheses to maximize the value.

        # Convert tokens to a simplified array ignoring EOF:
        tokens = [t for t in self.tokens if t.type != "EOF"]
        n = len(tokens)

        # Memo dp: key (l,r) -> max value or None if impossible
        from functools import lru_cache

        # Because parentheses can be added anywhere, the tokens array itself is always fully valid as a sequence
        # So we need to consider interpretations as expressions, by parenthesizing subexpressions properly.

        # Since only single digit numbers, operators + and -, parentheses allowed, the key is to find maximum value by adding parentheses
        # We note that the original tokens form an expression (given), but we can add any parentheses anywhere.

        # We'll do dp over intervals [l, r] where we try to parse the tokens into expression and compute max result.

        # Because token can be digit or operator or parens, but we can add any parentheses,
        # The parentheses in original can be ignored because we can add parentheses arbitrarily.

        # So define dp[l][r] = maximum value of expression that can be formed from tokens[l:r+1]

        # To do this dp, we must parse all possible splits:
        # If [l] is digit and l==r: then dp[l][r] = that digit value
        # Else look for operator positions m where tokens[m] is '+' or '-'
        # Then dp[l][r] = max over dp[l][m-1] op dp[m+1][r]

        # To apply parentheses anywhere, we simply consider all partitions.

        @lru_cache(None)
        def dp(l:int, r:int) -> int:
            if l > r:
                return None
            # Single token
            if l == r:
                if tokens[l].type == "DIGIT":
                    return int(tokens[l].value)
                else:
                    # Single token not digit no expr
                    return None
            # Try the whole interval with parentheses: because parentheses can be added anywhere,
            # we can ignore existing parentheses and just consider the token sequence with digits and operators.

            max_val = None
            # if tokens[l] == '(' and tokens[r] == ')', attempt to strip these parentheses if they match
            # but parentheses might be unbalanced if added wrongly - problem allows it if the final expression is syntactically correct (which means complete according to BNF)
            # So best is to ignore parentheses tokens because we can add any parentheses freely

            # But to be safe, strip valid outer parentheses:
            if tokens[l].type == '(' and tokens[r].type == ')':
                inner = dp(l+1, r-1)
                if inner is not None:
                    max_val = inner

            # Try all operators positions that separate expression:
            # operators are '+' or '-'
            for m in range(l+1, r):
                if tokens[m].type in ['+', '-']:
                    left = dp(l, m-1)
                    right = dp(m+1, r)
                    if left is not None and right is not None:
                        val = (left + right) if tokens[m].type == '+' else (left - right)
                        if max_val is None or val > max_val:
                            max_val = val
            return max_val

        ans = dp(0, n-1)
        if ans is None:
            return 0
        return ans

def main():
    import sys
    S = sys.stdin.readline().strip()
    solver = MaxExpression(S)
    print(solver.solve())

if __name__=="__main__":
    main()