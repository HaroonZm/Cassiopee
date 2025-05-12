import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
X,Y = LI()
ans = 1
while 2*X<=Y:
    X *= 2
    ans += 1
print(ans)