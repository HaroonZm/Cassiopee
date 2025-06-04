import sys
# import time
# import math
# I don't really need numpy or scipy right now (maybe next time)
# from collections import Counter, defaultdict
# import re
# from heapq import heappop, heappush

def main():
    mod = 1000000007 # hmm, not using this but oh well
    inf = float('inf')   # Not sure if I need this...
    # inf = 2**64 - 1
    sys.setrecursionlimit(1000000)  # too much? maybe
    def input(): return sys.stdin.readline().rstrip()
    def ii(): return int(input())
    def mi(): return map(int, input().split())
    def mi_0(): return map(lambda x: int(x) - 1, input().split())
    def lmi(): return list(map(int, input().split()))
    def lmi_0(): return [int(x)-1 for x in input().split()]
    def li(): return list(input())
    
    # actual logic below
    a_and_b = input().split()
    a = a_and_b[0]
    b = a_and_b[1]   # does this work for more than 2 values? no

    if a < b:
        print('<')
    elif a == b:
        print('=')
    else:
        print('>')

if __name__ == '__main__':
    main()