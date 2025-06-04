import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break
        n = int(n)
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        # precompute ladder tops for each floor and side
        def ladder_top(building):
            top = [i for i in range(n)]
            i = 0
            while i < n:
                if building[i] == 1:
                    j = i
                    while j +1 < n and building[j+1] ==1:
                        j+=1
                    for k in range(i,j+1):
                        top[k] = j
                    i = j+1
                else:
                    i+=1
            return top

        top_a = ladder_top(a)
        top_b = ladder_top(b)

        # Next position after landing on a floor with wall type:
        # for normal wall(0): stay same floor
        # for ladder(1): go to ladder top floor
        # for slippery(2): slide down to floor with normal(0) or ladder's top floor on that side
        # sliding applies to wall landed on not to launch wall
        def next_floor(side,floor):
            # side: 0 or 1
            if side==0:
                w = a[floor]
                t = top_a[floor]
            else:
                w = b[floor]
                t = top_b[floor]
            if w==0:
                return floor
            elif w==1:
                return t
            else: # 2 slippery
                # slide down until normal(0) or ladder top floor
                # but must slide to a floor <= current floor
                # sliding means fall down on same side to a floor with wall 0 or 1
                curr = floor
                while curr>0:
                    if side==0:
                        if a[curr-1]!=2:
                            # if ladder, move to its top
                            if a[curr-1]==1:
                                return top_a[curr-1]
                            else:
                                return curr-1
                    else:
                        if b[curr-1]!=2:
                            if b[curr-1]==1:
                                return top_b[curr-1]
                            else:
                                return curr-1
                    curr-=1
                return 0 # if nothing found, slide to floor 0

        # State: (side, floor)
        # side 0 or 1
        # start from (0,0) or (1,0)
        # can jump to other side floor f,f+1,f+2 if valid floor<n
        # after jump, apply wall effect next_floor
        q=deque()
        visited=[[False]*n for _ in range(2)]
        # start positions
        for side in (0,1):
            nf=next_floor(side,0)
            if not visited[side][nf]:
                visited[side][nf]=True
                q.append((side,nf,1)) # jump count=1 (first jump from floor 1 to other building?)
        ans=-1
        # BFS
        while q:
            side,floor,jumps = q.popleft()
            if floor==n-1:
                ans=jumps
                break
            other = 1-side
            for df in (0,1,2):
                nf = floor+df
                if nf>=n:
                    continue
                nf2=next_floor(other,nf)
                if not visited[other][nf2]:
                    visited[other][nf2]=True
                    q.append((other,nf2,jumps+1))
        print(ans if ans!=-1 else "NA")

if __name__ == "__main__":
    solve()