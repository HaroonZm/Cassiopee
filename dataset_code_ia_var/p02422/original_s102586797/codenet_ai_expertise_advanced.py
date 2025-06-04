from sys import stdin
from functools import partial

s = stdin.readline().rstrip()
q = int(stdin.readline())
readline = stdin.readline

for _ in range(q):
    op, *params = readline().split()
    a, b, *rest = map(int, params[:2]) + params[2:]
    if rest:
        p = rest[0]
        s = f"{s[:a]}{p}{s[b+1:]}"
    elif op == "reverse":
        s = f"{s[:a]}{s[a:b+1][::-1]}{s[b+1:]}"
    else:
        print(s[a:b+1])