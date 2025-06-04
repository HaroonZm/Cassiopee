import sys
from collections import deque

def myShuffle(arr, c):
    n = len(arr)
    s = n//2 if n%2==0 else (n-1)//2
    a1 = arr[s:]
    a2 = arr[:s]
    result = []
    idx = 0
    while True:
        k = 0
        for i in range(c):
            if k<len(a1): result.append(a1[0]); a1=a1[1:]; k+=1
        k = 0
        for i in range(c):
            if k<len(a2): result.append(a2[0]); a2=a2[1:]; k+=1
        if not a1 and not a2: break
    return result

def parse_and_run():
    while 1:
        line = sys.stdin.readline()
        if line == '': break
        data = line.strip().split()
        if not data: continue
        n, r = (lambda lst: (int(lst[0]), int(lst[1])))(data)
        deck = list(i for i in range(n))
        cc = [int(x) for x in sys.stdin.readline().strip().split()]
        i=0
        while i<r:
            deck = myShuffle(deck, cc[i])
            i+=1
        print(deck[len(deck)-1])
parse_and_run()