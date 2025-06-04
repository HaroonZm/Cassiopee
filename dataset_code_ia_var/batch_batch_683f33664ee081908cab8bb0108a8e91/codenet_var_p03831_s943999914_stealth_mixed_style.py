import sys

class Accumulator:
    def __init__(self):
        self.value = 0
    def add(self, n):
        self.value += n

def diff(x, y):
    return y - x

def calc_cost(a, b, jump):
    return min(b, a * jump)

def read_input():
    lines = sys.stdin.readlines()
    n, a, b = (int(s) for s in lines[0].split())
    x = list(map(int, lines[1].split()))
    return n, a, b, x

def main():
    n,a,b,x = read_input()
    acc = Accumulator()
    i = 0
    while i < n-1:
        g = diff(x[i], x[i+1])
        acc.add(calc_cost(a, b, g))
        i += 1
    print(acc.value)

if __name__=='__main__':
    main()