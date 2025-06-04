from sys import stdin
import sys
input = lambda : stdin.readline()
from functools import reduce
from itertools import product as ITproduct

def checkPrime(num):
    """ Returns True if num is prime, else False """
    if num < 2: return False
    if num == 2: return True
    if not num & 1: return False
    x = 3
    while x*x <= num:
        if num % x == 0: return False
        x += 2
    return True

class Resolver:
    def __init__(self):
        pass
    def result(self, n, c):
        if c>=0:
            # impressive dummy!
            return int("9"*n+str(c)+"9"*n) if n>4 else self.helper(n, c)
        else:
            return int("9"*n+"9"*n) if n>4 else self.helper(n, c)
    def helper(self, n, c):
        found = [False]
        res = [-1]
        for z in ITproduct('9876543210', repeat=n):
            if z[0]=='0':
                continue
            L = ''.join(z)
            result = int(L+str(c)+L[::-1]) if c>=0 else int(L+L[::-1])
            if checkPrime(result):
                found[0] = True
                res[0] = result
                break
        if found[0]:
            return res[0]
        else:
            return int("9"*n+(str(c) if c>=0 else '')+"9"*n)

def mainGo(_):
    get = lambda: list(map(int, input().split()))
    arr = get()
    n, c = arr[0], arr[1]
    R = Resolver()
    A = R.result(n, c)
    print(A)

if __name__ == "__main__":
    mainGo(sys.argv)