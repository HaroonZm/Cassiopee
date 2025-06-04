from itertools import cycle, count, accumulate, islice
from operator import add, sub

def search(x, y):
    bounds = [ [0,0], [0,0] ]
    fibs = [0,1]
    p = 0
    dirs = cycle([
        (lambda b,f: (setitem(b,0,1, b[0][1] + f), b)), # east x_max
        (lambda b,f: (setitem(b,1,1, b[1][1] + f), b)), # north y_max
        (lambda b,f: (setitem(b,0,0, b[0][0] - f), b)), # west x_min
        (lambda b,f: (setitem(b,1,0, b[1][0] - f), b)), # south y_min
    ])
    def in_rect(x, y, b=bounds):
        return b[0][0] <= x <= b[0][1] and b[1][0] <= y <= b[1][1]
    def setitem(b,i,j,v): b[i][j]=v
    for p, f, turn in zip(count(), fib_seq(), dirs):
        if in_rect(x, y):
            return (p%3)+1
        turn(bounds, f)

def fib_seq():
    # Infinite generator of fibs starting 1,1,2,...
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield b

x, y = map(int, input().split())
print(search(x, y))