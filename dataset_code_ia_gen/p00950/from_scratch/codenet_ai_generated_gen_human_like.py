from sys import setrecursionlimit
setrecursionlimit(10**7)

# Operators allowed
OPERATORS = {'+', '-', '*', '(', ')', '=', '0', '1'}

# Given input, encrypted equation string
s = input()

# Find all letters used in the equation
letters = set([c for c in s if c.isalpha()])

# The set of possible characters the letters can represent
possible_chars = list(OPERATORS)

# Map each letter to a character (0,1,+,-,*,(,),=)
# We will try all mappings consistent with the encryption constraints:
#   - One letter maps to exactly one character
#   - Different letters map to different characters
#   - Characters can appear multiple times both replaced by letters or left unreplaced

n = len(s)
letter_list = list(letters)
L = len(letter_list)

# Precompute positions of letters for substitution
letter_pos = {}
for i, c in enumerate(s):
    if c.isalpha():
        letter_pos.setdefault(c, []).append(i)

# We need to try all possible mappings letter->char with uniqueness constraint
# Because maximum length is 31, and possible chars are 9,
# and letters can be up to 52 (uppercase+lowercase), but problem limits input size to 31
# So maximum letters <=31.
# Trying all mappings would be huge, but only some letters appear,
# likely less than 10 letters.
# So brute force over mappings is possible with pruning.

# We will cache parsing results for each string to speed up checking validity.

# Functions for parsing according to grammar Q ::= E=E

# We'll write a parser for arithmetic expressions returning:
#   - set of possible values of expression (integers)
#   - only if valid parses exist, otherwise empty set
# We'll parse the string fully after replacing letters by their guessed chars.

# Evaluate expression in int, with:
# Numbers are binary (0 or 1B where B is binary number, starting with 1 if multi-digit)
# Negation unary operator
# Multiplication *, addition +, subtraction -, with specified precedence and left associativity

# To handle multiple parses (due to ambiguous parentheses?), we consider that the input is unambiguous
# by grammar, so parsing from left to right is unique. Parentheses may be redundant but don't create ambiguities.

# We'll implement a recursive descent parser with memoization.

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in '()+-*=':
            tokens.append(c)
            i += 1
        elif c == '0':
            tokens.append('0')
            i += 1
        elif c == '1':
            # parse binary number starting with 1
            j = i+1
            while j < len(expr) and expr[j] in '01':
                j += 1
            tokens.append(expr[i:j])
            i = j
        else:
            # invalid token
            return None
    return tokens

def parse_Q(tokens):
    # Q ::= E=E
    # returns (value, length) or None
    for i in range(len(tokens)):
        if tokens[i] == '=':
            left = parse_E(tokens[:i])
            right = parse_E(tokens[i+1:])
            if left is None or right is None:
                return None
            return (left, right)
    return None

def parse_E(tokens):
    # E ::= T | E+T | E-T
    # left associative, so parse left to right
    if not tokens:
        return None
    # Parse first T
    left = parse_T(tokens)
    if left is None:
        return None
    val, length = left
    pos = length
    while pos < len(tokens):
        op = tokens[pos]
        if op != '+' and op != '-':
            break
        right = parse_T(tokens[pos+1:])
        if right is None:
            return None
        rval, rlen = right
        pos += 1 + rlen
        # Apply operator
        if op == '+':
            val = val + rval
        else:
            val = val - rval
    if pos != len(tokens):
        return None
    return (val, pos)

def parse_T(tokens):
    # T ::= F | T*F
    # left associative, so parse left to right
    if not tokens:
        return None
    # Parse first F
    left = parse_F(tokens)
    if left is None:
        return None
    val, length = left
    pos = length
    while pos < len(tokens):
        op = tokens[pos]
        if op != '*':
            break
        right = parse_F(tokens[pos+1:])
        if right is None:
            return None
        rval, rlen = right
        val = val * rval
        pos += 1 + rlen
    if pos != len(tokens):
        return None
    return (val, pos)

def parse_F(tokens):
    # F ::= N | -F | (E)
    if not tokens:
        return None
    if tokens[0] == '-':
        f = parse_F(tokens[1:])
        if f is None:
            return None
        val, length = f
        return (-val, length + 1)
    if tokens[0] == '(':
        # find corresponding ')'
        depth = 0
        for i in range(len(tokens)):
            if tokens[i] == '(':
                depth += 1
            elif tokens[i] == ')':
                depth -= 1
                if depth == 0:
                    inner = parse_E(tokens[1:i])
                    if inner is None:
                        return None
                    val, length = inner
                    if length != i - 1:
                        return None
                    if i + 1 != len(tokens):
                        # after ')' something remains - parse_F requires full token consumption, so no
                        pass
                    return (val, i + 1)
        return None  # no matching )
    # else parse N
    n = parse_N(tokens)
    if n is None:
        return None
    return n

