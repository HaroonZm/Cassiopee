import sys

# variables: a,b,c,d
# values: 0 or 1
# total 16 combinations of (a,b,c,d)
# We represent each expression by a 16-bit integer, each bit is the output for one input

def vars_to_bits():
    # generate mapping from variable to 16-bit value
    table = {}
    for v in ['a','b','c','d']:
        bits = 0
        for i in range(16):
            # bit is 1 if corresponding variable bit in i is 1
            if v=='a':
                bit = (i>>3)&1
            elif v=='b':
                bit = (i>>2)&1
            elif v=='c':
                bit = (i>>1)&1
            elif v=='d':
                bit = i&1
            bits |= (bit << i)
        table[v] = bits
    return table

var_bits = vars_to_bits()

# Functions to evaluate operators on 16 bit masks
def negate(x):
    return (~x)&0xFFFF

def xor(x,y):
    return x ^ y

def andop(x,y):
    return x & y

# Parse expression to get its 16bit evaluation
# Also find minimal length expression for each 16bit result by combining

# We'll store for each bit pattern, the minimal length expression that evaluates to it

# Approach:
# - parse given expr to get bit pattern
# - build expr length dictionary with initial expr
# - then try to reduce expression length by checking equivalent expressions with same bit pattern, by applying rules:
#   - double negation
#   - commutativity of AND and XOR (min lengths among permutations)
#   - simplification like 0,1 and variables where possible
#   But since we want a beginner solution and code simple, we'll do only basic memo and parsing and simple length calculation

# So instead, we parse expr, compute bit pattern, and then BFS or DP to find shortest length expression for that bit pattern

# We'll build a dict: best_len[bit_pattern] = minimal length expr

# Initially known:
# - 0: '0' length 1
# - 1: '1' length 1
# - var_bits: variables length 1 each

# We use BFS to build from simple expressions to complex

from collections import deque

def expr_to_bits(s):
    # parse s, return bit pattern and length (length is len(s))
    # parse using recursive descent according to grammar

    # Grammar:
    # <E> ::= 0 | 1 | a | b | c | d | -<E> | (<E> ^ <E>) | (<E> * <E>)
    #
    # We'll parse with a pointer

    pos = 0
    n = len(s)

    def parse_expr():
        nonlocal pos
        if pos >= n:
            return None
        c = s[pos]
        if c in '01abcd':
            pos += 1
            if c == '0':
                return 0,1
            elif c == '1':
                return 0xFFFF,1
            else:
                return var_bits[c],1
        elif c == '-':
            pos += 1
            val, length = parse_expr()
            return negate(val), length+1
        elif c == '(':
            pos += 1
            left_val, left_len = parse_expr()
            if pos >= n:
                return None
            op = s[pos]
            if op not in ['^','*']:
                return None
            pos += 1
            right_val, right_len = parse_expr()
            if pos >= n or s[pos] != ')':
                return None
            pos += 1
            if op == '^':
                val = xor(left_val,right_val)
            else:
                val = andop(left_val,right_val)
            length = left_len + right_len + 3 # ( ) and op
            return val,length
        else:
            return None

    val,length = parse_expr()
    return val,length

# We will precalc minimal length expressions for all 2^16 = 65536 possible values,
# starting from initial known expressions.

best_len = {}

# initialize with constants and variables
best_len[0] = 1 # "0"
best_len[0xFFFF] = 1 # "1"
for v in ['a','b','c','d']:
    best_len[var_bits[v]] = 1

# We'll keep a queue of newly found expressions to try combining with others
queue = deque()
# initialize queue with known expressions: bit-pattern,value,length
for k in best_len:
    queue.append(k)

# Since max expression is 16 chars, and we only save lengths, we just try to build expressions by:
# - applying negation to known expressions
# - applying operators ^ and * between known expressions
# - also storing minimal length for each pattern

# Because we are beginner code, do a loop with a limit of iterations

for _ in range(100000):
    if not queue:
        break
    x = queue.popleft()
    lenx = best_len[x]
    # negation
    nx = negate(x)
    new_len = lenx + 1
    if nx not in best_len or best_len[nx] > new_len:
        best_len[nx] = new_len
        queue.append(nx)
    # combine with all known expressions so far
    # to limit complexity, we only combine with values in best_len keys (convert to list snapshot)
    keys_list = list(best_len.keys())
    for y in keys_list:
        leny = best_len[y]
        # xor
        v = xor(x,y)
        l = lenx + leny + 3 # (x^y)
        if v not in best_len or best_len[v] > l:
            best_len[v] = l
            queue.append(v)
        # and
        v = andop(x,y)
        l = lenx + leny + 3 # (x*y)
        if v not in best_len or best_len[v] > l:
            best_len[v] = l
            queue.append(v)

for line in sys.stdin:
    line=line.strip()
    if line=='.':
        break
    val,length = expr_to_bits(line)
    # output minimal length
    if val in best_len:
        print(best_len[val])
    else:
        # fallback print length parsed
        print(length)