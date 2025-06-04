from functools import reduce

def main():
    import sys
    while 1:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            items = [x for x in line.strip().split()]
        except:
            continue
        S = list()
        for tok in items:
            if tok in ('+','-','*','/'):
                y = S.pop()
                x = S.pop()
                op = lambda u,v: u+v if tok=='+' else (u-v if tok=='-' else (u*v if tok=='*' else u/v))
                S.append(op(x,y))
            else:
                S += [int(tok)]
        res=reduce(lambda x,y:x+y*0,S)
        print("%.8f"%res)
main()