import sys
import re
import math
from typing import List, Set, Union, Dict, Callable, Tuple, Optional

class Expression:
    def evaluate_all(self) -> Set[int]:
        """Evaluate all possible results of this expression with different parenthesizations."""
        raise NotImplementedError

class Number(Expression):
    def __init__(self, value: int):
        self.value = value
    
    def evaluate_all(self) -> Set[int]:
        return {self.value}

class BinaryOp(Expression):
    def __init__(self, left: Expression, right: Expression, op: str):
        self.left = left
        self.right = right
        self.op = op
        self._operation = self._get_operation(op)
    
    def _get_operation(self, op: str) -> Callable[[int,int], Optional[int]]:
        # Define operations according to Kitamasa-kun's rules
        def add(a: int, b: int) -> Optional[int]:
            return a + b
        def sub(a: int, b: int) -> Optional[int]:
            return a - b
        def mul(a: int, b: int) -> Optional[int]:
            return a * b
        def div(a: int, b: int) -> Optional[int]:
            # division by zero is invalid calculation path
            if b == 0:
                return None
            # Kitamasa-kun rounds result to the smaller abs integer, truncates fractional part
            res = a / b
            abs_a = abs(a)
            abs_b = abs(b)
            if abs_a < abs_b:
                # round to abs smaller = abs(a)
                target_abs = abs_a
            else:
                target_abs = abs_b
            # truncate fractional part towards zero (integer division trunc)
            if res >= 0:
                approx = int(math.floor(res))
            else:
                approx = int(math.ceil(res))
            # nearest integer to res with abs <= target_abs
            # fix if abs(approx) > target_abs
            if abs(approx) > target_abs:
                # choose sign of approx:
                approx = int(res//1)  # redundancy but keep
                # truncate abs to target_abs with sign of approx:
                approx = (target_abs if approx >= 0 else -target_abs)
            return approx
        return {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
        }[op]
    
    def evaluate_all(self) -> Set[int]:
        # Because multiple ways of parenthesizing children, we have to consider all their results combinatorially
        left_vals = self.left.evaluate_all()
        right_vals = self.right.evaluate_all()
        results = set()
        for lv in left_vals:
            for rv in right_vals:
                val = self._operation(lv, rv)
                if val is not None and abs(val) <= 10**9:
                    results.add(val)
        return results

class Parentheses(Expression):
    def __init__(self, inner: Expression):
        self.inner = inner
    
    def evaluate_all(self) -> Set[int]:
        # Parentheses enforce order, so just evaluate inner once
        return self.inner.evaluate_all()

class Parser:
    def __init__(self, s: str):
        self.s = s
        self.pos = 0
    
    def peek(self) -> Optional[str]:
        if self.pos < len(self.s):
            return self.s[self.pos]
        return None

    def consume(self, ch: Optional[str] = None) -> str:
        if self.pos >= len(self.s):
            raise ValueError("Unexpected end of input")
        c = self.s[self.pos]
        if ch is not None and c != ch:
            raise ValueError(f"Expected '{ch}', got '{c}'")
        self.pos += 1
        return c

    def parse_expression(self) -> Expression:
        # Parse expression with custom order,
        # but Kitamasa-kun does not fix precedence, all possible binary split orders must count,
        # so parsing into AST just by the syntax:
        # We'll parse fully into an AST with binary op nodes, ignoring precedence,
        # and then during evaluation we generate all ways of evaluation by recursive splitting.
        #
        # Because to compute all possible results with all possible orders,
        # we must parse fully respecting parentheses but treat flat expressions
        # as a list of tokens for re-parenthesizing.
        tokens = self.tokenize_expression()
        expr = self.build_expression_all_ways(tokens)
        return expr
    
    def tokenize_expression(self) -> List[Union[int, str]]:
        # Tokenize numbers, operators and parentheses
        tokens: List[Union[int,str]] = []
        while True:
            c = self.peek()
            if c is None:
                break
            if c.isspace():
                self.consume()
                continue
            if c.isdigit():
                # parse full number
                num_str = ''
                while self.peek() is not None and self.peek().isdigit():
                    num_str += self.consume()
                tokens.append(int(num_str))
            elif c in "+-*/()":
                tokens.append(self.consume())
            else:
                # Invalid character
                raise ValueError(f"Invalid character {c}")
        return tokens

    def build_expression_all_ways(self, tokens: List[Union[int,str]]) -> Expression:
        # Rebuild Expression tree from tokens taking parentheses into account
        # We parse a fully parenthesized structure and produce an Expression that allows multiple evaluation orders.
        # For Kitamasa-kun, all possible _parenthesizations_ correspond to different computation orders.
        # So we parse to AST with minimal structure: numbers and subexpressions with operators.
        # 'tokens' is list of numbers, operators, parentheses (remaining after tokenizing).

        # We'll implement a function to parse tokens into expression recursively.
        def parse_tokens(ts: List[Union[int,str]], start: int, end: int) -> Expression:
            # Remove enclosing parentheses if present
            while start < end and ts[start] == '(' and self.matching_paren(ts, start) == end - 1:
                start += 1
                end -= 1
            
            # If only one token and it's number, return Number
            if start == end - 1:
                if isinstance(ts[start], int):
                    return Number(ts[start])
                else:
                    raise ValueError("Expected number")
            # If the token range contains no parentheses on its edge, we try all binary splits
            # but for now, return a special Expression that supports generating all ways
            return ExpressionWithOps(ts[start:end])

        def expr_all_ways(ts: List[Union[int,str]], start: int, end: int) -> Expression:
            # Like parse_tokens but wrap as ExpressionWithOps to handle all possible parenthesis placements
            return parse_tokens(ts, start, end)

        # We define a helper to find matching paren index:
    def matching_paren(self, tokens: List[Union[int,str]], start_index: int) -> int:
        # Precondition tokens[start_index] == '('
        depth = 0
        for i in range(start_index, len(tokens)):
            if tokens[i] == '(':
                depth += 1
            elif tokens[i] == ')':
                depth -= 1
                if depth == 0:
                    return i
        raise ValueError("Unmatched '(' in expression")

    def parse_expression(self) -> Expression:
        # Instead of prior approach, implement a proper expression parser for given BNF,
        # but then represent the expression as a nested structure that supports all evaluation orders.
        # We'll use memoization on subexpressions by indices for generating all results.
        # To get tokens with positions, we tokenize first.
        self.pos = 0
        tokens = self.tokenize_expression()
        # parse tokens fully accepting parentheses and build a nested structure
        expr, next_pos = self.parse_expr_recursive(tokens, 0, len(tokens))
        if next_pos != len(tokens):
            raise ValueError("Extra tokens after valid expression")
        return expr

    def parse_expr_recursive(self, tokens: List[Union[int,str]], start: int, end: int) -> Tuple[Expression, int]:
        # parse expr ::= num | "(" expr ")" | expr op expr
        # But since implementation complexity, parse first primary (num or parenthesized expr)
        # then parse binary operations left to right with no fixed precedence (because all orders considered later)
        # For Kitamasa-kun, the evaluation order varies, so parser makes AST reflecting structure.
        # Here we parse with left-associative grouping by default (to produce an AST), but we reinterpret to evaluation all ways.

        def parse_primary(pos: int) -> Tuple[Expression, int]:
            if pos >= end:
                raise ValueError("Unexpected end")
            tok = tokens[pos]
            if isinstance(tok, int):
                return Number(tok), pos + 1
            elif tok == '(':
                # parse inside parens
                matching = self.matching_paren(tokens, pos)
                inner_expr, _ = self.parse_expr_recursive(tokens, pos + 1, matching)
                return inner_expr, matching + 1
            else:
                raise ValueError(f"Unexpected token {tok} where primary exp expected")

        left_expr, pos = parse_primary(start)
        # parse zero or more (op primary)
        exprs: List[Expression] = [left_expr]
        ops: List[str] = []
        while pos < end:
            tok = tokens[pos]
            if tok in ('+', '-', '*', '/'):
                ops.append(tok)
                right_expr, pos = parse_primary(pos + 1)
                exprs.append(right_expr)
            else:
                break
        # Now we have a sequence: exprs[0], ops[0], exprs[1], ops[1], exprs[2] ...
        # Build a ExpressionWithOps node that captures this flat expression to compute all eval orders later
        return ExpressionWithOps(exprs, ops), pos

class ExpressionWithOps(Expression):
    def __init__(self, exprs: Union[List[Expression], List[Union[int,str]]], ops: Optional[List[str]] = None):
        # exprs can be either:
        # - List[Expression] plus ops list
        # or
        # - List of tokens not yet parsed (used in earlier stage)
        if ops is None:
            # We have tokens, parse them fully into ExpressionWithOps by tokenizer?
            # But we do not use this way now, all tokens processed by Parser.parse_expr_recursive
            raise NotImplementedError
        self.exprs: List[Expression] = exprs
        self.ops: List[str] = ops

        self.memo: Dict[Tuple[int,int], Set[int]] = {}

    def evaluate_all(self) -> Set[int]:
        # evaluate all possible outcomes by all parenthesizing orders of exprs and ops
        # use DP memoization on (start, end) expression slice
        return self._eval_range(0, len(self.exprs) - 1)

    def _eval_range(self, i: int, j: int) -> Set[int]:
        if (i, j) in self.memo:
            return self.memo[(i,j)]
        if i == j:
            # single expression value
            res = self.exprs[i].evaluate_all()
            self.memo[(i,j)] = res
            return res
        
        results: Set[int] = set()
        # try all splits k where op[k] splits exprs[i..j]
        for k in range(i, j):
            op = self.ops[k]
            left_vals = self._eval_range(i, k)
            right_vals = self._eval_range(k + 1, j)
            for lv in left_vals:
                for rv in right_vals:
                    val = self._apply_op(lv, op, rv)
                    if val is not None and abs(val) <= 10**9:
                        results.add(val)
        self.memo[(i,j)] = results
        return results
    
    def _apply_op(self, a: int, op: str, b: int) -> Optional[int]:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return None
            res = a / b
            abs_a = abs(a)
            abs_b = abs(b)
            target_abs = abs_a if abs_a < abs_b else abs_b
            if res >= 0:
                approx = int(math.floor(res))
            else:
                approx = int(math.ceil(res))
            # ensure abs(approx) <= target_abs
            if abs(approx) > target_abs:
                approx = target_abs if approx >= 0 else -target_abs
            return approx
        else:
            raise ValueError(f"Unknown operator {op}")

def main():
    lines = sys.stdin.read().strip('\n').split('\n')
    for line in lines:
        if line.strip() == '#':
            break
        parser = Parser(line.strip())
        expr = parser.parse_expression()
        results = expr.evaluate_all()
        print(len(results))

if __name__ == '__main__':
    main()