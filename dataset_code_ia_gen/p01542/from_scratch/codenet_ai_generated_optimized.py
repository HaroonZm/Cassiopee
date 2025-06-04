from sys import setrecursionlimit
setrecursionlimit(10**7)

import sys
input=sys.stdin.readline

s=input().rstrip()

n=len(s)
dots=[i for i,ch in enumerate(s) if ch=='.']
m=len(dots)

chars=['0','1','+','-','*','(',')']

val_range=(0,2047)  # 2**11-1=2047 > 2**10-1=1023 but we stay within 0..1023 anyway

# Characters allowed at dots depend on position:
# But we try all chars each time, and test if expr is valid.

# Parsing and evaluating function:

# We'll implement a recursive parser with memoization over substring indices,
# and per substitution of dots.

# To handle dots, we'll generate all combos of replacements, at most 5 dots (max 16^5=~1M),
# but only 11 possible chars per dot (0,1,+,-,*,(,)), actually total of 8 chars ('0','1','+','-','*','(',')'); '.' excluded.

# To reduce number of tries:
#   for each dot, test possible replacements.

# We'll implement a parser that:
# - For each substring s[l:r], returns set of possible values (int)
#   or empty if no valid parse.
# Values are in 0..1023

# We'll build a cache: key=(l,r), value=set of possible values

# Because of dots, we create a new string with replaced chars and parse it.

# But trying all dot replacements for each substring separately is impossible.

# So we generate all possible strings with dots replaced, parse each, keep max result.

# At most 5 dots, 8 possible chars => 8^5=32768 tries max. This is acceptable.

# Implementation:

# Set of allowed chars for dot: '0','1','+','-','*','(',')'

dot_candidates=['0','1','+','-','*','(',')']

from collections import deque

def is_digit(c):
    return c=='0' or c=='1'

# We'll parse expression per precedence:

# Grammar:
# expression = Term (('+'|'-') Term)*
# Term = Factor ('*' Factor)*
# Factor = number | '(' expression ')'
# number = digit+

# During number parsing, number is binary string => int

def parse_expr(s):

    # Use recursive descent parsing with position index p.
    # Return (value, new_p) or raise exception

    length=len(s)
    p=0

    def parse_number():
        nonlocal p
        start=p
        if p>=length or not is_digit(s[p]):
            raise ValueError
        while p<length and is_digit(s[p]):
            p+=1
        num_b=s[start:p]
        val=int(num_b,2)
        if val>=1024:
            raise ValueError
        return val

    def parse_factor():
        nonlocal p
        if p<length and s[p]=='(':
            p+=1
            val=parse_expression()
            if p>=length or s[p]!=')':
                raise ValueError
            p+=1
            return val
        else:
            return parse_number()

    def parse_term():
        nonlocal p
        val=parse_factor()
        while True:
            if p<length and s[p]=='*':
                p+=1
                rval=parse_factor()
                val=val*rval
                if val<0 or val>=1024:
                    raise ValueError
            else:
                break
        return val

    def parse_expression():
        nonlocal p
        val=parse_term()
        while True:
            if p<length and (s[p]=='+' or s[p]=='-'):
                op=s[p]
                p+=1
                rval=parse_term()
                if op=='+':
                    val=val+rval
                else:
                    val=val-rval
                if val<0 or val>=1024:
                    raise ValueError
            else:
                break
        return val

    val=parse_expression()
    if p!=length:
        raise ValueError
    return val

max_res=-1

from itertools import product

# We do cartesian product over dots positions candidate chars.
for repl in product(dot_candidates,repeat=m):
    arr=list(s)
    for i,ch in zip(dots,repl):
        arr[i]=ch
    st=''.join(arr)

    # quick check balanced parentheses
    cnt=0
    for c in st:
        if c=='(':
            cnt+=1
        elif c==')':
            cnt-=1
            if cnt<0:
                break
    if cnt!=0:
        continue

    # next try parse and calculate
    try:
        v=parse_expr(st)
        if v>max_res:
            max_res=v
    except:
        pass

print(max_res) if max_res>=0 else print(-1)