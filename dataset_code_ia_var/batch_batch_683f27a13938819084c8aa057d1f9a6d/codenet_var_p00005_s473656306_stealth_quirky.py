def gcdish(X, Y):
    # Personal flavor: tail recursion in a loop!
    while X and Y:
        X, Y = Y % X, X
    return Y + X

def reader(prompt='> '):
    # Personalized interactive input handler
    while True:
        try:
            raw = input(prompt)
        except:
            break
        if not raw.strip():
            continue
        stuffs = [float(j) for j in raw.strip().split()]
        if len(stuffs) != 2:
            print("Two numbers please.")
            continue
        yield tuple(stuffs)

for duo in reader('--> '):
    a, b = sorted(duo)
    which_gcd = gcdish(a, b) if b % a else a
    out = "%d %d" % (which_gcd, a*b//which_gcd if which_gcd else 0)
    print(out)