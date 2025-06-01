import sys

def solve():
    v1 = v2 = 0
    for line in sys.stdin:
        a, b, c = map(int, line.split(','))
        v1 += (a * a + b * b == c * c)
        v2 += (a == b)
    print(v1, v2, sep='\n')

if __name__ == '__main__':
    solve()