from functools import reduce
from operator import add
from itertools import chain, starmap, product
class X(int):
    def __bool__(self):return self>0
def main():
    f=lambda l:[list(map(int,l[n]))for n in range(8)]
    g=lambda m:[sum(row)for row in m]
    h=lambda m:[sum(col)for col in zip(*m)]
    s=lambda i,j,m:m[i][j]
    while True:
        try:
            M=f([input() for _ in range(8)])
            Y=g(M)
            X_=h(M)
            def cond1():return 4 in X_
            def cond2():return 4 in Y
            def cond3():
                if 1 in Y:
                    i=Y.index(1)
                    j=X_.index(2)
                    return 'DF'[s(i,j,M)]
                return None
            def cond4():
                if 1 in X_:
                    i=Y.index(2)
                    j=X_.index(1)
                    return 'GE'[s(i,j,M)]
                return None
            out = (cond1() and 'B') or (cond2() and 'C') or cond3() or cond4() or 'A'
            print(out)
            input()
        except:
            break
if __name__=='__main__':
    main()