import bisect as b
from collections import deque as dq
import sys,math,random
from heapq import heappush as hp,h as ho,heappop as hx
sys.setrecursionlimit(2*10**6)
MOD=10**9+7

I=lambda:int(sys.stdin.readline())
LI=lambda:[int(x) for x in sys.stdin.readline().split()]
def Legs(): return [list(x) for x in sys.stdin.readline().split()]
cs=lambda:list(sys.stdin.readline().rstrip('\n'))
def multi_i(n):return[I() for _ in range(n)]
def multi_li(n):return[LI() for _ in range(n)]

def process():
    n=I()
    s = cs()
    F = {'up':0,'low':0}
    i=0
    while i<len(s):
        c=s[i]
        if "A"<=c<="M": F['up']+=1
        elif"N"<=c<="Z": F['up']-=1
        elif'a'<=c<='m': F['low']+=1
        else: F['low']-=1
        i+=1
    out=[]
    idx=0
    while idx<len(s):
        c=s[idx]
        if c>='A' and c<='M':
            if F['up']>0:F['up']-=1;out.append(c)
        elif c>='N'and c<='Z':
            if F['up']<0:F['up']+=1;out.append(c)
        elif c>='a'and c<='m':
            if F['low']>0:F['low']-=1;out.append(c)
        elif c>='n'and c<='z':
            if F['low']<0:F['low']+=1;out.append(c)
        idx+=1
    print(f"{len(out)}")
    print("".join(map(str,out)))
    return 0

def main():
    process()

if __name__=='__main__':main()