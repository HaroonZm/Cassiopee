import sys
import re
from collections import defaultdict

sys.setrecursionlimit(10**7)

# The problem:
# Given an encrypted equation string (length <=31), where some characters are replaced by letters,
# we want to count how many possible original equations conforming to the grammar exist whose
# encrypted form matches the input string.
# The encryption rule: all occurrences replaced from a same original char must map to the same letter,
# different original chars never replaced by the same letter.
# Some occurrences of a char may be replaced, others not.
# Letters in the encrypted string are encryption chars, digits/operators/parentheses/equal sign are literals.
#
# We seek to count the number of original equations(evaluated expressions) matching the encryption,
# such that both sides evaluate equal.


# Approach outline:
# 1. The input has letters + literals.
#    Letters represent unknown original chars.
#    Different original chars replaced by distinct letters.
#    Non-letter characters are literals (0,1,+,-,*,(,),=).
#    The original equation contains exactly one '='.
#
# 2. We need to test assignments of original chars to letters,
#    consistent with letter substitutions, that can produce the given encrypted input.
#
# 3. To do that, we try all possible mappings from each letter ->
#    an original character from the set of possible chars {0,1,+,-,*,(,),=}.
#    But must be consistent between occurrences of the letter.
#    And different letters cannot map to the same original char.
#
# 4. For each complete mapping (letter->char), we substitute in the encrypted string,
#    obtaining a candidate original equation.
#    This equation must:
#       - have EXACTLY one '='
#       - conform to the grammar (parseable)
#       - evaluating left and right expressions must be equal.
#
# 5. Count how many mappings produce such valid original equations.
#
# Optimization:
# - The number of letters is at most the length of input (<=31), but often fewer.
# - The original chars can only be from the set:
#   '0','1','+','-','*','(',')','='
# - Number of distinct original chars: 9
# - So we assign letters distinct chars from these 9 candidates.
# - This is a permutation problem with pruning.
#
# Parsing and evaluating:
# - We'll do a recursive descent parser according to grammar.
# - Grammar expressions include negation prefix, *, +, -, parenthesis,
#   numbers are binary numbers starting with 0 or 1 (leading zeros only allowed if number is 0).
#
# Return the total count of valid original equations matching encrypted input.

# Original chars set (candidates for letter mapping)
ORIG_CHARS = ['0','1','+','-','*','(',')','=']

# Parse and evaluate structure
class ParseError(Exception):
    pass

class Parser:
    # We'll parse the string expr_str, starting at idx 0
    # and produce an AST and compute value.
    # Grammar:
    # Q ::= E=E
    # E ::= T | E+T | E-T
    # T ::= F | T*F
    # F ::= N | -F | (E)
    # N ::= 0 | 1B
    # B ::= empty | 0B | 1B
    #
    # We will parse methods parseQ, parseE, parseT, parseF, parseN
    #
    # We also track position and do left-associative parsing for +,-,* as described.
    #
    # Evaluate returns integer value of expression (in decimal)
        
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.pos = 0

    # utility
    def peek(self):
        return self.s[self.pos] if self.pos<self.n else None
    def consume(self):
        ch = self.peek()
        if ch is not None:
            self.pos += 1
        return ch
    def expect(self, ch):
        if self.peek() != ch:
            raise ParseError("Expected '{}' at pos {}".format(ch,self.pos))
        self.pos += 1
    def is_digit(self,ch):
        return ch=='0' or ch=='1'
    def parseQ(self):
        # Q ::= E=E
        val_left = self.parseE()
        if self.peek()!='=':
            raise ParseError("Expected '=' at pos {}".format(self.pos))
        self.consume() # consume '='
        val_right = self.parseE()
        if self.pos!=self.n:
            raise ParseError("Extra input at end")
        return (val_left,val_right)
    
    def parseE(self):
        # E ::= T | E+T | E-T (left associative)
        val = self.parseT()
        while True:
            ch = self.peek()
            if ch=='+':
                self.consume()
                right = self.parseT()
                val = val + right
            elif ch=='-':
                self.consume()
                right = self.parseT()
                val = val - right
            else:
                break
        return val

    def parseT(self):
        # T ::= F | T*F (left associative)
        val = self.parseF()
        while True:
            ch = self.peek()
            if ch=='*':
                self.consume()
                right = self.parseF()
                val = val * right
            else:
                break
        return val

    def parseF(self):
        # F ::= N | -F | (E)
        ch = self.peek()
        if ch=='-':
            self.consume()
            val = self.parseF()
            return -val
        elif ch=='(':
            self.consume()
            val = self.parseE()
            if self.peek()!=')':
                raise ParseError("Expected ')' at pos {}".format(self.pos))
            self.consume()
            return val
        else:
            val = self.parseN()
            return val

    def parseN(self):
        # N ::= 0 | 1B
        # B ::= empty | 0B | 1B
        ch = self.peek()
        if ch=='0':
            self.consume()
            return 0
        elif ch=='1':
            self.consume()
            val = 1
            # parse B
            while True:
                ch2 = self.peek()
                if ch2=='0':
                    self.consume()
                    val = val*2+0
                elif ch2=='1':
                    self.consume()
                    val = val*2+1
                else:
                    break
            return val
        else:
            raise ParseError("Expected number at pos {}".format(self.pos))


