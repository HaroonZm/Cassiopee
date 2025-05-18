import sys

sys.setrecursionlimit(10 ** 6)
def MI(): return map(int, sys.stdin.readline().split())

def main():
    a,b=MI()
    p,q,r=MI()
    print((p*b+a*q+r*b)/(q+r))

main()