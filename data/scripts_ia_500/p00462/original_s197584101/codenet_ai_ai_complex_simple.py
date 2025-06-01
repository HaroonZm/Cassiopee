import sys
from sys import stdin
from bisect import bisect_right as br
input = stdin.readline

def main(argv):
    def fold(x,y):return y-x if y>=x else y+L-x
    while 1:
        global L;L=int(input())
        if not L:break
        N,M=int(input()),int(input())
        W=[int(input())for _ in range(N-1)]
        D=[int(input())for _ in range(M)]
        W+= [0,L]
        W.sort()
        C=list(map(lambda z:L-z, W))
        C.sort()
        acc=0
        for t in D:
            if not t:continue
            i,j=br(W,t),br(C,L-t)
            a,b=W[i]-t,t - W[i-1]
            c,d=C[j]- (L - t),(L - t) - C[j-1]
            min_dist=min(min(a,b),min(c,d))
            acc+=min_dist
        print(acc)

if __name__=="__main__":
    main(sys.argv[1:])