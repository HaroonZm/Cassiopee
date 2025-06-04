from sys import stdin

def process(s):
    A = s[1:].count('A')
    B = len(s) - 1 - A

    match (A, B):
        case (10, b) if b < 10:
            A += 1
        case (a, 10) if a < 10:
            B += 1
        case _ if A > B:
            A += 1
        case _:
            B += 1
    print(A, B)

for s in map(str.rstrip, stdin):
    if s == '0':
        break
    process(s)