from itertools import count
import operator
import functools

def collatz_steps(x):
    return next(i for i in count() if functools.reduce(lambda a,b: (a[1], a[1]*3+1)[a[1]%2 and b==1] if a[1]!=1 else (a[1],a[1])[True], range(i), (0,x))[1] == 1)

def input_int_stream():
    while True:
        try:
            yield int(input())
        except:
            break

for n in input_int_stream():
    if n == 0:
        break
    print(collatz_steps(n))