import sys
from sys import stdin
input = stdin.readline

def main(args):
    while True:
        n = int(input())
        if n == -1:
            break
        q = []
        q.append(n % 4)
        while n > 3:
            n //= 4
            q.append(n % 4)
        q.reverse()
        print(''.join(map(str, q)))

if __name__ == '__main__':
    main(sys.argv[1:])