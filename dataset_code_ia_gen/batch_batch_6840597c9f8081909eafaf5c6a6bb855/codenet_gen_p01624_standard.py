import sys
sys.setrecursionlimit(10**7)

OPS = {'*', '+', '-', '&', '^', '|'}
PRI = {'*':4, '+':3, '-':3, '&':2, '^':1, '|':0}

def tokenize(s):
    tokens=[]
    i=0
    while i<len(s):
        c=s[i]
        if c in OPS or c in '()':
            tokens.append(c)
            i+=1
        else:
            j=i
            while j<len(s) and s[j].isdigit():
                j+=1
            tokens.append(s[i:j])
            i=j
    return tokens

def parse_expr(tokens):
    # Shunting yard parsing to AST using operator precedence and left associativity
    out=[]
    ops=[]
    def apply_op():
        op=ops.pop()
        r=out.pop()
        l=out.pop()
        out.append((op,l,r))
    i=0
    while i<len(tokens):
        t=tokens[i]
        if t=='(':
            ops.append(t)
        elif t==')':
            while ops and ops[-1]!='(':
                apply_op()
            ops.pop()
        elif t in OPS:
            while ops and ops[-1] in OPS and PRI[ops[-1]]>=PRI[t]:
                apply_op()
            ops.append(t)
        else:
            out.append(int(t))
        i+=1
    while ops:
        apply_op()
    return out[0]

def eval_ast(ast):
    if type(ast)==int:
        return ast
    op,l,r=ast
    lv=eval_ast(l)
    rv=eval_ast(r)
    if op=='*':
        return lv*rv
    elif op=='+':
        return lv+rv
    elif op=='-':
        return lv-rv
    elif op=='&':
        return lv & rv
    elif op=='^':
        return lv ^ rv
    elif op=='|':
        return lv | rv

def get_moves(expr):
    # generate all valid exprs from expr via one add or remove char,
    # valid expr means parseable and valid positive int rules
    res=[]
    chars = "()*+-&^|0123456789"
    n=len(expr)
    for i in range(n+1):
        # insert char
        for c in chars:
            newexpr=expr[:i]+c+expr[i:]
            if valid_expr(newexpr):
                res.append(newexpr)
    for i in range(n):
        newexpr=expr[:i]+expr[i+1:]
        if newexpr and valid_expr(newexpr):
            res.append(newexpr)
    return res

def valid_expr(s):
    # verify full validity per definition
    # attempt parse and check positive int no leading zeros
    try:
        tokens=tokenize(s)
        if not tokens:
            return False
        # check positive int format tokens
        for t in tokens:
            if t not in OPS and t not in ('(',')'):
                # positive integer: no leading zero except '0' itself not valid
                if t[0]=='0' and len(t)>1:
                    return False
                if t=='0':
                    return False
        parse_expr(tokens)
        return True
    except:
        return False

memo={}

def solve(N, expr):
    # minimax with memo: Max: even moves (Fukasawa), Min: odd moves (Komachi)
    # from expr, moves left: N, turn for player: 0(Fukasawa max) or 1(Komachi min)
    def dfs(e, n, turn):
        key=(e,n,turn)
        if key in memo:
            return memo[key]
        if n==0:
            val=eval_ast(parse_expr(tokenize(e)))
            memo[key]=val
            return val
        moves=get_moves(e)
        if turn==0:
            v=float('-inf')
            for ne in moves:
                v=max(v, dfs(ne,n-1,1))
        else:
            v=float('inf')
            for ne in moves:
                v=min(v, dfs(ne,n-1,0))
        memo[key]=v
        return v
    return dfs(expr,N,0)

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    if line=='0 #':
        break
    if ' ' in line:
        N,s=line.split(' ',1)
    else:
        N=line
        s=sys.stdin.readline().strip()
    N=int(N)
    print(solve(N,s))