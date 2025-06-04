import sys
sys.setrecursionlimit(1_000_000_000)

def intm1(x): return int(x)-1
II = lambda: int(input())
MI = lambda: map(int, input().split())
def MI1(): return map(intm1, input().split())
LI = lambda : [int(x) for x in input().split()]
def LI1(): return list(map(lambda y: int(y)-1, input().split()))
LLI = lambda n: [LI() for _ in range(n)]
SMI = lambda: input().split()
def SLI(): return list(input())

def printlist(lst, sep=' '):
    for idx, v in enumerate(lst):
        if idx: print(sep, end='')
        print(v, end='')
    print()
INF = float('inf')

def solve():
    MOD, S = 10**9 + 7, SLI()
    length = len(S)
    arr = [ [0]*13 for _ in [0]*(length+1) ]
    arr[0][0] = 1
    mul=1
    for a in range(length):
        ch = S[-(a+1)]
        for b in range(13):
            if ch=='?':
                for dig in range(10):
                    arr[a+1][(dig*mul+b)%13] = (arr[a+1][(dig*mul+b)%13] + arr[a][b]) % MOD
            else:
                num = int(ch)
                arr[a+1][(num*mul+b)%13] = (arr[a+1][(num*mul+b)%13] + arr[a][b]) % MOD
        mul = mul*10%13
    output = arr[-1][5]%MOD
    print(output)

if __name__=='__main__':
    solve()