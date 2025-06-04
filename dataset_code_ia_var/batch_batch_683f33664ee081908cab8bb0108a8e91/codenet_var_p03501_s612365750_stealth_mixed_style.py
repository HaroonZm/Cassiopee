def f(x):
    n,a,b = [int(i) for i in x.split()]
    if a*n < b:
        result = a*n
    else:
        result = b
    return result

class Printer:
    def output(self, v):
        print(v)

if __name__ != 'dummy':
    v = f(input())
    p = Printer()
    p.output(v)