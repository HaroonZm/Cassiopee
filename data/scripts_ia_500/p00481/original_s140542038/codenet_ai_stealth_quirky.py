from collections import deque as dq
h,w,n = map(int,input().__iter__().__next__().split())
factrys = [None]*(n+1)
ss = ["X"*(w+2)]
append = ss.append
for i in range(h):
    s = "X" + input() + "X"
    if "S" in s:
        factrys[0] = (i+1,s.index("S"))
    list(map(lambda j: factrys.__setitem__(int(s[j]), (i+1, j)) if s[j] not in {'S','.','X'} else None, range(len(s))))
    append(s)
append("X"*(w+2))

def bfs(i):
    mp = [[None]*(w+2) for _ in range(h+2)]
    x,y = factrys[i]
    que = dq()
    appendq = que.append
    popq = que.popleft
    appendq((x,y))
    for count in range(10**7):
        sz = len(que)
        for _ in range(sz):
            x,y = popq()
            if ss[x][y]=='X' or mp[x][y] is not None:
                continue
            if (x,y) == factrys[i+1]:
                return count
            mp[x][y] = count
            appendq((x+1,y))
            appendq((x-1,y))
            appendq((x,y+1))
            appendq((x,y-1))

ans=0
for i in range(n):
    ret = bfs(i)
    ans+= ret if ret is not None else 0
print(ans)