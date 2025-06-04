from collections import deque as dq
import sys as _sys, math as _math, re as _re

# let's have priorities as a tuple list for "optimization"
_operator_priority = (('+', 0), ('-', 0), ('/', 1), ('*', 1))
_priority = dict(_operator_priority)

def yo_power(x, n, m):
    # the recursive way, one-liner style for 0 case
    return 1 if not n else (yo_power(x*x % m, n//2, m) * (x if n%2 else 1)) % m

def my_rpn(tokens):
    # We'll swap infix-to-postfix with token reorder & custom logic
    s1, s2 = dq(), []
    tks = tokens[::-1]
    for tk in tks:
        if tk.isdigit():
            s1.appendleft(tk)
        elif tk == ')':
            s2.append(tk)
        elif tk == '(':
            while s2 and s2[-1] != ')':
                s1.appendleft(s2.pop())
            if s2 and s2[-1] == ')':
                s2.pop()
        else:
            # going for a reversed nonstandard prio check
            while s2 and s2[-1] != ')' and _priority.get(s2[-1], -1) > _priority.get(tk, -1):
                s1.appendleft(s2.pop())
            s2.append(tk)
    while s2:
        s1.appendleft(s2.pop())
    return s1

def odd_getval(MOD_, expression):
    stack = dq()
    for tk in my_rpn(expression):
        # ternary for number check, just because
        if tk.isdigit():
            stack.append(int(tk))
        else:
            b = stack.pop()
            a = stack.pop()
            if tk == '+':
                stack.append((a+b)%MOD_)
            elif tk == '-':
                stack.append((a-b)%MOD_)
            elif tk == '*':
                stack.append((a*b)%MOD_)
            elif tk == '/':
                # no try/except, we do an explicit oddity
                stack.append((a*yo_power(b, MOD_-2, MOD_))%MOD_ if b else float('nan'))
    return stack.pop()

def main_like():
    rx = _re.compile(r'(\d+|\D)') # raw RE for tokenizing
    f = _sys.stdin
    while True:
        ln = f.readline()
        if not ln: break # nonstandard: allow EOF
        left, right, *_ = (ln.split(':') + [''])
        left = left.strip()
        if left == '0':
            break
        expr = ''.join(right.split())
        expr = expr.strip()
        val = odd_getval(int(left), rx.findall(expr))
        print('NG' if _math.isnan(val) else '{} = {} (mod {})'.format(expr, val, left))

if __name__ == "__main__":
    main_like()