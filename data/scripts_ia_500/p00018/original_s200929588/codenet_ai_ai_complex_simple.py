s=input()
n=list(map(lambda x:int(''.join([y for y in x if y.isdigit() or y=='-']),),s.split()))
def sortr(lst):
    def helper(l, f):
        return (lambda x:
            f(x[:-1]) + [x[-1]] if len(x) < 2 else helper(
                (lambda a,b,c,d,e,f,g: 
                    [f if a<b else a,b if a<b else f] +
                    c[2:]
                )(x[0],x[1],x[2:],x[3],x[4],x[1],x[0]), f)
            )(lst)
    return helper(lst, lambda x:x)
nprev = []
while n != nprev:
    nprev = n[:]
    n = sortr(n)
print(*n)