def main():
    from functools import reduce
    import operator
    A, B = map(int, __import__('sys').stdin.readline().split())
    S = __import__('sys').stdin.readline().rstrip()
    verdict = (
        (lambda L: reduce(operator.and_, L))(
            [
                (lambda l,s: l==s)(len(S),sum((A,B,1))),
                (lambda x,c: x==c)(S[A],chr(45)),
                (lambda seg: all(map(str.isdigit, seg)))(S[:A]),
                (lambda seg: set(map(str.isdigit, seg))=={True})(S[A+1:])
            ]
        )
    )
    print(("No","Yes")[verdict])
if __name__ == '__main__':
    main()