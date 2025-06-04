import sys
sys.setrecursionlimit(10**7)

N,K=map(int,input().split())
parts={}
for _ in range(K):
    p,h=input().split()
    h=int(h)
    bars=[]
    for __ in range(h-1):
        row=list(map(int,input().split()))
        bars.append(row)
    perm=list(range(N))
    # build permutation for one part
    # simulate amida
    def part_perm():
        res=perm[:]
        for row in bars:
            i=0
            while i<N-1:
                if row[i]==1:
                    res[i],res[i+1]=res[i+1],res[i]
                    i+=2
                else:
                    i+=1
        return res
    pp=part_perm()
    # Build inverse permutation for mapping top->bottom
    # Since the simulation gave final labels position, we want the permutation mapping input positions to outputs
    # The permutation pp shows the output order of input positions
    # So permutation p maps i to pp[i]
    # But to compose permutations as function composition, we use zero-based arrays,
    # where p[i] = position after transformation of i
    parts[p]=pp

E=int(input())

# Parse expression into sequence list: element is (type, value)
# type: 'part' for single part, 'seq' for sequence, 'repeat' for repeated sequence
# we parse into nested structure and then build overall permutation
#
# Grammar:
# expression := term {'+' term}
# term := factor | number '(' expression ')'
# factor := uppercase letter
# number := integer

import re
token_re=re.compile(r'[A-Z]|\d+|\+|\(|\)')

class Parser:
    def __init__(self,s):
        self.tokens=token_re.findall(s)
        self.pos=0
    def peek(self):
        return self.tokens[self.pos] if self.pos<len(self.tokens) else None
    def consume(self,t=None):
        if t is not None and self.peek()!=t:
            raise ValueError('Expected '+t+' but got '+str(self.peek()))
        v=self.peek()
        self.pos+=1
        return v
    def parse_expression(self):
        terms=[self.parse_term()]
        while self.peek()=='+':
            self.consume('+')
            terms.append(self.parse_term())
        if len(terms)==1:
            return terms[0]
        return ('seq',terms)
    def parse_term(self):
        if self.peek() and self.peek().isdigit():
            n=int(self.consume())
            self.consume('(')
            exp=self.parse_expression()
            self.consume(')')
            return ('repeat',n,exp)
        else:
            return self.parse_factor()
    def parse_factor(self):
        t=self.peek()
        if t is None:
            raise ValueError('Unexpected end')
        if re.match('[A-Z]',t):
            self.consume()
            return ('part',t)
        else:
            raise ValueError('Unexpected token '+str(t))

def compose(p,q):
    # compose two permutations p,q of size N: return p(q(x))
    # permutations are lists of size N where p[i] is image of i
    return [p[q[i]] for i in range(N)]
def pow_perm(p,k):
    # fast exponentiation of permutation p to k-th power
    res=list(range(N))
    base=p[:]
    while k>0:
        if k&1:
            res=compose(base,res)
        base=compose(base,base)
        k>>=1
    return res
def eval_exp(exp):
    if exp[0]=='part':
        return parts[exp[1]]
    if exp[0]=='seq':
        res=list(range(N))
        for sub in exp[1]:
            res=compose(eval_exp(sub),res)
        return res
    if exp[0]=='repeat':
        n,sub=exp[1],exp[2]
        p=eval_exp(sub)
        return pow_perm(p,n)

for _ in range(E):
    line=input()
    p=Parser(line)
    exp=p.parse_expression()
    ans=eval_exp(exp)
    # output: for input positions 0..N-1, numbering from 1..N
    # ans[i] is output position of i, zero-based
    # We need to output the output permutation that transforms 1..N to after amida, so output ans mapped +1
    # But the problem says output the labels at the bottom in the order from left to right
    # The labels at bottom are from top (1..N) mapped according to amida: for each i from top 1 to N,
    # we follow amida down and reach ans[i] (0-based index)
    # So output is bottom labels as per ans
    # output ans but +1
    print(*[a+1 for a in ans])