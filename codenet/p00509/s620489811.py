"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0586

"""
import sys
from sys import stdin
from itertools import product
input = stdin.readline

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def solve(n, c):
    if c >= 0:
        dummy = int('9'*n + str(c) + '9'*n)
    else:
        dummy = int('9'*n + '9'*n)

    # https://www.ioi-jp.org/joi/2005/2006-m1-prob_and_sol/2006-m1-t5-review.html
    if n > 4:
        return dummy

    found = False
    ans = -1
    for p in product('9876543210', repeat=n):
        if p[0] == '0':
            continue
        t = ''.join(p)
        if c >= 0:
            ans = int(t + str(c) + t[::-1])
        else:
            ans = int(t + t[::-1])
        if is_prime(ans):
            found = True
            break

    if found:
        return ans
    else:
        return dummy

def main(args):
    n, c = map(int, input().split())
    result = solve(n, c)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])