def main():
    expr = sys.stdin.readline().rstrip('\n')
    # Letter set in encrypted input
    letters = set(ch for ch in expr if ch.isalpha())

    # If no '=' in encrypted input literals, we can try letters mapped to '='
    # We know original has exactly one '='

    # prepare a mapping from letters -> original char
    # they must be distinct chars chosen from ORIG_CHARS
    # also literals in input must match original char at that position

    # For each letter, candidate chars = ORIG_CHARS
    # But we can prune some:
    # If same letter occurs multiple times, must be consistent mapping
    # literals in the input should match the original char at positions not letters

    # For that we first collect occurrences of each letter positions
    letter_positions = defaultdict(list)
    for i,ch in enumerate(expr):
        if ch.isalpha():
            letter_positions[ch].append(i)

    # For each letter, possible chars = ORIG_CHARS
    # But if at one occurrence the letter is 'A' and at position i, literal at expr[i] is letter,
    # we don't know original char. We try all candidates.

    # But we can prune candidates when a letter and a literal appear at same pos, letters are distinct from literals.

    # So we try all assignments letter->original char in ORIG_CHARS,
    # with letters mapping distinct original chars,
    # apply substitution to encrypted input,
    # check if results have exactly one '=' literal,
    # parse and eval,
    # count correct.

    letters_list = list(letters)
    L = len(letters_list)

    # Precompute literals positions to check no conflict
    # For literal positions: if ch not letter, must match itself in final mapping
    # After substitution of letters, combined string s' is original string candidate.

    # We'll implement DFS to assign letters distinct original chars.

    # We store:
    # assigned = dict letter->orig_char
    # used_chars = set of orig_char already assigned

    res = 0

    def check_and_count():
        # produce candidate original string by replacing letters by assigned chars
        s2 = list(expr)
        for ltr,ch2 in assigned.items():
            for pos in letter_positions[ltr]:
                s2[pos] = ch2
        s2 = ''.join(s2)

        # Check equal sign count must be exactly 1
        if s2.count('=')!=1:
            return 0

        # Check all chars in s2 in ORIG_CHARS or literals '0','1','+','-','*','(',')','='
        # Here allowed chars:
        # The original chars are ORIG_CHARS
        # Note the input literals must be from valid chars, otherwise no parse.
        # So if s2 contains any char not in ORIG_CHARS, reject
        for c in s2:
            if c not in ORIG_CHARS:
                return 0

        # Parse and evaluate:
        try:
            parser = Parser(s2)
            val_left, val_right = parser.parseQ()
            if val_left==val_right:
                return 1
            else:
                return 0
        except ParseError:
            return 0

    def dfs(i, assigned, used_chars):
        nonlocal res
        if i==L:
            res += check_and_count()
            return
        ltr = letters_list[i]
        for c in ORIG_CHARS:
            if c in used_chars:
                continue
            # assign
            assigned[ltr] = c
            used_chars.add(c)
            dfs(i+1, assigned, used_chars)
            used_chars.remove(c)
            del assigned[ltr]

    if L==0:
        # no letters, just try parsing literal expression as is
        # Check '=' count
        if expr.count('=')==1:
            valid = 0
            for c in expr:
                if c not in ORIG_CHARS:
                    print(0)
                    return
            try:
                parser = Parser(expr)
                val_left, val_right = parser.parseQ()
                if val_left==val_right:
                    valid = 1
            except ParseError:
                valid = 0
            print(valid)
        else:
            print(0)
    else:
        dfs(0, {}, set())
        print(res)

if __name__=="__main__":
    main()