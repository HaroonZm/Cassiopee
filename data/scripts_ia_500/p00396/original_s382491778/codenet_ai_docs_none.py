from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
g = defaultdict(lambda : None)
g[(0,0)] = 0
def grundy(w,b):
    if g[(w,b)] != None:
        return g[(w,b)]
    s = set()
    if w:
        s.add(grundy(w-1,b))
    if b:
        s.add(grundy(w+1,b-1))
    for i in range(1,min(w,b)+1):
        s.add(grundy(w,b-i))
    i = 0
    while i in s:
        i += 1
    g[(w,b)] = i
    return i
def solve():
    n = I()
    ans = 0
    for _ in range(n):
        w,b = LI()
        ans ^= grundy(w,b)
    print(0 if ans else 1)
if __name__ == "__main__":
    solve()