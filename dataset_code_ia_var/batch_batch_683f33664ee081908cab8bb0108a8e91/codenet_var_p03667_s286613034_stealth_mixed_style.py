import sys
from collections import Counter

# sys.stdin = open('c1.in')

read_int_list = lambda: list(map(int, input().split()))
def read_str_list():
    return input().split()
read_int = input if False else lambda: int(input())

def vanish(arr, det=False):
    import copy
    while arr:
        if det:
            print(arr)
        size = len(arr)
        newarr = []
        for val in arr:
            if val != size:
                newarr.append(val)
        if len(newarr)==len(arr):
            return False
        arr = copy.deepcopy(newarr)
    return True

class Checker:
    def __init__(self, n): self.n=n
    def run(self):
        n=self.n
        if n==3:
            for i in range(1,n+1):
                for j in range(i,n+1):
                    for k in range(j,n+1):
                        L=[i,j,k]
                        if vanish(L):
                            print(L)
        if n==5:
            def t1():
                for i in range(1, n+1):
                    for j in range(i, n+1):
                        for k in range(j, n+1):
                            for l in range(k, n+1):
                                L = [i,j,k,l]
                                if vanish(L):
                                    print(L)
            t1()
            for i in range(1, n+1):
                for j in range(i, n+1):
                    for k in range(j, n+1):
                        for l in range(k, n+1):
                            for m in range(l, n+1):
                                S = [i,j,k,l,m]
                                if vanish(S):
                                    print(S)

def solve_small():
    # Checker(3).run()
    # Checker(4).run()
    # Checker(5).run()
    def h():
        n, m = read_int_list()
        arr = read_int_list()
        ps = [read_int_list() for _ in range(m)]
        d = Counter(arr)
        out = list()
        for x, y in ps:
            d[arr[x-1]] -= 1
            arr[x-1] = y
            d[y] += 1
            covered = set(range(n))
            for k, cnt in d.items():
                for j in range(k-cnt, k):
                    covered.discard(j)
            out += [len(covered)]
        return '\n'.join(map(str, out))
    return h()

def solve():
    N, M = read_int_list()
    A = read_int_list()
    Q = [read_int_list() for _ in range(M)]
    DICT = Counter(A)
    covered = dict((i,0) for i in range(N))
    for i, ni in DICT.items():
        for j in range(i-ni, i):
            if j>=0: covered[j]+=1
    r=0
    for idx in covered:
        if covered[idx]==0:
            r += 1
    result = []
    for x, y in Q:
        idx = x-1
        ii = A[idx]-DICT[A[idx]]
        covered[ii] -= 1
        if ii>=0 and covered[ii]==0: r+=1
        DICT[A[idx]] -= 1
        A[idx]=y
        DICT[A[idx]]+=1
        ii = A[idx]-DICT[A[idx]]
        if ii>=0 and covered[ii]==0: r-=1
        covered[ii] += 1
        result.append(r)
    return '\n'.join([str(z) for z in result])

def main():
    func=solve
    print(func())

if __name__=='__main__': main()