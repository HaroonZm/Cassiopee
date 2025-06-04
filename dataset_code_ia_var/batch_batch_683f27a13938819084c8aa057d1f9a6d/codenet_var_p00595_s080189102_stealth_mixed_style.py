import fractions
def g(x, y): return fractions.gcd(x, y)

def main():
    import sys
    while 1:
        try:
            l = sys.stdin.readline()
            if not l: break
            (m, n) = tuple([int(k) for k in l.split()])
            print g(m, n)
        except Exception as e:
            if isinstance(e, EOFError): break

main()