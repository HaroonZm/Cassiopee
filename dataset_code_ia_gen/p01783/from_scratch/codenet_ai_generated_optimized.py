import sys
sys.setrecursionlimit(10**7)

s = input()

usable = set("LR(),0123456789?")
digits = set("0123456789")

# We will parse the string into an expression tree, replacing '?' optimally,
# and get the max score or invalid.

# Grammar:
# expr := number | func_call
# number := non-empty digit sequence without leading zeros except '0'
# func_call := ('L'|'R') '(' expr ',' expr ')'

# We will parse with memo:
# parse(i,j) returns (max_value or None if invalid, fully replaced string, next_pos)

# But since we do not need to output string, only max score, we keep only max value.
# We need to fill '?' to maximize value.

# For efficient parsing, we'll parse from i to len(s). We return:
# set of parsed expressions from i:
# Because multiple substrings may be valid parsed exprs.

# But since we want the max score for the full string, we try to parse full string from 0 to len(s).


from functools import lru_cache

n = len(s)

# We define a helper to match a character set with '?':
def match_char(pos, cset):
    c = s[pos]
    return c == '?' or c in cset

# parse number starting at pos, return list of (value_str, value_int, end_pos)
def parse_number(pos):
    res = []

    # number cannot be empty, so length>=1
    # number digits=[0-9], leading zero only if the number is 0

    # try all substrings s[pos:end], end > pos
    # all characters digits or '?'
    # replace '?' by digits to maximize integer
    # highest int means longest (because of huge numbers), tie break by replacing '?' by '9'

    # To optimize:
    # from pos, extend as long as possible with match_char '? or digit'
    # generate candidate values by replacing '?' with '9'
    # discard if leading zero and length>1

    # So find max length substring of digits + '?'
    end = pos
    while end < n and match_char(end, digits):
        end += 1
    if end == pos:
        return []

    # at least one char
    substr = s[pos:end]

    # Leading zero?
    # if first char is '0' or '?':
    # if '?' replaced by '9' or '0' to maximize? '0' not maximizing, replace first '?' by '1' if possible,
    # to maximize number, first char '?' should be '9' except if that makes leading zero?

    # But number with leading zero only allowed if number == 0 (single digit '0').

    # We'll try all possible ways to replace '?' in substr:
    # but it's expensive, instead:

    # We'll replace '?' in first character:
    #   - if length>1, first char must be digit 1-9 (max is 9)
    #   - if length==1, first char can be 0-9

    # For rest chars, replace '?' by '9'

    # So we check first char:
    c0 = substr[0]
    # candidates for first char depending on length
    candidates = []
    if len(substr) == 1:
        if c0 == '?':
            for d in '9876543210':
                candidates.append(d + substr[1:].replace('?', '9'))
        else:
            candidates.append(substr.replace('?', '9'))
    else:
        # length>1
        # first char can't be '0' (or '?'=>0)
        if c0 == '?':
            for d in '987654321':
                candidates.append(d + substr[1:].replace('?', '9'))
        else:
            # first char digit but no zero
            if c0 == '0':
                return []
            candidates.append(substr.replace('?', '9'))

    for val_str in candidates:
        if val_str[0] == '0' and len(val_str) > 1:
            continue
        # check all chars digit
        if not all(ch in digits for ch in val_str):
            continue
        val_int = int(val_str)
        res.append((val_str, val_int, end))
    return res

@lru_cache(None)
def parse_expr(i):
    # returns list of (value:int, end_pos:int) for all valid expr from i
    # want to find all possible parsed expr from i and their max value
    res = []

    if i >= n:
        return []

    # Try parse number
    numbers = parse_number(i)
    for val_str, val_int, end_pos in numbers:
        res.append((val_int,end_pos))

    # Try parse func_call: 'L' or 'R' + '(' + expr + ',' + expr + ')'

    # pos i must be L or R or ?
    if i < n and (s[i] == 'L' or s[i] == 'R' or s[i] == '?'):
        first = [s[i]] if s[i] in ('L','R') else ['L','R']
        for func_letter in first:
            j = i + 1
            # next must be '(' or '?'
            if j >= n:
                continue
            if not match_char(j, '('):
                continue

            j1 = j + 1
            # parse expr 1 starting at j1
            expr1_list = parse_expr(j1)
            for (val1, pos1) in expr1_list:
                # after expr1 must be ',' or '?'
                if pos1 >= n:
                    continue
                if not match_char(pos1, ','):
                    continue
                pos2 = pos1 + 1
                # parse expr 2 starting at pos2
                expr2_list = parse_expr(pos2)
                for (val2, pos3) in expr2_list:
                    # after expr2 must be ')' or '?'
                    if pos3 >= n:
                        continue
                    if not match_char(pos3, ')'):
                        continue
                    end_pos = pos3 + 1
                    # compute value:
                    if func_letter == 'L':
                        val = val1
                    else:
                        val = val2
                    res.append((val,end_pos))
    return res

# parse all expr starting at 0 that consumes whole string
parsed = parse_expr(0)
max_val = -1
for val,end_pos in parsed:
    if end_pos == n:
        max_val = max(max_val,val)

if max_val == -1:
    print("invalid")
else:
    print(max_val)