import sys
from collections import deque

def encode(states):
    res = 0
    for i, s in enumerate(states):
        res |= s << (i * 2)
    return res

def decode(state_int, n):
    states = []
    for i in range(n):
        states.append((state_int >> (i * 2)) & 3)
    return states

def top_cups(n, state_int):
    # return list of stacks top cups, index is tray 0-2, value is cup size (0 means empty)
    positions = [[] for _ in range(3)]
    for i in range(n):
        tray = (state_int >> (i * 2)) & 3
        if tray != 3:
            positions[tray].append(i+1)
    top = [0, 0, 0]
    for i in range(3):
        if positions[i]:
            top[i] = max(positions[i])
    return top

def solve():
    input = sys.stdin.readline
    while True:
        n,m = map(int,input().split())
        if n==0 and m==0:
            break
        countA,*A = list(map(int,input().split()))
        countB,*B = list(map(int,input().split()))
        countC,*C = list(map(int,input().split()))
        # initial states: for each cup 1..n, record tray 0=A,1=B,2=C
        pos = [3]*n
        for x in A:
            pos[x-1]=0
        for x in B:
            pos[x-1]=1
        for x in C:
            pos[x-1]=2
        start = encode(pos)
        # target states: all cups on tray 0 or all on tray 2
        # no cups on tray 1, so no bit 1
        # 3 means not on any tray, invalid
        from collections import deque
        visited = {}
        visited[start]=0
        q = deque([start])
        ans = -1
        # moves allowed: A<->B and B<->C, no A<->C directly
        # move top cup from a to b only if a-b valid and rules respected
        while q:
            cur = q.popleft()
            d = visited[cur]
            if d>m:
                continue
            # check goal:
            cntA = cntC = 0
            # verify all cups on A or all on C
            # state cups are on tray 0,1,2 or 3 invalid
            # condition: all cups on tray 0 or all cups on tray 2
            # no cup on tray 1 allowed for goal
            allA = True
            allC = True
            for i in range(n):
                tray = (cur>>(i*2))&3
                if tray!=0:
                    allA=False
                if tray!=2:
                    allC=False
            if allA or allC:
                ans=d
                break
            # find top cups on each tray
            top = [0,0,0]
            for i in range(n-1,-1,-1):
                tray = (cur>>(i*2))&3
                if tray<=2:
                    if top[tray]<i+1:
                        top[tray]=i+1
            # try moves:
            # allowed edges: (0<->1), (1<->2)
            for a,b in [(0,1),(1,0),(1,2),(2,1)]:
                if top[a]==0:
                    continue
                cup = top[a]
                # check if move to b is valid (rule 2)
                # get top cup on b
                t_b = top[b]
                # can put cup on b only if cup < t_b or t_b==0
                # because smaller cup must be under larger or empty
                # here cups with bigger number is bigger cup
                if t_b==0 or cup<t_b:
                    # move cup from tray a to tray b
                    # update state
                    new_state = cur
                    # clear cup's 2 bits
                    new_state &= ~(3<<(2*(cup-1)))
                    # set to b
                    new_state |= b<<(2*(cup-1))
                    if new_state not in visited:
                        visited[new_state] = d+1
                        q.append(new_state)
        print(ans)

if __name__=="__main__":
    solve()