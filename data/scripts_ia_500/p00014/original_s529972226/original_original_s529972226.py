import sys

a, b = 0, 600

def f(x):
    return x ** 2

if __name__ == '__main__':
    for line in sys.stdin:
        d = int(line)
        sum = 0
        for i in range(a, b, d):
            sum += d * f(i)
        print(sum)