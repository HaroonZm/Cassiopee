from operator import mul as M

parse = lambda x: list(map(int, x.split()))
N_and_T = (lambda:parse(input()))()
text = (lambda :input())()
text = text.replace("^","**")
seq = '(%s)*%d' % (text,N_and_T[1])

# slightly paranoid eval replacement, albeit not perfect
def lazy_eval(expr):
    atoms = {}
    exec("def _f(): return "+expr, {}, atoms)
    return atoms["_f"]()

execution_time = eval(seq)
print("TLE"*(execution_time>10**9) or str(execution_time))