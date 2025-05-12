import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n,m = map(int,input().split())
x = list(map(int,input().split()))

from collections import Counter, defaultdict
c = Counter(x)
cc = defaultdict(list)
onum = defaultdict(int)
esum = defaultdict(int)
for k,v in c.items():
    cc[k%m].append(v)
    if v%2:
        onum[k%m] += 1
        esum[k%m] += v-1
    else:
        esum[k%m] += v
    
def sub(l, o):
    return sum(item//2 for item in l) + o//2
def sub2(l1, o1, l2, o2, e1, e2):
    if o1==o2:
        return sum(item//2 for item in l1) + sum(item//2 for item in l2) + o1
    elif o1<o2:
        o1, o2 = o2, o1
        l1, l2 = l2, l1
        e1, e2 = e2, e1
    ans = 0
    ans += o2
    o1 = o1 - o2
    if o1 <= e2:
        ans += o1
        e2 -= o1
        ans += (e1//2) + (e2//2)
    else:
        ans += e2
        ans += (e1//2)
    return ans

if m%2==0:
    ans = 0
    ans += sub(cc[0], onum[0])
    ans += sub(cc[m//2], onum[m//2])
    for k in range(1,m//2):
        ans += sub2(cc[k], onum[k], cc[m-k], onum[m-k], esum[k], esum[m-k])
else:
    ans = 0
    ans += sub(cc[0], onum[0])
    for k in range(1,m//2+1):
        ans += sub2(cc[k], onum[k], cc[m-k], onum[m-k], esum[k],  esum[m-k])
print(ans)