def parse_N(tokens):
    # N ::= 0 | 1B
    # B ::= empty | 0B | 1B
    if not tokens:
        return None
    t = tokens[0]
    if t == '0':
        return (0, 1)
    # else a binary number starting with 1
    # must be digit string starting with '1'
    if all(c in '01' for c in t) and t[0] == '1':
        # convert binary string to int
        val = int(t, 2)
        return (val, 1)
    return None

# To handle backtracking and multiple parses due to parentheses presence, we need full parser with memo.

# Instead, implement parser using memo and full backtracking with cache.

from functools import lru_cache

# We parse by grammar on token list with indices (l,r): tokens[l:r]

# Tokens are preprocessed, parse returns set of possible values for each grammar nonterminal to handle ambiguities.

# To handle parsing fully, implement parse_Q, parse_E, parse_T, parse_F, parse_N with memo and returning sets of values and full consumption check

# We want to confirm that the whole string is parsed exactly.

def parse_tokens(tokens):
    # Parse Q ::= E=E
    eq_positions = [i for i,t in enumerate(tokens) if t=='=']
    if len(eq_positions) != 1:
        return None
    eq_pos = eq_positions[0]
    left_vals = parse_E(0, eq_pos, tokens)
    right_vals = parse_E(eq_pos+1, len(tokens), tokens)
    if not left_vals or not right_vals:
        return None
    # Return list of (left_val, right_val) pairs
    result = []
    for lv in left_vals:
        for rv in right_vals:
            result.append((lv, rv))
    return result

@lru_cache(None)
def parse_E(l, r, tokens):
    # E ::= T | E+T | E-T
    # left-associative
    if l >= r:
        return set()
    res = set()
    # parse first T from l
    t_vals = parse_T(l, r, tokens)
    res |= t_vals
    for i in range(l+1, r-1):
        if tokens[i] == '+' or tokens[i] == '-':
            # E -> E + T
            left_vals = parse_E(l, i, tokens)
            right_vals = parse_T(i+1, r, tokens)
            for lv in left_vals:
                for rv in right_vals:
                    if tokens[i] == '+':
                        res.add(lv + rv)
                    else:
                        res.add(lv - rv)
    return res

@lru_cache(None)
def parse_T(l, r, tokens):
    # T ::= F | T*F
    if l >= r:
        return set()
    res = set()
    f_vals = parse_F(l, r, tokens)
    res |= f_vals
    for i in range(l+1, r-1):
        if tokens[i] == '*':
            left_vals = parse_T(l, i, tokens)
            right_vals = parse_F(i+1, r, tokens)
            for lv in left_vals:
                for rv in right_vals:
                    res.add(lv*rv)
    return res

@lru_cache(None)
def parse_F(l, r, tokens):
    # F ::= N | -F | (E)
    res = set()
    if l >= r:
        return res
    # -F
    if tokens[l] == '-':
        f_vals = parse_F(l+1, r, tokens)
        res |= set([-v for v in f_vals])
        return res
    # (E)
    if tokens[l] == '(' and tokens[r-1] == ')':
        e_vals = parse_E(l+1, r-1, tokens)
        res |= e_vals
        # return because if starts with '(' and ends with ')', we don't parse N also
        return res
    # N
    n_vals = parse_N(l, r, tokens)
    res |= n_vals
    return res

@lru_cache(None)
def parse_N(l, r, tokens):
    # N ::= 0 | 1B
    if r - l != 1:
        return set()
    t = tokens[l]
    if t == '0':
        return set([0])
    if t[0] == '1' and all(c in '01' for c in t):
        return set([int(t, 2)])
    return set()

# Now we implement function to replace letters by guessed chars and extract tokens

def construct_test_expr(mapping):
    arr = list(s)
    for c in letter_list:
        ch = mapping[c]
        for pos in letter_pos[c]:
            arr[pos] = ch
    return ''.join(arr)

def tokenize_expr(expr):
    res = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in '+-*()=':
            res.append(c)
            i += 1
        elif c == '(' or c == ')':
            res.append(c)
            i += 1
        elif c == '0':
            res.append('0')
            i += 1
        elif c == '1':
            j = i+1
            while j < len(expr) and expr[j] in '01':
                j += 1
            res.append(expr[i:j])
            i = j
        else:
            # invalid char
            return None
    return res

# Now brute force all mappings letter -> possible char, different letters different char

answer = 0

from itertools import permutations

if L > len(possible_chars):
    print(0)
    exit()

for perm in permutations(possible_chars, L):
    mapping = dict(zip(letter_list, perm))
    expr = construct_test_expr(mapping)
    tokens = tokenize_expr(expr)
    if tokens is None:
        continue
    # The original string s may contain chars which are letters replaced by mapping or other chars untouched
    # Now verify s matches the rule of letters mapping one to one unique char
    # It is guaranteed by construction.

    # parse Q from tokens
    parse_E.cache_clear()
    parse_T.cache_clear()
    parse_F.cache_clear()
    parse_N.cache_clear()
    results = parse_tokens(tokens)
    if results is None:
        continue
    # count how many solutions have lhs == rhs
    cnt = 0
    for lv, rv in results:
        if lv == rv:
            cnt += 1
    if cnt > 0:
        answer += cnt

print(answer)