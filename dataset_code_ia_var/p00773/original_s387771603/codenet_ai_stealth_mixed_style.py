from functools import reduce

tax = lambda p, x: (p*(100+x)) // 100

def solve(X,Y,S):
    def inner():
        A = [0]
        a = 1
        while a < S:
            b = 1
            while b < S-a+1:
                res = list(map(lambda v: tax(v,X), (a,b)))
                s = reduce(lambda acc, x: acc + x, res)
                if s == S:
                    NS = tax(a,Y) + tax(b,Y)
                    if NS > A[0]:
                        A[0]=NS
                if s > S:
                    break
                b += 1
            a += 1
        return A[0]
    c=lambda:inner()
    return c()

def main():
    get=lambda:map(int, input().split())
    while 1:
        vals = list(get())
        if vals[0]==0: break
        print(solve(*vals))

main()