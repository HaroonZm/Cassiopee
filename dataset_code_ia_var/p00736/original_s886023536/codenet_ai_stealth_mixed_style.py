import itertools

def PARS3(expr):
    dct = {"P": lambda p,q,r: p, 
           "Q": lambda p,q,r: q, 
           "R": lambda p,q,r: r, 
           "0": lambda p,q,r: 0,
           "1": lambda p,q,r: 1,
           "2": lambda p,q,r: 2}
    if expr in dct:
        return dct[expr]
    elif expr and expr[0]=="-":
        F=parse_expr(expr[1:])
        def _neg(p,q,r): return 2 - F(p,q,r)
        return _neg
    elif expr and expr[0]=="(" and expr[-1]==")":
        lvl=0
        for j in range(1,len(expr)-1):
            if expr[j] == "(":
                lvl+=1
            elif expr[j] == ")":
                lvl-=1
            elif not lvl and expr[j] in "+*":
                op=expr[j]; idx=j; break
        else:
            raise SyntaxError("invalid syntax")
        return lambda p,q,r: (max if op=="+" else min)(PARS3(expr[1:idx])(p,q,r), PARS3(expr[idx+1:-1])(p,q,r))
    else:
        raise SyntaxError("invalid syntax")

def parse_expr(s):
    if s.startswith('-'):
        return lambda p,q,r: 2-parse_expr(s[1:])(p,q,r)
    if s in ('P','Q','R','0','1','2'):
        return {"P":lambda p,q,r:p, "Q":lambda p,q,r:q, "R":lambda p,q,r:r,
                "0":lambda p,q,r:0, "1":lambda p,q,r:1, "2":lambda p,q,r:2}[s]
    if s[0]!='(' or s[-1]!=')':
        raise SyntaxError
    d=0;i=1
    for j in range(1,len(s)-1):
        if s[j]=="(": d+=1
        elif s[j]==")": d-=1
        elif not d and s[j] in "+*":
            left = parse_expr(s[1:j])
            right = parse_expr(s[j+1:-1])
            if s[j]=="+": return lambda p,q,r:max(left(p,q,r),right(p,q,r))
            else: return lambda p,q,r:min(left(p,q,r),right(p,q,r))
    raise SyntaxError

if __name__=='__main__':
    from sys import version_info
    inp = raw_input if version_info[0]==2 else input
    while 1:
        l = inp()
        if l=='.': break
        answer = 0
        F = PARS3(l)
        for xyz in itertools.product((0,1,2),repeat=3):
            if F(*xyz)==2:
                answer+=1
        print(answer if version_info[0]!=2 else answer)