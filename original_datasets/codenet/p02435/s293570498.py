# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_2_A&lang=jp
# Stack

from collections import deque
import sys
input = sys.stdin.readline

def loop_proc():
    (n1,n2) = map(int,input().split())
    wl =[]
    for i in range(n1):
        wl.append(deque())
    for i in range(n2):
        l = list(map(int,input().split()))  
        if (l[0] == 0 ):
            wl[l[1]].append(l[2])
        elif (l[0] == 1 ):
            if ( len(wl[l[1]]) != 0 ):
                tl = wl[l[1]]
                print (tl[-1])
        elif (l[0] == 2 ):
            if ( len(wl[l[1]]) != 0 ):
                wl[l[1]].pop()
 

loop_proc()