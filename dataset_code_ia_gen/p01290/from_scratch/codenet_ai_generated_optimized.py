from sys import stdin
from collections import deque

DIRS = [(1,0),(-1,0),(0,1),(0,-1),(0,0)]

def idx(x,y,W): return y*W+x

def solve():
    input = stdin.readline
    while True:
        W,H = map(int,input().split())
        if W==0 and H==0:
            break
        palace = [input().rstrip('\n') for _ in range(H)]
        Qx=Qy=Ax=Ay=None
        exits = []
        for y in range(H):
            for x in range(W):
                c = palace[y][x]
                if c=='Q':
                    Qx,Qy = x,y
                elif c=='A':
                    Ax,Ay = x,y
                elif c=='E':
                    exits.append((x,y))
        # Precompute validity
        valid = [[c!='#' for c in row] for row in palace]
        # Map position to index
        # State: (queen_pos, army_pos, turn) turn: 0 queen to move,1 army to move
        # positions are integers (y*W+x)
        N = W*H
        def neighbors(pos):
            x,y = pos%W,pos//W
            res = []
            for dx,dy in DIRS:
                nx,ny = x+dx,y+dy
                if 0<=nx<W and 0<=ny<H and valid[ny][nx]:
                    res.append(ny*W+nx)
            return res

        Qpos = Qy*W+Qx
        Apos = Ay*W+Ax
        exits_set = set((ey*W+ex) for (ex,ey) in exits)

        # Status: 0=unknown,1=win for current moving player,2=lose for current moving player
        # who is to move indicated by turn
        # We want to determine from state (Qpos,Apos,0) (queen to move)
        # If queen can force escape -> queen win
        # If army can force catch -> army win (queen lose)
        # Else draw

        # We'll build the graph backward from terminal states:
        # Army catch queen: Qpos==Apos at army turn -> army wins
        # Queen escaped: after army move, queen in exit alone -> queen wins

        from collections import deque

        M = 2*N*N  # states: queen pos, army pos, turn

        dist = [[-1]*M for _ in range(3)]  # For safety, will not use, reduce memory below

        # We'll use a 3D array: dp[qpos][apos][turn]: state status
        # But memory limit: 30*30=900 positions, states=900*900*2=1.62e6 too large for dp directly
        # We store dp in a flat array with size 2*N*N

        # Let's encode state to int:
        # s = (qpos)*N*2 + (apos)*2 + turn

        def encode(qpos,apos,turn):
            return qpos*N*2+apos*2+turn
        def decode(s):
            turn = s&1
            s>>=1
            apos = s%N
            qpos = s//N
            return qpos,apos,turn

        # For each state store:
        # status: 0=unknown,1=win(current mover),2=lose(current mover)
        status = [0]*(2*N*N)
        degree = [0]*(2*N*N)

        # Precompute moves counts (degree)
        # For each state count possible moves of current mover

        for q in range(N):
            qx,qy = q%W,q//W
            if not valid[qy][qx]: continue
            for a in range(N):
                ax,ay = a%W,a//W
                if not valid[ay][ax]: continue
                for t in (0,1):
                    s = encode(q,a,t)
                    if t==0:
                        # queen to move
                        cnt = 0
                        for nq in neighbors(q):
                            cnt +=1
                        degree[s] = cnt
                    else:
                        # army to move
                        cnt =0
                        for na in neighbors(a):
                            cnt +=1
                        degree[s] = cnt

        qpos0 = Qpos
        apos0 = Apos

        queue = deque()

        # Initialize terminal states

        # 1) Army catches queen: any state with qpos==apos at army turn -> army win -> queen lose on queen turn
        # At army move (t=1), if qpos==apos then army already caught queen: so this state is win for army (mover)
        # So at t=1 state with qpos==apos is win for army (mover)
        # Then the previous states (queen moves) losing states

        for q in range(N):
            qx,qy = q%W,q//W
            if not valid[qy][qx]: continue
            for a in range(N):
                ax,ay = a%W,a//W
                if not valid[ay][ax]: continue
                # army turn and qpos==apos
                if q==a:
                    s = encode(q,a,1)
                    status[s] = 1
                    queue.append(s)

        # 2) Queen escape: after army's turn (t=1), queen's position is in exit and qpos!=apos → queen wins
        # so after army moves:
        # If qpos in exits and qpos!=apos → queen escapes
        # mark states t=1 with qpos in exits and qpos!=apos as queen winning states for army mover?
        # yes queen wins at army move turn if queen at exit alone.

        for q in exits_set:
            for a in range(N):
                if q==a:
                    continue
                s=encode(q,a,1)
                if status[s]==0:
                    status[s]=1
                    queue.append(s)

        # Backward propagation

        # For each state:
        # if status==unknown
        # if any next move leads to losing state for opponent, then current state is winning
        # else if all next moves lead to winning states for opponent, then current is losing

        while queue:
            s = queue.popleft()
            st = status[s]
            q,a,t = decode(s)
            prev_t = 1 - t

            # find predecessors

            if t==1:
                # current mover: army
                # predecessor turn: queen
                # queen moves from q0 to q
                # army same position a
                # predecessor states: (q0,a,0) with queen's move from q0 to q

                # find all q0 where q in neighbors(q0)
                for q0 in neighbors(q):
                    ps = encode(q0,a,0)
                    if status[ps]!=0:
                        continue
                    # check if current state s is losing for player who moves in ps (queen to move)
                    # if current state is win (st==1) for mover, then from predecessor (opponent mover), this move leads to state where opponent wins
                    # so at predecessor, the mover has a move to a winning state -> predecessor is winning
                    if st==2:
                        # current state losing, so predecessor has move to losing state -> predecessor is winning
                        status[ps]=1
                        queue.append(ps)
                    else:
                        # current state winning, count degree decrements
                        degree[ps]-=1
                        if degree[ps]==0:
                            status[ps]=2
                            queue.append(ps)
            else:
                # t==0 queen to move
                # predecessor turn army move (t=1), army moves from a0 to a, queen position q same
                for a0 in neighbors(a):
                    ps = encode(q,a0,1)
                    if status[ps]!=0:
                        continue
                    if st==2:
                        # current losing for mover (queen), so predecessor (army) can move to losing state opponent, so predecessor winning
                        status[ps]=1
                        queue.append(ps)
                    else:
                        degree[ps]-=1
                        if degree[ps]==0:
                            status[ps]=2
                            queue.append(ps)

        # Now analyze initial state (qpos0, apos0, 0)
        init = encode(qpos0,apos0,0)
        res = status[init]
        # res interpretations:
        # 1 = winning for mover to move (queen to move)
        # 2 = losing for mover (queen)
        # 0 = draw (neither can force win)

        # queen moves first
        if res==1:
            print("Queen can escape.")
        elif res==2:
            print("Army can catch Queen.")
        else:
            print("Queen can not escape and Army can not catch Queen.")

if __name__=="__main__":
    solve()