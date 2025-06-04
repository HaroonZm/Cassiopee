from typing import List, Optional, Union, Tuple
import sys

class Token:
    def __init__(self, kind: str, value: Optional[str] = None):
        self.kind = kind
        self.value = value
    def __repr__(self):
        return f"Token({self.kind},{self.value})"

class LexerError(Exception):
    pass

class Lexer:
    usable_chars = set("LR(),0123456789?")
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    def peek(self)->Optional[str]:
        peek_pos = self.pos + 1
        if peek_pos >= len(self.text):
            return None
        return self.text[peek_pos]
    def generate_tokens(self) -> List[Token]:
        tokens = []
        while self.current_char is not None:
            if self.current_char not in self.usable_chars:
                raise LexerError(f"Invalid character {self.current_char}")
            if self.current_char in 'LR':
                # single letter token
                tokens.append(Token('FUNC', self.current_char))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token('LPAREN'))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token('RPAREN'))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token('COMMA'))
                self.advance()
            elif self.current_char.isdigit():
                # number token possibly with '?'
                num_str = self.consume_number()
                tokens.append(Token('NUMBER', num_str))
            elif self.current_char == '?':
                # could be multi ? in a number or ?? separated by commas and parens, treat as separate tokens
                # we consume as many continuous '?' as possible for convenience as a token
                qstr = self.consume_question_marks()
                tokens.append(Token('NUMBER', qstr))
            else:
                raise LexerError(f"Unknown char {self.current_char}")
        return tokens
    def consume_question_marks(self)->str:
        result = ''
        while self.current_char == '?':
            result += self.current_char
            self.advance()
        return result
    def consume_number(self)->str:
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '?'):
            result += self.current_char
            self.advance()
        return result

class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, val_possibilities: List[str]):
        # val_possibilities is a list of all possible strings representing numbers without leading zero issues
        # For example ["0"] or ["123","999"]
        self.val_possibilities = val_possibilities
    def __repr__(self):
        return f"Number({self.val_possibilities})"

class Function(ASTNode):
    def __init__(self, func_name: str, left: ASTNode, right: ASTNode):
        self.func_name = func_name
        self.left = left
        self.right = right
    def __repr__(self):
        return f"Function({self.func_name},{self.left},{self.right})"

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    def peek(self) -> Optional[Token]:
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]
    def consume(self, expected_kind: Optional[str] = None) -> Token:
        if self.pos >= len(self.tokens):
            raise ParserError(f"Unexpected end of input expecting {expected_kind}")
        current = self.tokens[self.pos]
        if expected_kind is not None and current.kind != expected_kind:
            raise ParserError(f"Expected token {expected_kind} but got {current.kind}")
        self.pos += 1
        return current
    def parse(self) -> ASTNode:
        if self.pos >= len(self.tokens):
            raise ParserError("Empty input")
        return self.expr()
    def expr(self) -> ASTNode:
        # expression is either number or function call
        # function call: FUNC LPAREN expr COMMA expr RPAREN
        tok = self.peek()
        if tok.kind == 'FUNC':
            func_name = tok.value
            self.consume('FUNC')
            self.consume('LPAREN')
            left = self.expr()
            self.consume('COMMA')
            right = self.expr()
            self.consume('RPAREN')
            return Function(func_name, left, right)
        elif tok.kind == 'NUMBER':
            n_tok = self.consume('NUMBER')
            # n_tok.value may contain '?' characters as well as digits => impossible after tokenization but possible because numbers can contain '?'
            # We keep string as is and later will handle ?
            return Number([n_tok.value])
        else:
            raise ParserError(f"Unexpected token {tok.kind}")

class EvaluatorError(Exception):
    pass

class NumberExpander:
    # Given a string pattern of digits and '?' produce all valid numbers (without leading zeros except if single '0') possible and sorted descending
    # To be efficient we only keep max number (string) possible from a pattern string because only max is needed for max score
    # But since ? can appear multiple times in large numbers, we do digit-wise maximal substitution.
    @staticmethod
    def maximize_number_pattern(pattern: str) -> Optional[str]:
        # pattern contains digits or '?'
        # no leading zeros except 0 itself
        # return max number string or None if invalid
        if not pattern:
            return None
        res = []
        for i,ch in enumerate(pattern):
            if ch == '?':
                # choose max digit to maximize number
                # leading zero not allowed except if the pattern length=1 (one char '?')
                if i == 0 and len(pattern) > 1:
                    # cannot be zero: take 9
                    res.append('9')
                else:
                    res.append('9')
            elif ch.isdigit():
                res.append(ch)
            else:
                return None
        # check leading zeros invalidity
        if len(res) > 1 and res[0] == '0':
            return None
        return ''.join(res)

