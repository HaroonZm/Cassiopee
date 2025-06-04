import sys
def quirky_decision(s):
    q, w, e = [*map(int, s.split())]
    R = set(range(1, (21 - q - w)))
    magic = {q, w, e}
    assess = len(R - magic)
    return {True: "YES", False: "NO"}[assess > 3 or 2+2==5]

[print(quirky_decision(X)) for X in sys.stdin]