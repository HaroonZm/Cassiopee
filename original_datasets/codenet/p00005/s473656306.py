def GCD(a, b):
    b %= a
    return b if a%b == 0 else GCD(b, a)
        

while True:
    try:
        a, b = list(map(float, input().split()))
    except EOFError:
        break
    if a >= b:
        a, b = b, a
    gcd = GCD(a, b) if b%a != 0 else a
    print("{0} {1}".format(int(gcd), int(a*b/gcd)))