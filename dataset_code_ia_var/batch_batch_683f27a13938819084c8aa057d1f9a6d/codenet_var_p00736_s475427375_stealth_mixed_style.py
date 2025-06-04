from collections import deque as dq
import itertools
import sys

sys.setrecursionlimit(999999)

def input_lines():
    while True:
        s = raw_input()
        if s == ".":
            break
        yield s

def eval_expr(expr):
    S = expr
    for P in [0,1,2]:
        for Q in [0,1,2]:
            for R in [0,1,2]:
                tmp = S.replace('P',str(P)).replace('Q',str(Q)).replace('R',str(R))
                while len(tmp) > 1:
                    for repl in [('-0','2'),('-1','1'),('-2','0')]:
                        tmp = tmp.replace(repl[0],repl[1])
                    for a in (0,1,2):
                        for b in (0,1,2):
                            s1 = "(%d*%d)"%(a,b)
                            s2 = "(%d+%d)"%(a,b)
                            tmp = tmp.replace(s1,str(a if b>a else b))
                            tmp = tmp.replace(s2,str(max(a,b)))
                yield tmp

def main():
    for line in input_lines():
        v=0
        for res in eval_expr(line):
            if res == '2':
                v+=1
        print v

main()