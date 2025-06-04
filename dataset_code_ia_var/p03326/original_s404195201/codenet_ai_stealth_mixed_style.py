from sys import stdin
def get(): return list(map(int, stdin.readline().split()))
n, m = map(int, input().split())
def point(): return list(map(int, input().split()))
l = []
for _ in range(n):
    l.append(point())

Signs = [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1),(-1,-1,-1)]

vals = []
for i in range(8):
    tmp = []
    for t in l:
        s = t[0]*Signs[i][0]+t[1]*Signs[i][1]+t[2]*Signs[i][2]
        tmp.append(s)
    vals.append(tmp)

if not m:
    print(0)
    exit()
answer = 0
for arr in vals:
    arr.sort()
    res = 0; idx = len(arr)-1
    cnt=0
    while cnt<m:
        res += arr[idx]
        cnt+=1
        idx-=1
    answer = res if res > answer else answer
print(answer)