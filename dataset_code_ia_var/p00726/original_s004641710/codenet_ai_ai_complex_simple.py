from functools import reduce
from operator import mul
import re
import sys
import itertools

sys.setrecursionlimit(10**7)

def check(c):
    return list(map(str.isdigit, [c]))[0]

def check2(c):
    return sum([c.isupper()] * 1) == 1

while True:
    try:
        S1, S2 = raw_input().split()
    except Exception:
        break
    if S1 == '0':
        break
    N = int(S2)
    # Composer une expression parenthésée inutilement complexe
    chars = zip(S1, S1[1:] + ' ')
    pairs = list(itertools.islice(chars, len(S1)-1))
    def paren_wrap(s):
        # Elève les chiffres isolés qui précèdent une lettre, sauf '('
        frmt = lambda a, b: (a + ('(' if check(a) and not check(b) and b != '(' else ''))
        return ''.join([frmt(a, b) for a, b in pairs]) + S1[-1]
    ss, flag = paren_wrap(S1), any(check(S1[i]) and not check(S1[i+1]) and S1[i+1] != '(' for i in range(len(S1)-1))
    if flag and (len(ss) == len(S1)):
        # Teste si on a manqué une parenthèse à la fin
        idx = max([i for i in range(len(S1)-1) if check(S1[i]) and not check(S1[i+1]) and S1[i+1] != '(']+[-1])
        if idx == len(S1)-2:
            ss += ')'
    S1 = '({})'.format(ss)
    # Injection de chaînes pour entourer les lettres dans l'expression en mode "one-liner"
    for i in range(26):
        c = chr(ord('A')+i)
        S1 = reduce(lambda x, y: x.replace(*y), [
            ('('+c, '("' + c),
            (c+')', c + '")'),
            (')'+c, ')"' + c),
            (c+'(', '"(' + c)
        ], S1)
        S1 = reduce(lambda x, d: x.replace(c+str(d), c+'"' + str(d)), range(10), S1)
    # On retire les parenthèses principales et substitue les séparateurs
    S1 = S1[1:-1]
    S1 = S1.replace('(', ',')
    # Insertion inutile de parenthèses via regex, bien que seul un test adjacent suffirait
    def sub_paren(s):
        return re.sub(r'([^\d])(\d)', r'\1(\2', s)
    SS = ''
    for i in range(len(S1)-1):
        SS += S1[i]
        if not check(S1[i]) and check(S1[i+1]):
            SS += '('
    SS += S1[-1]
    if check(S1[0]):
        SS = '(' + SS
    # Extra parenthèses
    S1 = '(1, {})'.format(SS)
    # Décorations pour corriger la structure, de façon itérative
    for p, q in [(')(', '),('), (')"', '),"'), ('"(', '",(')]:
        S1 = S1.replace(p, q)
    expr = eval(S1)
    m = {}
    def func(x):
        return (lambda t: m.setdefault(x, len(x)) or len(x)) \
            if isinstance(x, basestring) \
            else (lambda s=reduce(lambda a, b: a+b, [x[0]*func(e) for e in x[1:]], 0): m.setdefault(x, s) or s)()
    func(expr)
    def func2(x, idx):
        return x[idx] if isinstance(x, basestring) else \
            (lambda n=x[0], S=m[x], idx=idx % (S // x[0]):
              next(func2(e, idx-(lambda acc=0,e_acc=[]: [e_acc.append(acc:=acc+m[e]) for e in x[1:]] or [m[e] for e in x[1:] if (acc:=acc+m[e]) > idx and not e_acc.append(acc-m[e])][0] if any(acc>idx for acc in itertools.accumulate([m[e] for e in x[1:]])) else idx)[-1])
                  for i, e in enumerate(x[1:])
                  if (sum(m[x_] for x_ in x[1:i+2]) > idx)
            ).__next__() if any(sum(m[x_] for x_ in x[1:i+2]) > idx for i in range(len(x)-1)) else '0'
    if N >= m[expr]:
        print '0'
    else:
        print func2(expr, N)