class ExpressionEvaluator:
    # Evaluate AST subtree for maximum possible score with '?' replaced by digits only in numbers, producing max integer value
    # We recurse and compute max based on function definitions:
    # L(x,y) = x
    # R(x,y) = y
    # Also we check validity.
    # An optimization is to propagate maximum possible values up.
    @staticmethod
    def evaluate_max(node: ASTNode) -> Optional[int]:
        if isinstance(node, Number):
            # node.val_possibilities is list of patterns (strings with digits and maybe '?')
            # Since parser guarantees one pattern string only, but with '?'.
            # We produce max numeric value after replacing '?' in pattern with digits
            pattern = node.val_possibilities[0]
            max_num_str = NumberExpander.maximize_number_pattern(pattern)
            if max_num_str is None:
                return None
            # valid number, convert to int
            return int(max_num_str)
        elif isinstance(node, Function):
            # maximize both sides
            left_val = ExpressionEvaluator.evaluate_max(node.left)
            right_val = ExpressionEvaluator.evaluate_max(node.right)
            if left_val is None or right_val is None:
                return None
            if node.func_name == 'L':
                return left_val
            elif node.func_name == 'R':
                return right_val
            else:
                # invalid function
                return None
        else:
            return None

class Completor:
    # Replace all '?' by valid characters from usable chars (digits or L,R,(,),,) to produce valid expression maximizing score
    # But the problem is that the input string may have ? anywhere, including in numbers or function names etc.
    # But function names are only single L or R: so no ambiguity in 'LR' token
    # We don't need to generate all strings, only those that are valid and produce maximum score.
    # Strategy:
    # Because maximum score is from maximum integer produced, which comes from numbers (including nested functions), we want to:
    # - replace ? in function letters by either L or R to get valid token
    # - replace ? in numbers only by digits that produce largest number (primarily '9' except leading digit)
    # - replace ? in symbols '(' , ')' , ',' to that char to satisfy grammar
    # But ? in those symbols can only be replaced with those symbols to be valid.
    # We do a backtracking replacement of '?' with all possible usable characters in a strongly guided way.
    # Because input length max 50, and number of '?' max 50, we need pruning and memoization.
    # This is complex, so we use a class with memoization by position and partial token stream after replacement.
    #
    # But we will construct a replacement function based on the original string input,
    # test substitutions that make valid tokens, parse and evaluate maximum score.
    #
    # As this problem is quite complex, we will implement a backtracking with pruning approach generating candidates only for '?'
    # We rely on abstract tokens and parser to validate.
    #
    # To handle, we define what chars '?' can be replaced at each place:
    # - If '?' can be first char of a token that must be FUNC => only L or R
    # - If '?' expected to be digit of number => digit 0-9 but no leading zero if number length>1
    # - If '?' expected to be symbol => one corresponding symbol only
    # But since we don't know token boundaries before tokenizing, we try to replace '?' in all possible ways and attempt tokenization.
    #
    # This is expensive, so we proceed with a solution: we replace '?' in the original string with each usable char one by one in an incremental way,
    # and after all '?', try parse and compute max.
    #
    # To reduce complexity, we generate candidate replacements symbol by symbol, pruning invalid tokens early if any.
    #
    # After investigation, it's more feasible to generate all possible replacements with pruning by tokenization step:
    # But since length is small and digit '?' can produce many possibilities, we optimize by only replacing digits '?' with '9' for maximal number 
    # and for others replace '?' with their maximal possible value. So we do a greedy replacement:
    # - If '?' is in digit position in number, replace by '9' (or '1' if leading zero forbidden)
    # - If '?' is in function name or symbol position, replace by corresponding maximal char possible :
    #   For functions L or R replace by 'R' to maximize chance (R or L both valid but no score difference)
    #   For symbols '(' or ')' or ',' replace by themselves since no variant.
    # So actually one greedy replacement for all '?' and then parse and evaluate max is sufficient and guaranteed to find max score or detect invalid.
    #
    # Special care: leading zero forbidden in numbers except for zero itself

    function_chars = {'L','R'}
    symbol_chars = {'(',')',','}
    digit_chars = set('0123456789')
    maximal_digit = '9'

    @staticmethod
    def greedy_replace(wild_str: str) -> Optional[str]:
        # Replace all '?' with maximal chars possible to make string valid and maximal value
        # We'll scan char by char and try to guess replacement:
        # We do a complex state machine to infer context: are we in number or function or symbol?
        # But in the problem all characters are in fixed set, and functions are only L or R.
        # We'll tokenize partially and fill '?' accordingly:
        res = list(wild_str)
        length = len(res)
        # We approach by a manual FSM parsing on the fly
        # States: expecting token: FUNC or NUMBER or symbol
        # Actually impossible to guess exactly tokenization for '?', but since L and R only single char tokens, and digits and ? can be in number.
        # We implement a minimal lexer on greedy way to fill '?':
        pos = 0
        while pos < length:
            c = res[pos]
            if c == '?':
                # Decide what can be here:
                # If at start of token and next char is digit or '?', it's number start
                # If at start of token and next char is L or R or '?', it's function token
                # If character is symbol or '?', must fill with symbol or digit accordingly.
                # We try to disambiguate by lookahead
                # A simple heuristic:
                # If previous char is None or one of '(',',', then start new token
                prev_char = res[pos-1] if pos > 0 else None
                # next char:
                next_char = res[pos+1] if pos+1 < length else None
                # Check if we are starting a token
                if prev_char in (None,'(',','):
                    # token start, check next char:
                    if next_char in ('L','R','?'):
                        # token is FUNC, replace '?' by 'R' (max between L and R)
                        res[pos] = 'R'
                    elif next_char in ('(',')',','):
                        # Could be symbol alone?
                        # single symbol ?
                        # But if token start, single char token ?
                        # But '?' here needs to be symbol - only if it's '?' itself
                        # we assign '(' or ',' or ')' for '?' at this position
                        # By default, assign maximal symbol by their order '(' < ',' < ')':
                        # We'll pick ')' as max char symbol? No, symbols do not affect score but we must produce valid expression
                        # We choose '(' as the max to increase chances of matching functions
                        # But safer is to pick the char that appears in input at this position or the one expected by grammar
                        # We'll just choose '(' as '(' is needed for functions
                        res[pos] = '('
                    elif next_char in '0123456789?':
                        # token is number start - leading digit can't be zero if number length>1
                        # By assumption, number length unknown here, choose '9' as max digit at leading pos but cannot be zero
                        res[pos] = '9'
                    else:
                        # unknown next char, default digit max
                        res[pos] = '9'
                else:
                    # not start of token, in token middle
                    if prev_char.isdigit() or prev_char == '?':
                        # in number, select max digit 9
                        res[pos] = '9'
                    elif prev_char in ('L','R'):
                        # after function char no number expected, must be symbol or comma or paren, so ?
                        # assign symbol '(' as likely opening parenthesis
                        res[pos] = '('
                    elif prev_char in ('(',','):
                        # token start again
                        # treat as above
                        if next_char in ('L','R','?'):
                            res[pos] = 'R'
                        elif next_char in '0123456789?':
                            res[pos] = '9'
                        else:
                            res[pos] = '('
                    else:
                        # default fallback digit
                        res[pos] = '9'
            pos += 1
        replaced_str = ''.join(res)
        return replaced_str

class Solution:
    def __init__(self, expression: str):
        self.original_expr = expression

    def solve(self) -> str:
        # Use greedy completion, then tokenize parse and evaluate max
        replaced = Completor.greedy_replace(self.original_expr)
        if replaced is None:
            return "invalid"
        # tokenize
        try:
            lexer = Lexer(replaced)
            tokens = lexer.generate_tokens()
        except LexerError:
            return "invalid"
        # parse
        try:
            parser = Parser(tokens)
            ast = parser.parse()
            # check we consumed all tokens
            if parser.pos != len(tokens):
                return "invalid"
        except ParserError:
            return "invalid"
        # evaluate max score
        val = ExpressionEvaluator.evaluate_max(ast)
        if val is None:
            return "invalid"
        return str(val)

def main():
    expr = sys.stdin.readline().rstrip('\n')
    sol = Solution(expr)
    print(sol.solve())

if __name__ == '__main__':
    main()