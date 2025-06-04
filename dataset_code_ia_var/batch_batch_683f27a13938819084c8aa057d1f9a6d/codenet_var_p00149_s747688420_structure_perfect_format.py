from collections import Counter

def check(f):
    if f >= 1.1:
        return "A"
    elif f >= 0.6:
        return "B"
    elif f >= 0.2:
        return "C"
    else:
        return "D"

dicl = Counter()
dicr = Counter()

while True:
    try:
        l, r = map(float, input().split())
        lx = check(l)
        rx = check(r)
        dicl[lx] += 1
        dicr[rx] += 1
    except EOFError:
        break

for alpha in ("A", "B", "C", "D"):
    print(dicl[alpha], dicr[alpha])