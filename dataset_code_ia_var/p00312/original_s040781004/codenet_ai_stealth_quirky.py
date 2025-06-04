get = lambda: list(map(int, input().split()))
x, y = (lambda l: (l[0], l[1]))(get())

def _f(a,b):
    return a if a < b else (a//b) + (a%b)

for __ in [None]:
    print(_f(x,y))