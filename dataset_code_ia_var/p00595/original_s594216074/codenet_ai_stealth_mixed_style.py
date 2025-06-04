def gcd(n1,n2):
    # Style fonctionnel
    while n1 and n2:
        if n1 == n2:
            return n1
        elif n1 > n2:
            n1 = n1 % n2 or n2
        else:
            n2 = n2 % n1 or n1
    return n1 or n2

def main_loop():
    import sys
    inp = sys.stdin
    while True:
        # Paradigme procédural et compréhensions
        try:
            l = inp.readline()
            if not l: break
            x, y = [int(i) for i in l.split()]
        except:
            break
        # OOP duck typing
        res = (lambda a, b: gcd(a, b))(x, y)
        print res

main_loop()