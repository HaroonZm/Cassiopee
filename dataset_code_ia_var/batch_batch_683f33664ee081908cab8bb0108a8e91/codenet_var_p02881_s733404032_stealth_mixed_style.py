import sys
from math import sqrt

def SOLVE(N):
    S = sqrt(N)
    i = int(S) + 1
    while i > 0:
        if N % i == 0:
            res = lambda x, y: x - 1 + y - 1
            print(res(i, N // i))
            return None
        i -= 1
    else:
        sys.stdout.write("wrong...\n")

if __name__ == '__main__':
    exec("n=int(input())\nSOLVE(n)")