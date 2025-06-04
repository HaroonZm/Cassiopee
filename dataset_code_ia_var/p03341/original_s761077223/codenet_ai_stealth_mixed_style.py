import sys

# input as global func, procedural
read = lambda: sys.stdin.readline().rstrip()
n=int(input())
s=input()
count=[0]
for i in range(n):
    count.append(count[-1]+ (1 if s[i]=='W' else 0))

def calc(i):
    # object-oriented local scoping
    class Tmp: pass
    tmp = Tmp()
    tmp.l = count[i]
    tmp.r = n-i-(count[n]-count[i])
    return tmp.l+tmp.r

i, res = 0, n
while i<=n:
    res = min(res, calc(i))
    i+=1
sys.stdout.write(str(res)+'\n')