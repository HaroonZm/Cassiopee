import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
A = LI()
B = sorted(set(A))
d = {}
for b in B:
    d[b] = 0
for a in A:
    d[a] += 1

C = [d[b] for b in B]

ans = len(B)
x = sum(c-1 for c in C)
if x % 2 == 1:
    ans -= 1

print(ans)